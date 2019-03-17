import cv2
import numpy as np
a=cv2.imread('proimage1.jpg')
cv2.imshow('proimage',a)
# cv2.waitKey(1000)
cv2.destroyAllWindows()
imggray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow('proimage',imggray)
# cv2.waitKey(1000)
cv2.destroyAllWindows()
print(imggray)
reimage=cv2.resize(imggray,(256,256))
cv2.imshow('',reimage)
arr1=np.zeros((128,128))
for i in range(128):
    for j in range(128):
        arr1[i][j]=reimage[i][j]
imgpart1=np.uint8(arr1)
cv2.imshow('',imgpart1)
# cv2.waitKey(1000)
arr2=np.zeros((128,128))
for i in range(128):
    for j in range(128):
        arr2[i][j]=reimage[i+128][j]
imgpart2=np.uint8(arr2)
cv2.imshow('',imgpart2)
# cv2.waitKey(1000)
arr3=np.zeros((128,128))
for i in range(128):
    for j in range(128):
        arr3[i][j]=reimage[i][j+128]
imgpart3=np.uint8(arr3)
cv2.imshow('',imgpart3)
# cv2.waitKey(1000)
arr4=np.zeros((128,128))
for i in range(128):
    for j in range(128):
        arr4[i][j]=reimage[i+128][j+128]
imgpart4=np.uint8(arr4)
cv2.imshow('',imgpart4)
# cv2.waitKey(1000)
cv2.destroyAllWindows()
n=int(input('enter:'))
arr5=np.zeros((256-2*n,256-2*n))
for i in range(256-(2*n)):
    for j in range(256-(2*n)):
        arr5[i][j]=reimage[n+i][j+n]
imgpart5=np.uint8(arr5)
cv2.imshow('',imgpart5)
# cv2.waitKey(1000)
cv2.destroyAllWindows()
