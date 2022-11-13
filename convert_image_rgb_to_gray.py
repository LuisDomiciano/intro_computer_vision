import cv2

image = cv2.imread("fruits.jpg")

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("Image Gray", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
