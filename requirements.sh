#!/bin/bash

apt update
apt upgrade -y
apt install software-properties-common -y

add-apt-repository ppa:alexlarsson/flatpak

apt update
apt install xserver-xorg x11-xserver-utils xinit -y
apt install openbox -y
apt install pulseaudio minizip -y

apt install flatpak -y
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
wget https://flathub.org/repo/appstream/com.snes9x.Snes9x.flatpakref
flatpak install com.snes9x.Snes9x.flatpakref -y

apt install antimicro -y

apt install feh -y

apt install git debhelper build-essential

mkdir /home/pi/ROMS

reboot

exit