import cv2

image = cv2.imread("fruits.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(image)

cv2.imshow("Canal H", hue)
cv2.imshow("Canal S", saturation)
cv2.imshow("Canal V", value)

cv2.waitKey(0)
cv2.destroyAllWindows()
