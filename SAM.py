from Da import *



print(cap.get(5))


fs=[]
uwu=CreateVW('Jai1')
while(True):
    fpsCalc()
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=pp(frame)
    
    if len(frame)==0:
        continue
    fs.append(frame)
    cv2.imshow('frame',frame)
    try:
        uwu.write(frame)
    except:
        print("Error: ",frame)
    #uwu.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
uwu.release()