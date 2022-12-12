import time
import numpy as np
import cv2

sss=cv2.aruco
alba=sss.Dictionary_get(cv2.aruco.DICT_6X6_50)
apar=sss.DetectorParameters_create()


cap = cv2.VideoCapture(0)

def CreateVW(nn,fpss=30):
    h,w=int(cap.get(4)),int(cap.get(3))
    codi=cv2.VideoWriter_fourcc(*'DIVX')
    Ali=cv2.VideoWriter(f"{nn}.avi",codi,fpss,(w,h))
    return Ali


def pp(bb):
    thing=sss.detectMarkers(bb,alba,parameters=apar)
    try:
        print(thing[1][0])
    except:
        pass
    thing=thing[0]
    try:
        (til,tir,bir,bil)=thing[0][0]
    except IndexError:
        return []
    blabla=list(map(lambda x:list(map(int,x)),(til,tir,bir,bil)))
    (til,tir,bir,bil)=blabla

    _=cv2.line(bb,til,tir,(0,255,0),2)
    _=cv2.line(bb,tir,bir,(0,255,0),2)
    _=cv2.line(bb,bir,bil,(0,255,0),2)
    _=cv2.line(bb,bil,til,(0,255,0),2)
    #L.append(bb)
    return bb


a=time.time()
count=0
mfps=0
fpsn=1 # Total no of

def fpsCalc():
    global a
    global count
    global mfps
    global fpsn
    if int((time.time()-a))<1:
        count+=1
    else:
        print(count)
        if mfps-count<8:    # To avoid out lieres
            mfps+=count/fpsn
            mfps*=fpsn/(fpsn+1)
            fpsn-=-1
        print("M ---",mfps)
        print("inst ---",count)
        a=time.time()
        count=0