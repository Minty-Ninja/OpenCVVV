#importing library
import cv2

#Read an image
x= cv2.imread("Coloured image.jpg", cv2.IMREAD_COLOR)

#SHow the image
cv2.imshow("Coloured Image", x)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

#Reading and displaying image in grayscale
red= cv2.imread("Coloured image.jpg", 0)

#SHow the image
cv2.imshow("Coloured Image", red)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Saving image in a new path
import cv2

#OS to handle directory functionality
import os

file_path = "C:\\Users\\DELL\\Desktop\\Coding Stuff\\Python Stuff Fr\\OpenCVVV"

#Read the image
grey = cv2.imread("Coloured image.jpg", 0)

#SHow the image
cv2.imshow("Coloured Image", red)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Changing current execution directory
os.chdir(file_path)
cv2.imwrite("BW.png", grey)
print("Successsfully Saved")

#Format of saving RGB in OpenCV = BGR

#Printing an image in different colour format
import cv2

#Read the image
RGB = cv2.imread("RGB.png", 1)

#Split the image in Blue, Green and Red
b,g,r = cv2.split(RGB)

cv2.imshow("Original", RGB)
cv2.waitKey()

cv2.imshow("Blue Saturation", b)
cv2.waitKey()

cv2.imshow("Green Saturation", g)
cv2.waitKey()

cv2.imshow("Red Saturation", r)
cv2.waitKey()


cv2.destroyAllWindows()
