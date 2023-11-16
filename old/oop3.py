import cv2 as cv
import numpy as np

class findpic :
    def __init__(self,main_img,temp_img):
        
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def find(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        min,max,minloc,maxloc =  cv.minMaxLoc(result)
        print(max)
        print(maxloc)
        
        acc = 0.4
        
        location = np.where(result >= acc )
        location = list(zip(*location[::-1]))
        print(type(location))
        # print(location)
        
        if location:
            hieght = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
            
            rectangle = []
            point = []
            
            for l in location :
                rect = [int(l[0]),int(l[1]),width,hieght]
                rectangle.append(rect)
            
            rex,weights = cv.groupRectangles(rectangle,groupThreshold=1,eps=0.5)
            exit
            
            if len(rex):
                for (x,y,w,h) in rex:
                    print(x,y,w,h)
                    topleft = (x,y)
                    bottomright = (x+w,y+h)
                    cv.rectangle(self.main_img,topleft,bottomright,color=(255,0,255),thickness=2 ,lineType=cv.LINE_8)
                    
                    centerX = int(w/2)  +  x
                    centerY = int(h/2)  +  y
                    
                    point.append((centerX,centerY))
                    cv.drawMarker(self.main_img,(centerX,centerY),color=(255,0,255),thickness=4,markerSize=10,markerType=cv.MARKER_DIAMOND)
                    
                

        
        cv.imshow('result',self.main_img)
        cv.waitKey(5000)
        cv.destroyAllWindows()
find = findpic('images/op.jpeg','images/opp.jpeg')
find.find()