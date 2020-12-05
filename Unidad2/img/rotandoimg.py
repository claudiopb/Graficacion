# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 02:48:53 2020

@author: Telmex
"""


import cv2
img = cv2.imread('ave.jpg')
print(img.shape)

fila,col,_ = img.shape
print(fila,col)

M = cv2.getRotationMatrix2D(((col-1)/2,(fila-1)/2),90,1)
print(M)
dst = cv2.warpAffine(img,M,(col,fila))

cv2.imshow('Imagen de entrada',img)
cv2.imshow('Imagen de salida',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()