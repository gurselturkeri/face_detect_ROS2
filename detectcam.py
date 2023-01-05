import cv2

class A:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        self.cap = cv2.VideoCapture(0)

        
        while True:
            self._, self.img = self.cap.read()
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.1, 4)
            try:
                if self.faces[0] != []:
                    cv2.putText(img=self.img, text='Face is Detected', org=(800, 120), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=2)
                    print("yuz")
            except:
                cv2.putText(img=self.img, text='Not Detected', org=(800, 120), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=2)
        
            for (x, y, w, h) in self.faces:
                cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display
            cv2.imshow('img', self.img)

            # Stop if escape key is pressed
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break

        # Release the VideoCapture object
        self.cap.release()

a = A()