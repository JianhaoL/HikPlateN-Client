import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import xmltodict
import json
from multiprocessing import Queue


class Client:
    def __init__(self, host, login=None, password=None, timeout=3, isapi_prefix='ISAPI'):
        """
        :param host: Host for device ('http://192.168.0.2')
        :param login: (optional) Login for device
        :param password: (optional) Password for device
        :param isapi_prefix: (optional) defaults to ISAPI but can be customized
        :param timeout: (optional) Timeout for request
        """
        self.host = host
        self.login = login
        self.password = password
        self.timeout = float(timeout)
        self.isapi_prefix = isapi_prefix
        self.statusCode = -1
        self.statusStr = "No Internet"
        self.req = self._check_session()
        self.count_events = 1


    def _check_session(self):
        """Check the connection with device

         :return request.session() object
        """

        full_url = self.host+"/ISAPI/System/deviceInfo"
        session = requests.session()
        session.auth = HTTPBasicAuth(self.login, self.password)
        try:
            response = session.request("get", full_url, timeout=self.timeout, stream=True)
        except requests.exceptions.Timeout:
            self.statusCode = -1
            self.statusStr = "Time out, probably wrong host address given"
            return
        # Maybe set up for a retry, or continue in a retry loop
        # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            self.statusCode = str(e)
            return
        # catastrophic error. bail.
        if response.status_code == 401:
            session.auth = HTTPDigestAuth(self.login, self.password)
            response = session.request("get", full_url, timeout=self.timeout)
            try:
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                if response.status_code == 401:
                    self.statusCode = -1
                    self.statusStr = "Username or password wrong!"
                    return
                else:
                    self.statusStr = str(e)
                    self.statusCode = -1
                    return
        self.jsonDics=response_parser(response)
        self.statusCode = 200
        return session

def response_parser(response, present='dict'):
    """ Convert Hikvision results
    """
    if isinstance(response, (list,)):
        result = "".join(response)
    else:
        result = response.text

    if present == 'dict':
        if isinstance(response, (list,)):
            events = []
            for event in response:
                e = json.loads(json.dumps(xmltodict.parse(event)))
                events.append(e)
            return events
        return json.loads(json.dumps(xmltodict.parse(result)))
    else:
        return result


def connect_putPlate(host, usr, passwd, data=None):
    if not data:
        return (-1, "writing null stream ")
    cam = Client(host, usr, passwd)
    if (cam.statusCode != 200):
        return(-1, cam.statusStr)
    else:
        full_url = host+'/ISAPI/Traffic/channels/1/licensePlateAuditData'
        try:
            response1 = cam.req.request("put", full_url,
                                        timeout=cam.timeout, data=data)
        except requests.exceptions.Timeout:
            cam.statusCode = -1
            cam.statusStr = "Time out, connection lost"
            return (-1, cam.statusStr)
    # Maybe set up for a retry, or continue in a retry loop
    # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            cam.statusCode = str(e)
            cam.statusCode = -1
            return (-1, cam.statusStr)
        try:
            response1.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response1.status_code==400:
                return(-400, "Client side error, check whether you have the repeated number. Wrong format of excel")
            if response1.status_code == 401:
                return (-1, "Username or password wrong")
            else:
                return(-1, str(e))
        return (200, "succeed")


def connect_putPlateNVR(host, usr, passwd, data=None):
    if not data:
        return (-1, "writing null stream ")
    cam = Client(host, usr, passwd)
    if (cam.statusCode != 200):
        return(-1, cam.statusStr)
    else:
        full_url = host+'/ISAPI/Traffic/plateList'
        try:
            response1 = cam.req.request("put", full_url,
                                        timeout=cam.timeout, data=data)
        except requests.exceptions.Timeout:
            cam.statusCode = -1
            cam.statusStr = "Time out, connection lost"
            return (-1, cam.statusStr)
        except requests.exceptions.RequestException as e:
            cam.statusCode = str(e)
            cam.statusCode = -1
            return (-1, cam.statusStr)
        try:
            response1.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response1.status_code==400:
                return(-400, "Client side error, check whether you have the repeated number. Wrong format of excel")
            if response1.status_code == 401:
                return (-1, "Username or password wrong")
            else:
                return(-1, str(e))
        return (200, "succeed")





def connect_getPlate(host, usr, passwd):
    cam = Client(host, usr, passwd)
    if(cam.statusCode!=200):
        return(-1, cam.statusStr)
    else:
        full_url =host+ '/ISAPI/Traffic/channels/1/licensePlateAuditData'
        try:
            response = cam.req.request("get", full_url,timeout=cam.timeout, data=None)
        except requests.exceptions.Timeout:
            cam.statusCode = -1
            cam.statusStr = "Time out, connection lost"
            return (-1, cam.statusStr)
        except requests.exceptions.RequestException as e:
            cam.statusCode = str(e)
            cam.statusCode = -1
            return (-1, cam.statusStr)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 401:
                return (-1, "Username or password wrong")
            if response.status_code == 403:
                full_url = host + '/ISAPI/Traffic/plateList'
                try:
                    response = cam.req.request("get", full_url, timeout=cam.timeout, data=None)
                except requests.exceptions.Timeout:
                    cam.statusCode = -1
                    cam.statusStr = "Time out, connection lost"
                    return (-1, cam.statusStr)
                except requests.exceptions.RequestException as e:
                    cam.statusCode = str(e)
                    cam.statusCode = -1
                    return (-1, cam.statusStr)
                try:
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                        return (-1, str(e))
                return (999,response.content)
            else:
                return (-1, str(e))

        return (200, response.content)















def connect_getDevInfo(host, usr, passwd):
    cam = Client(host=host, login=usr, password=passwd)
    if (cam.statusCode != 200):
        return (-1, cam.statusStr, -1)
    if isinstance(cam.jsonDics, (list,)):
        jDic=cam.jsonDics[0]
    else:
        jDic=cam.jsonDics
    return (jDic["DeviceInfo"]["deviceName"], jDic["DeviceInfo"]["model"], jDic["DeviceInfo"]["firmwareVersion"])





