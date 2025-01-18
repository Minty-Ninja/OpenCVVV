import cv2
import numpy as np

c = cv2.imread("Crazy Cat.jpeg")
m = cv2.imread("Crazy Monkey.jpeg")

#Arithmetic Operations on Image - Weighted Sum : Mix the weight of the 2 images
x = cv2.addWeighted(c, 0.5, m,0.4 , 0) #0.5, o.4 etc are weight given 
cv2.imshow("K", x)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

c = cv2.imread("Crazy Cat.jpeg")
m = cv2.imread("Crazy Monkey.jpeg")

#Weighted difference 
x = cv2.subtract(m, c)

cv2.imshow("K", x)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Image Resizing
c = cv2.imread("Crazy Cat.jpeg", 1)
cv2.imshow("Original", c)
cv2.waitKey(0)
cv2.destroyAllWindows()

resize_c = cv2.resize(c, (510, 800))
cv2.imshow("New", resize_c)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Erosion - Shrink the white region in an image

m = cv2.imread("crazy Monkey.jpeg", 1)
kernel = np.ones((5,5), np.uint8)

x = cv2.erode(m, kernel)
cv2.imshow("Original", m)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("New", x)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Blurring an img

x=cv2.imread("Crazy Cat.jpeg", 1)
cv2.imshow("Original", x)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Blur 1- Gaussian Blurred Image
xces= cv2.GaussianBlur(x, (15, 15), 0)
cv2.imshow("Gaussian Blur", xces)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Blur 2- Median Blur

x=cv2.imread("Crazy Cat.jpeg", 1)
cv2.imshow("Original", x)

cv2.waitKey(0)
cv2.destroyAllWindows()

xces= cv2.medianBlur(x, 5)
cv2.imshow("Median Blur", xces)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Blur 3- Bilateral Blur

x=cv2.imread("Crazy Cat.jpeg", 1)
cv2.imshow("Original", x)

cv2.waitKey(0)
cv2.destroyAllWindows()


xces= cv2.bilateralFilter(x, 10, 100, 100)
cv2.imshow("Bilateral Blur", xces)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Adding borders on Images
x= cv2.imread("Crazy Monkey.jpeg")
cv2.imshow("Original", x)

y= cv2.copyMakeBorder(x, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = (0,0,0)) #Image, 4 Directions,Constant that is needed for border 
cv2.imshow("Bordered" ,y)

cv2.waitKey(0)
cv2.destroyAllWindows()
