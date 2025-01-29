#!/bin/bash

if [ $(id -u) -ne 0 ]; then
    red_sudo=$(echo -e "\033[1;31m" "sudo" "\033[0m")
    echo -e "\033[33m[\033[31m!\033[33m] \033[37mYou need to \033[33mrun \033[37mthis program with ${red_sudo} Please !."
    exit 1
fi

clear

sudo apt install snap -y
sudo snap install scrcpy

sudo pacman -S scrcpy -y

sudo dnf copr enable zeno/scrcpy && dnf install scrcpy -y

sudo emerge scrcpy -y

sudo apt install ffmpeg libsdl2-2.0-0 adb wget \
                 gcc git pkg-config meson ninja-build libsdl2-dev \
                 libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
                 libswresample-dev libusb-1.0-0 libusb-1.0-0-dev -y

git clone https://github.com/Genymobile/scrcpy

cd scrcpy

sudo ./install_release.sh

sudo ./release.sh

sudo apt install adb -y

git pull

sudo ./install_release.sh

sudo ninja -Cbuild-auto uninstall


sudo ./install_release.sh

sudo ./release.sh
