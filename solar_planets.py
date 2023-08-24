import cv2
import numpy

#bora começar

image = cv2.imread("solar-system.jpg")
cv2.putText(image,"Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(image,"Mercurio", (100,140), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,255))
cv2.putText(image,"Venus", (200,140), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,255))
cv2.putText(image,"Terra/Lua", (300,140), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,255))
cv2.putText(image,"Marte", (400,140), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,255))
cv2.putText(image,"Jupiter", (500,30), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,255))
cv2.putText(image,"Saturno", (700,30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(image,"Urano", (1000,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(image,"Netuno", (1100,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.imshow("solar-system", image)
cv2.waitKey(0)

