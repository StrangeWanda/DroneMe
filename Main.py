import stil_madd as smi
from Bas import *
from LRboy import *
import cv2
'''
V=smi.conn("/dev/ttyAMA0")
smi.arm(V)
smi.Take_off(V,1)

print("Set default/target airspeed to 3")
V.airspeed = 3
'''

cap = cv2.VideoCapture(0)
frame_W=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_H=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
rot_deg=2
BOX_ar=15
th=45

def turn(loli):
	if loli=="L":
		# smi.rot(vehicle=V, heading=rot_deg)
		smi.print("[green]Turn Left[/green]")
	else:
		#smi.rot(vehicle=V, heading=rot_deg,wise=-1)
		smi.print("[violet]Turn Right![/violet]")



def det_aru_box():
	print(cap.read())
	ret, frame = cap.read()
	while not is_aric(frame, BOX_ar):
		if frame is None:
			continue
		
		ret, frame = cap.read()
		#cv2.imshow('frame',frame)
		#frame=Dbox_cor(frame)
		
		
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		#cent=center(*(nana(frame,id)[0][0]))

	c=nana(frame, BOX_ar)
	pn=center(*(c[0]))
	frame = cv2.circle(frame,pn,radius=1,color=(0,0,255),thickness=-1)
	lol=l_r(pn,frame_W,frame_H)

		
	smi.print(f'[blue]Detected on {"Left" if "L"==lol else "Right"}![/blue]')
	pvs=lol

	while pvs == lol:
		
		# Capture frame-by-frame
		ret, frame = cap.read()
		#cv2.imshow('frame',frame)
		#frame=Dbox_cor(frame)
		
		if len(frame)==0:
			continue
		
		try:
			c=nana(frame, BOX_ar)
			pn=center(*(c[0]))
			frame = cv2.circle(frame,pn,radius=1,color=(0,0,255),thickness=-1)

			lol=l_r(pn,frame_W,frame_H)
			turn(lol)
			
		except TypeError as e:
			pass
		frame=Dbox_cor(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
det_aru_box()
smi.print("The Center")