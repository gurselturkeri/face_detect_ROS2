import cv2
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class A(Node):
    def __init__(self):
        super().__init__('a')
        self.publisher_ = self.create_publisher(String, '/topic', 10)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        self.cap = cv2.VideoCapture(0)

        while True:
            self._, self.img = self.cap.read()
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.1, 4)
            try:
                if self.faces[0] != []:
                    self.publisher_.publish(self.msg)
                    cv2.putText(img=self.img, text='Face is Detected', org=(900, 120), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=2)
                    print("yuz")
            except:
                cv2.putText(img=self.img, text='Not Detected', org=(900, 120), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=2)
        
            for (x, y, w, h) in self.faces:
                cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                self.uzaklik = round((1/w) * 10000 + 20,3)
                self.uzaklik = 'Distance: ' + str(self.uzaklik) + 'cm'
                cv2.putText(img=self.img, text=self.uzaklik, org=(x, y-10), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 128, 0),thickness=2)
                
                print(self.uzaklik)

            cv2.putText(img=self.img, text='@gurselturkeri', org=(960, 710), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(150, 120, 20),thickness=2)
            cv2.imshow('img', self.img)

            self.msg = String()
            self.msg.data = "yuz"
            
            
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break

        # Release the VideoCapture object
        self.cap.release()


def main(args=None):
    rclpy.init(args=args)
    a = A()
    rclpy.spin(a)
    a.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
