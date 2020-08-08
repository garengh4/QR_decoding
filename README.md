# QR_decoding
The intent of this code is to stream live feed + capture/decode detected QR codes. The follow

What you need:
- Raspberry pi zero
- MicroSD with Raspberry pi NOOBS (USE PROGRAM: SD card formatter)
- camera, micro-usb with interfaces, etc.
- HDMI, secondary monitor

1) Connecting to the internet to download --> full tutorial here: https://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/
   (USE PROGRAM: PuTTY + WinSCP)
   /boot/config.txt --> dtoverlay=dwc2
   /boot/cmdline.txt --> ... rootwait modules-load=dwc2,g_ether quiet ...
    
# Personal connection configuration 2020/08/08
   Host Name: dobby.local
   login as : pi
   password : aeroclub

2) Installing QR Decoding packages --> full tutorial here: https://github.com/rijinmk/code-qr-code-reader-rpi3
   check internet connection --> ping 8.8.8.8 (Return to step 1 if fail)
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install fswebcam
   sudo apt-get install libzbar0 libzbar-dev
   sudo pip install zbarlight
   
3) Create/store/transfer files in appropriate directories
   test93.py  --> /home/pi/
   qr_codes   --> /home/pi/
   qr_log.txt --> /home/pi/

4) Write programs into autostart

   /etc/xdg/lxsession/LXDE-pi/autostart
   @lxpanel --profile LXDE-pi
   @pcmanfm --desktop --profile LXDE-pi
   @xscreensaver -no-splash 
   point-rpi

   @xset s off
   @xset -dpms
   @lxterminal -e python /home/pi/test93.py
   
# POINTS OF NOTE: 
- Python version 2 works better 
- bashrc forces 2 instances of the program to run on startup, causing failure. Add this to last line:

    /home/pi/.bashrc
    alias python='/usr/bin/python2'
    cd /home/pi/Desktop
    python2 on_start_cmds.py



   
   
