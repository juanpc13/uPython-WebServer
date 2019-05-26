import network
import json

ap_ssid = "ESP32"
ap_password = "87654321"
ap_authmode = 3  # WPA2

wifiFile = 'data/wifi.json'


class WifiManager:
    def __init__(self):
        self.ap = network.WLAN(network.AP_IF)
        self.sta = network.WLAN(network.STA_IF)

    def connect(self):
        # Activamos STACIONARIO
        self.sta.active(True)

        # Buscamos los wifi cercanos y los guardados
        wifiScanList = self.sta.scan()

        # Cargamos los wifi de la memoria flash SPIFFS
        with open(wifiFile, 'r') as f:
            jsonWifiList = json.loads(f.read())

        # Obtener lista de coincidencias
        wifiList = []
        for w in wifiScanList:
            for local in jsonWifiList:
                if w[0].decode("utf-8") == local["ssid"]:
                    wifiList.append(w)

        # Encontrar wifi mas cercano
        wifi = None
        for w in wifiList:
            if wifi is None or w[3] >= wifi[3]:
                wifi = w
        print("***BestWifiSignal=", wifi[0].decode("utf-8"))

        if wifi is not None:
            # SSID
            ssid = wifi[0].decode("utf-8")
            # PassWord
            for w in jsonWifiList:
                if w["ssid"] == ssid:
                    passwd = w["password"]
                    break
                else:
                    passwd = None

            # Conectar
            if passwd is not None:
                self.sta.connect(ssid, passwd)
                while not self.sta.isconnected():
                    pass
                print('network config:', self.sta.ifconfig())
            else:
                self.sta.connect(ssid)
            return True
        return False

    def getSTA(self):
        return self.sta

    def getAP(self):
        return self.ap

    def createAP(self):
        self.ap.active(True)
        self.ap.config(essid=ap_ssid, password=ap_password,
                       authmode=ap_authmode)
        return True
