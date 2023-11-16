import cv2 as cv
main_img = cv.imread('images/mainimg.jpeg',cv.IMREAD_ANYCOLOR)
temp_img = cv.imread('images/temp.jpeg',cv.IMREAD_ANYCOLOR)
# print(main_img)
# print((temp_img))

result = cv.matchTemplate(main_img,temp_img,cv.TM_CCOEFF_NORMED)
min,max,minloc,maxloc =  cv.minMaxLoc(result)
print(max)

accuracy = 0.4

if max >= accuracy:
    topleft = maxloc
    print(temp_img.shape)
    print("สวยๆ")
    
    height = temp_img.shape[0]
    width = temp_img.shape[1]
    
    bottomright = (topleft[0]+width,topleft[1]+height)
    
    cv.rectangle(main_img,topleft,bottomright,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
    cv.imshow('result',main_img)
    cv.waitKey(5000)
    cv.destroyAllWindows()
    