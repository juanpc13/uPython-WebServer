# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#import webrepl
# webrepl.start()

from lib.wifiManager.wifiManager import WifiManager

wifiM = WifiManager()

if wifiM.connect():
    print("********WIFI is Connected**********")
else:
    wifiM.createAP()
    print("********WIFI as AccessPoint********")
