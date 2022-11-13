import cv2

image = cv2.imread("fruits.jpg")
blue, green, red = cv2.split(image)

cv2.imshow("Canal R", red)
cv2.imshow("Canal G", green)
cv2.imshow("Canal B", blue)

cv2.imwrite("fruits-canal-red.jpg", red)
cv2.imwrite("fruits-canal-green.jpg", green)
cv2.imwrite("fruits-canal-blue.jpg", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
