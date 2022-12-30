import time
import numpy as np
import cv2
import LRboy

sss=cv2.aruco
alba=sss.Dictionary_get(cv2.aruco.DICT_6X6_50)
apar=sss.DetectorParameters_create()




koli = None

def Dbox_cor(bb):
    (s, ids, rejected) = cv2.aruco.detectMarkers(bb, alba,parameters=apar)
    for f in s:
        try:
            (til,tir,bir,bil)=f[0]
        except IndexError:
            return bb
        blabla=list(map(lambda x:list(map(int,x)),(til,tir,bir,bil)))
        (til,tir,bir,bil)=blabla

        _=cv2.line(bb,til,tir,(0,255,0),2)
        _=cv2.line(bb,tir,bir,(0,255,0),2)
        _=cv2.line(bb,bir,bil,(0,255,0),2)
        _=cv2.line(bb,bil,til,(0,255,0),2)
    return bb

def is_aric(pp,an=False):
    try:
        (corners, ids, rejected) = cv2.aruco.detectMarkers(pp, alba,parameters=apar)
        return (len(corners)>0 and not(an)) or (an and (an in ids))
    except:
        return False

def nana(pp,id):
    (corners, ids, rejected) = cv2.aruco.detectMarkers(pp, alba,parameters=apar)
    if len(corners) > 0:
        try:
            return corners[list(ids).index(id)]
        except ValueError as e:
            pass



if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
    #cv2.imshow('frame',frame)
    #frame=pp(frame
        # print(cv2.aruco.detectMarkers(frame, alba,parameters=apar)[1])
        if len(frame)==0:
            continue
        c=nana(frame,15)
        frame = Dbox_cor(frame)
        
        try:
            
            pn=LRboy.center(*(c[0]))
            print(pn)
            frame = cv2.circle(frame,pn,radius=1,color=(0,0,255),thickness=-1)
            
        except TypeError as e:
            pass
        
        

        cv2.imshow("d",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        cap.release()
        cv2.destroyAllWindows()