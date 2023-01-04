#!/bin/bash

sudo su

apt update
apt install software-properties-common -y

add-apt-repository ppa:alexlarsson/flatpak

apt upgrade -y
apt install xserver-xorg x11-xserver-utils xinit -y
apt install openbox lxterminal -y
apt install pulseaudio -y

apt install flatpak -y
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
wget https://flathub.org/repo/appstream/com.snes9x.Snes9x.flatpakref
flatpak install com.snes9x.Snes9x.flatpakref

apt install antimicro -y

reboot

exit