# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 03:08:59 2020

@author: Telmex
"""

import cv2
image = cv2.imread('ave.jpg')
print(image.shape)
# Escalando una imagen
                      #ejes   X   Y
imageOut = cv2.resize(image,(500,200), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()