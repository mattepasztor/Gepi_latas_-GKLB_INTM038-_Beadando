import cv2
from pyzbar import pyzbar

path = "C:\\Users\\User\\Desktop\\test\\test.jpg"

img = cv2.imread(path)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

barcodes = pyzbar.decode(img)

for barcode in barcodes:
    x,y,w,h = barcode.rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
    
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()