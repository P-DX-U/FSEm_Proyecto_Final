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

import os
import shutil
import time

rutaOrigen = '/media/usb0/ROMS/'
rutaDestino = '/home/pi/ROMS/'

def romsCopy():
    while True:
        try:
            if os.path.exists(rutaOrigen) == True:
                if len(os.listdir(rutaOrigen)) >= 1:
                    archivos = os.listdir(rutaOrigen)
                    print(archivos)
                    for i in archivos:
                        if os.path.exists(rutaDestino + i) == False:
                            if i.endswith(".smc"):
                                shutil.copy(rutaOrigen + i, rutaDestino)
                            if i.endswith(".sfc"):
                                shutil.copy(rutaOrigen + i, rutaDestino)
                            if i.endswith(".zip"):
                                shutil.copy(rutaOrigen + i, rutaDestino)
                        else:
                            print('Archivo ' + i + ' repetido.\n')
                            pass
                    os.system('sudo umount /media/usb0')
                    print('USB desmontado.\n')
                else:
                    os.system('sudo umount /media/usb0')
                    print('USB desmontado.\n')
            else:
                time.sleep(1)

        except KeyboardInterrupt:
            return

def main():
    romsCopy()

if __name__ == '__main__':
    main()
