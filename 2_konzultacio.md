# Választott téma: Vonalkód, QR-kód olvasása: Egy- vagy kétdimenziós kódok olvasása fényképről

## Téma kidolgozásának gyakorlati megvalósítása

A feladat egyik lehetséges megoldása a következő:
1. Szükséges csomagok:
   * [OpenCV](https://opencv.org/)
   * [Pyzbar](https://pypi.org/project/pyzbar/)
2. Logika:
   * Tesztfájlok elérési útjának megadása és megnyitása: 
  
      import cv2

      path = "C:\\Users\\User\\Desktop\\test\\test.jpg"

      img = cv2.imread(path)

      cv2.imshow("img",img)

      cv2.waitKey(0)

      cv2.destroyAllWindows()'
   * Barcode kijelölése és dekódolása
     * barcodes = pyzbar.decode(img) **barcodes objektum x,y,w,h helyét megadja a vonalkódnak**
     * for barcode in barcodes: **az összes vonalkód megtekintéséhez**
         x,y,w,h = barcode.rect **vonalkód analizálásához** 
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4) **vonalkód kijelöléséhez** 
   * A dekódolt adatok és a kódolás típusának megjelenítése a képeken
```
      cv2.imshow("img",img)

      cv2.waitKey(0)

      cv2.destroyAllWindows()


[QR code generator](https://hu.qr-code-generator.com)
