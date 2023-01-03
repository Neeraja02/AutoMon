from pyscreenshot import grab
import cv2
import pytesseract
import time
import os
import sim

class ScrRead(sim.WheelLoader):
    def __init__(self):
        time.sleep(5)
        im = grab(bbox = (174, 205, 1181, 911))
        im.save(r"F:\Nivedita_College\CatCodathon\img\im1.png")
        while True:
            p1 = self.passcount("im1.png")
            #time.sleep(1)
            im = grab(bbox = (174, 205, 1181, 911))
            im.save(r"F:\Nivedita_College\CatCodathon\img\im2.png")
            #time.sleep(10)s
            p2 = self.passcount("im2.png")
            #print(p1, p2)
            if int(p1) != int(p2):
                print(p1, p2)
                sim.storeButton.invoke()
                #print("inv")
                #pass
                #click store
            os.remove(r"F:\Nivedita_College\CatCodathon\img\im1.png")
            os.rename(r"F:\Nivedita_College\CatCodathon\img\im2.png", r"F:\Nivedita_College\CatCodathon\img\im1.png")

    def passcount(self,img):        
        path = r"F:\Nivedita_College\CatCodathon\img\\" + img
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # Grayscale and Otsu's threshold
        print(path)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Perform text extraction
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
        data = data.replace('\n',"")
        i1 = data.index("Pass Count")
        #print(data)
        i2 = data.index("STORE")
        r = data[i1 + len("Pass Count"):i2]
        return(r)
    
    
    
if __name__ == "__main__":
    obj = ScrRead()
    obj.mainloop()
