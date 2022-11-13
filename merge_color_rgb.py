import cv2

image = cv2.imread("fruits.jpg")
blue, green, red = cv2.split(image)

image = cv2.merge((blue, green, red))
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

