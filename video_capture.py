import cv2

shot = cv2.VideoCapture(0)

while True:
  ret, frame = shot.read()
  cv2.imshow("WebCam", frame)

  if cv2.waitKey(0) & 0xFF == ord("q"):
    break

shot.release()
cv2.destroyAllWindows()
