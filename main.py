import json
from lib.microWebServer.microWebSrv import MicroWebSrv

pins = [0,2,]


@MicroWebSrv.route('/status', "GET")
def handlerStatus(httpClient, httpResponse):    
    # Create a Json Status from reading pins(NOT HARCODE)
    content = """{"pins":[{"gpio1":1},{"gpio2":0}]}""" 
    httpResponse.WriteResponseOk(headers=None, contentType="text/plain", contentCharset="utf-8", content=content)


srv = MicroWebSrv(webPath='www/')
srv.MaxWebSocketRecvLen = 256
srv.WebSocketThreaded = False
srv.Start()
