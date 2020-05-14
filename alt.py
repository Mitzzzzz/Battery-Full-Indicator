import time
import psutil
import win32api
from win32con import MB_SYSTEMMODAL


def getbatterydetails():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    return battery, plugged, percent


boxOpen = False
while True:
    batteryval, pluggedval, percentval = getbatterydetails()
    if not pluggedval:
        boxOpen = False
        print("Plugged in " + str(pluggedval) + " Remaining " + percentval)
    if pluggedval:
        print("Plugged in " + str(pluggedval) + " Charged " + percentval)
        if percentval >= "99" and not boxOpen:
            win32api.MessageBox(0, 'Battery Fully Charged, disconnect charger', 'FULL', MB_SYSTEMMODAL)
            boxOpen = True
    time.sleep(40)
