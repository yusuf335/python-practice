#!/usr/bin/python

import io
import sys
import fcntl
import time
import copy
import string
from AtlasI2C import (
    AtlasI2C
)

def get_devices():
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []

    for i in device_address_list:
        device.set_i2c_address(i)
        response = device.query("i")

        # check if the device is an EZO device
        checkEzo = response.split(",")
        if len(checkEzo) > 0:
            if checkEzo[0].endswith("?I"):
                # yes - this is an EZO device
                moduletype = checkEzo[1]
                response = device.query("name,?").split(",")[1]
                device_list.append(AtlasI2C(address = i, moduletype = moduletype, name = response))
    return device_list

def main():

    device_list = get_devices()

    if len(device_list) == 0:
        print ("No EZO devices found")
        exit()

    device = device_list[0]

    while True:

        delaytime = device.long_timeout

        # check for polling time being too short, change it to the minimum timeout if too short
        if delaytime < device.long_timeout:
            print("Polling time is shorter than timeout, setting polling time to %0.2f" % device.long_timeout)
            delaytime = device.long_timeout
        try:
            while True:
                print("-------press ctrl-c to stop the polling")
                for dev in device_list:
                    dev.write("R")
                time.sleep(delaytime)
                for dev in device_list:
                    print(dev.read())

        except KeyboardInterrupt:       # catches the ctrl-c command, which breaks the loop above
            print("Continuous polling stopped")
            print_devices(device_list, device)

if __name__ == '__main__':
    main()
