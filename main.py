from CO2Meter import *
import time

REPORT_INTERVAL = 3

sensor = CO2Meter("/dev/hidraw0")
while True:
    values = sensor.get_data()
    print(values)
    time.sleep(REPORT_INTERVAL)
