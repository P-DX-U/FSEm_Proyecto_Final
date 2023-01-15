#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# usb_roms2pi.py
# Author: Pablo Gonzalez
# License: MIT
# Fecha: 2023-01-14
#
# Copy the SNES roms in format .smc, .sfc and .zip from a usb 
# storage drive to /home/pi/ROMS directory in the Raspberry Pi, 
# with automatic dismount of the usb storage drive. 
#
# ## ############################################################

import os # Import miscellaneous operating system interfaces.
import shutil # Import High-level file operation to copy the roms.
from time import sleep # Import pause function.
import RPi.GPIO as GPIO # Imports GPIO control of Raspberry Pi.

# Mounting point of the usb storage drive with ROMS folder inside (Source).
srcPath = '/media/usb0/ROMS/'
# ROMS folder in the Raspberry Pi (Destination).
destPath = '/home/pi/ROMS/'  

GPIO.setwarnings(False) # Disable warnings.
GPIO.setmode(GPIO.BOARD) # Library config to use an especific pin.
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) # Pin 32 as output and enable in low. 

# Function to copy rom files from usb drive into the Raspberry Pi ROMS path.
def romsCopy():
    while True: # Program works every time
        try: # Exception handling.
            # Detects if the usb drive is plugged in.
            if os.path.exists(srcPath) == True:
                # Starts if there is one or more files.
                if len(os.listdir(srcPath)) >= 1:
                    # Creates a list with the name of the files.
                    archivos = os.listdir(srcPath)
                    # print(archivos)
                    for i in archivos:
                        # If the rom does not exists in the destination path,
                        # it is copied.
                        if os.path.exists(destPath + i) == False:
                            if i.endswith(".smc"):
                                shutil.copy(srcPath + i, destPath)
                            if i.endswith(".sfc"):
                                shutil.copy(srcPath + i, destPath)
                            if i.endswith(".zip"):
                                shutil.copy(srcPath + i, destPath)
                        else: # Skips the repeated file.
                            # print('The file > ' + i + ', is repeated.\n')
                            pass
                    # Dismount the usb drive when checks every file or the path
                    # is empty.
                    os.system('sudo umount /media/usb0')
                    #print('USB desmontado.\n')
                    # The led lights up to indicate that the usb drive 
                    # can be disconnected.
                    GPIO.output(32, GPIO.HIGH)
                    sleep(3)
                else:
                    os.system('sudo umount /media/usb0')
                    #print('USB desmontado.\n')
                    GPIO.output(32, GPIO.HIGH)
                    sleep(3)

            else: # Take a pause when the usb drive is unmounted.
                # Turns off the led and restarts the sequence.
                GPIO.output(32, GPIO.LOW) 
                time.sleep(1)

        except KeyboardInterrupt:
            return

def main():
    romsCopy()

if __name__ == '__main__':
    main()
