import cv2

path = "C:\\Users\\User\\Desktop\\test\\test.jpg"

img = cv2.imread(path)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

