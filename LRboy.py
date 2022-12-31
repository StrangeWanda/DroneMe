# Program to check if the box is at the left or rigth of the frame 

# define a function to find the center of the 4 points

def center(p1,p2,p3,p4):
    return (int((p1[0]+p2[0]+p3[0]+p4[0])/4),int((p1[1]+p2[1]+p3[1]+p4[1])/4))

def l_r(p,width,hight):
    if p[0]<int(width/2):
        return 'L'
    return 'R'


if __name__=="__main__":
    print(center((1,1),(-1,-1),(1,-1),(-1,1)))
    
