#QR_decoding
The intent of this code is to stream live feed + capture and decode detected QR codes

What you need: <br/>
--> Raspberry pi zero <br/>
--> MicroSD with Raspberry pi NOOBS (USE PROGRAM: SD card formatter) <br/>
--> camera, micro-usb with interfaces, etc. <br/>
--> HDMI, secondary monitor <br/>

1) Connecting to the internet to download --> full tutorial here: https://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/ <br/>
(USE PROGRAM: PuTTY + WinSCP) <br/>
/boot/config.txt --> dtoverlay=dwc2 <br/>
/boot/cmdline.txt --> ... rootwait modules-load=dwc2,g_ether quiet ... <br/>
    
   #Personal connection configuration 2021/01/23 <br/>
    Host Name: raspberrypi.local <br/>
    login as : pi <br/>
    password : Terminal <br/>

2. Installing QR Decoding packages --> full tutorial here: https://github.com/rijinmk/code-qr-code-reader-rpi3 <br/>
   check internet connection --> ping 8.8.8.8 (Return to step 1 if fail) <br/>
   
   sudo apt-get update <br/>
   sudo apt-get upgrade <br/>
   sudo apt-get install fswebcam <br/>
   sudo apt-get install libzbar0 libzbar-dev <br/>
   sudo pip install zbarlight <br/>
   
3. Create/store/transfer files in appropriate directories <br/>
   test93.py  --> /home/pi/ <br/>
   qr_codes   --> /home/pi/ <br/>
   qr_log.txt --> /home/pi/ <br/>

4. Write programs into autostart <br/>

   /etc/xdg/lxsession/LXDE-pi/autostart <br/>
   @lxpanel --profile LXDE-pi <br/>
   @pcmanfm --desktop --profile LXDE-pi <br/>
   @xscreensaver -no-splash <br/>
   point-rpi

   @xset s off <br/>
   @xset -dpms <br/>
   @lxterminal -e python /home/pi/test93.py <br/>
   
POINTS OF NOTE: <br/>
--> Python version 2 works better <br/>
--> bashrc forces 2 instances of the program to run on startup, causing failure (method scrapped). If you'd like to explore this failure, add this to last line <br/>

   /home/pi/.bashrc <br/>
   alias python='/usr/bin/python2' <br/>
   cd /home/pi/Desktop <br/>
   python2 on_start_cmds.py <br/>

Waking up black screen <br/>
    export DISPLAY=:0 <br/>
    xset s reset <br/>
    
Check if camera is enabled. If it returns start_x=1 then the camera is indeed enabled. <br/>
    grep start_x=1 /boot/config.txt <br/>

Check camera status <br/>
    vcgencmd get_camera
   
   
