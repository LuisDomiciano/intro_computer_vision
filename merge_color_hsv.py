import cv2

image = cv2.imread("fruits.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(image)

cv2.imshow("canal H", hue)
cv2.imshow("Canal S", saturation)
cv2.imshow("Canal V", value)

image = cv2.merge((hue, saturation, value))
image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imshow("Merge Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
