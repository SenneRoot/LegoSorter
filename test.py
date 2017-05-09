import cv2

image = cv2.imread("image.jpg")
color = image[200, 550]
print color
