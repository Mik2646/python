import cv2 as cv
import numpy as np

class Picture:
    def __init__(self,main_img,temp_img):
        
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def findpic(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        min,max,minloc,maxloc =  cv.minMaxLoc(result)
        print(max)
        print(maxloc)
        
        acc = 0.4
        
        if max >= acc:
            topleft = maxloc
            print(self.temp_img.shape)
            print("สวยๆ")
    
            height = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
    
            bottomright = (topleft[0]+width,topleft[1]+height)
    
            cv.rectangle(self.main_img,topleft,bottomright,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
            
            font = cv.FONT_ITALIC
            
            position = (topleft[0]+30,topleft[1]-15)
            fontsize = 1.5
            color = (255,255,255,255)
            cv.putText(self.main_img,"test_text",position,font,fontsize,color,thickness=2)
            
            cv.imshow('result',self.main_img)
            cv.waitKey(5000)
            cv.destroyAllWindows()