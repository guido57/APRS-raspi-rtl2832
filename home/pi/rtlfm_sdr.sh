#!/bin/bash
cd /home/pi
pkill -9 rtl_fm
pkill -9 python
python led.py # turn the white led on
rtl_fm -f 144.8e6 -M nbfm  -g 40 -F 4  -r 24000 - |  direwolf -c rtlfm_sdr.conf -r 24000 -D 1 -B 1200 -T "%H:%M:%S %Z"  -  | tee  rtlfm_sdr.log
