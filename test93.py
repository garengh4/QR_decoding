import zbarlight
import os
import sys
import PIL
import time
from picamera import PiCamera
from time import sleep
camera = PiCamera()
width = 860
height = 950
x=600
y=0
camera.framerate = 15
camera.preview_fullscreen = False
camera.preview_window = (x,y,width,height)

i =0
for i in range(69):
	print 'Opening Live Feed...'
	camera.start_preview()
	sleep(30)
	camera.stop_preview()
	sleep(2)
	try:
		f = 1
		qr_count = len(os.listdir('qr_codes'))
		print '--Taking picture..'
		camera.start_preview()
		sleep(5)
		camera.capture('/home/pi/qr_codes/qr_%s.jpg' % qr_count)
		camera.stop_preview()
		print 'Picture taken..'
	except:
		f = 0
		print 'Picture couldn\'t be taken..'
	if(f):
		print 'Scanning image..'
		f = open('qr_codes/qr_'+str(qr_count)+'.jpg','rb')
		qr = PIL.Image.open(f);
		qr.load()
		codes = zbarlight.scan_codes('qrcode',qr)
		if(codes==None):
			os.remove('qr_codes/qr_'+str(qr_count)+'.jpg')
			print 'No QR code found'
		else:
			print 'DETECTED! --> QR code(s):'
			print codes
			f = open('qr_log.txt','a')
			for i in range(len(codes)):
				f.write(codes[i])
				if(i!=len(codes)-1):
					f.write('^')
			f.write('~')
	i=i+1
