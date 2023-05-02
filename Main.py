
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
import easyocr
import time
import os

import numpy as np
import cv2
import pyshine as ps
from threading import Thread



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 522)
        self.mw  = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/H.png"))
        self.label.setObjectName("label")

        # adding another label for second video
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/H.png"))
        self.label_4.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.label_4)


        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 0, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout.addWidget(self.verticalSlider_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(313, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)

        self.th = {}
        self.pushButton_2.clicked.connect(self.run_threads)
        self.pushButton_3.clicked.connect(self.run_threads)
        self.pushButton.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Added code here
        self.filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png' # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.tmp2 = None # Will hold the temporary image for display2
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value
        self.fps=0
        
        self.started = False
        self.started2 = False

    def play_videos(self,notePath):
        print(notePath)
        if notePath == 'pushButton_2':
            self.loadImage()
        if notePath == 'pushButton_3':
            self.loadImage2()
	
    def run_threads(self):
        self.th[self.mw.sender().objectName()] = Thread(target = self.play_videos, args = (self.mw.sender().objectName(),)) 
        self.th[self.mw.sender().objectName()].start()
        
    def loadImage(self): # Left Video Feed For Plate Number Recognition 
        try:
            CarCascade = cv2.CascadeClassifier('D:\Codings\pyqt6\datasets\cars1.xml')
            PlateCascade = cv2.CascadeClassifier('D:\Codings\pyqt6\datasets\Plate_Number.xml')
        except Exception as e:
            print('Warning...',e)

        if self.started:
            self.started=False
            self.pushButton_2.setText('Start')	
        else:
            self.started=True
            self.pushButton_2.setText('Stop')
        
        cam = True # True for webcam
        #if cam:
        #    vid = cv2.VideoCapture(0)
        #else:
        vid = cv2.VideoCapture('video/video3.mp4')
        
        cnt=0
        frames_to_count=20
        st = 0
        fps=0


        ax1=0
        ay=150
        ax2=1280
        #line b
        bx1=0
        by=210 #line hieght
        bx2=1280 #down line witdh

        i = 0 
        count = 0
        
        while(vid.isOpened()):
            # QtWidgets.QApplication.processEvents()	
            _, image = vid.read()
            image  = imutils.resize(image ,height = 480 )

            gray= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            #bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
            #edged = cv2.Canny(bfilter, 30, 200) 
            #contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            #contours = sorted(contours, key=cv2.contourArea, reverse=True)

            cv2.line(image,(ax1,ay),(ax2,ay),(255,0,0),2)
            cv2.line(image,(bx1,by),(bx2,by),(255,0,0),2)
            
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            try:
                cars = CarCascade.detectMultiScale(gray,1.1,4)
                plates = PlateCascade.detectMultiScale(gray,1.1,4)
              
                
                for (x, y, w, h) in plates:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (10, 228,220), 5) 
                    area = w*h
                    count += 1

                    if area > 500 :
                        frameRoi = gray[y:y+h, x:x+w] 
                        cv2.putText(frameRoi," Detected",(20,20), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
                        cv2.imshow('Video 1 ', frameRoi)
                        
                    while int(ay) <= int((y+y+h)/1):
                        if int(by) >= int((y+y+h)/1)&int(by+1) >= int((y+y+h)/1):
                            cv2.line(image,(bx1,by),(bx2,by),(0,255,0),2)
                            i = i + 1
                            filename = 'Detected ('+str(i)+")---"+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
                            cv2.imwrite(filename,frameRoi)
                            print("capture end")
                            cv2.putText(image, "capture end", (bx1+ 10 ,by+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                            break
                        else :
                            cv2.line(image,(ax1,ay),(ax2,ay),(0,255,0),2)
                            cv2.putText(image, "capture start", (ax1+ 10 ,ay+10), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),3)
                            print("capture start")                           
                            break
                #for (x, y, w, h) in plates:
                #    cv2.rectangle(frameRoi, (x, y), (x + w, y + h), (255, 0,220), 5) 
            
                #cv2.imshow('frameRoi', frameRoi )

            except Exception as e:
                pass


            if cnt == frames_to_count:
                try: # To avoid divide by 0 we put it in try except
                    #print(frames_to_count/(time.time()-st),'FPS') 
                    fps = round(frames_to_count/(time.time()-st)) 
                    st = time.time()
                    cnt=0
                except:
                    pass
            
            cnt+=1
            
            self.update(image,self.label,fps)
            key = cv2.waitKey(1) & 0xFF
            
            if self.started==False:
                break
                print('Loop break')


    def loadImage2(self): # Speed Detection  Right Speed Detection
        if self.started2:
            self.started2=False
            self.pushButton_3.setText('Start2')	
        else:
            self.started2=True
            self.pushButton_3.setText('Stop2')
    

        try:
            carCascade = cv2.CascadeClassifier('datasets/cars1.xml')
        except Exception as e:
            print('Warning...',e)

        
       
        #video ....
        cam = True # True for webcam
        #if cam:
        #    vid = cv2.VideoCapture(1)
        #else:
        vid = cv2.VideoCapture('video/video3.mp4')
        
        cnt=0
        frames_to_count=20
        st = 0
        fps=0
            
        ax1=0
        ay=150
        ax2=1280
        #line b
        bx1=0
        by=310 #line hieght
        bx2=1280 #down line witdh

        i = 1
        start_time = time.time()
        count = 0

        

        while(vid.isOpened()):
            # QtWidgets.QApplication.processEvents()	
            _, image = vid.read()
            image  = imutils.resize(image ,height = 480 )

            blurred = cv2.blur(image,ksize=(15,15))
            gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

            cv2.line(image,(ax1,ay),(ax2,ay),(255,0,0),2)
            cv2.line(image,(bx1,by),(bx2,by),(255,0,0),2)

            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            try:
                car = carCascade.detectMultiScale(
                gray,1.1,4)
                
                for (x, y, w, h) in car:
                    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)   
                    cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),1,(0,255,0),-1)
                    count += 1

                    while int(ay) == int((y+y+h)/2):
                            start_time = time.time()
                            break
                        
                    while int(ay) <= int((y+y+h)/1):
                        if int(by) >= int((y+y+h)/1)&int(by+1) >= int((y+y+h)/1):
                            cv2.line(image,(bx1,by),(bx2,by),(0,255,0),2)

                            speedtime = time.time() - start_time
                            speed = (9.144*3600)/(speedtime*1000)

                            print("Car Number "+str(i)+" Speed: "+str(speed))
                            i = i + 1
                            cv2.putText(image, "Speed: "+str(speed)+"KM/H", (bx1+ 10 ,by+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                            break
                        else :
                            cv2.line(image,(ax1,ay),(ax2,ay),(0,255,0),2)
                            cv2.putText(image, "Calcuting", (ax1+ 10 ,ay+10), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),3)
                            break
                
            except Exception as e:
                pass
            
            if cnt == frames_to_count:
                try: # To avoid divide by 0 we put it in try except
                    #print(frames_to_count/(time.time()-st),'FPS') 
                    fps = round(frames_to_count/(time.time()-st)) 
                    
                    
                    st = time.time()
                    cnt=0
                except:
                    pass
            
            cnt+=1
            
            self.update(image,self.label_4,fps)
            key = cv2.waitKey(1) & 0xFF
            if self.started2==False:
                break
                print('Loop break')

    def setPhoto(self,image, label):
        """ This function will take image input and resize it 
            only for display purpose and convert it to QImage
            to set at the label.
        """
        if label is self.label:
            self.tmp = image
        if label is self.label_4:
            self.tmp2 = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        label.setPixmap(QtGui.QPixmap.fromImage(image))

    def brightness_value(self,value):
        """ This function will take value from the slider
            for the brightness from 0 to 99
        """
        self.brightness_value_now = value
        print('Brightness: ',value)
        #self.update()
        
        
    def blur_value(self,value):
        """ This function will take value from the slider 
            for the blur from 0 to 99 """
        self.blur_value_now = value
        print('Blur: ',value)
        #self.update()


    def changeBrightness(self,img,value):
        """ This function will take an image (img) and the brightness
            value. It will perform the brightness change using OpenCv
            and after split, will merge the img and return it.
        """
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
        
    def changeBlur(self,img,value):
        """ This function will take the img image and blur values as inputs.
            After perform blur operation using opencv function, it returns 
            the image img.
        """
        kernel_size = (value+1,value+1) # +1 is to avoid 0
        img = cv2.blur(img,kernel_size)
        return img

    def update(self,image,label,fps):
        """ This function will update the photo according to the 
            current values of blur and brightness and set it to photo label.
        """
        img = self.changeBrightness(image,self.brightness_value_now)
        img = self.changeBlur(img,self.blur_value_now)

        # Here we add display text to the image
        text  =  'FPS: '+str(fps)
        img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(10,20,222),text_RGB=(255,255,255))
        text = str(time.strftime("%H:%M %p"))
        img = ps.putBText(img,text,text_offset_x=image.shape[1]-180,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(228,20,222),text_RGB=(255,255,255))
        text  =  f"Brightness: {self.brightness_value_now}"
        img = ps.putBText(img,text,text_offset_x=80,text_offset_y=425,vspace=20,hspace=10, font_scale=1.0,background_RGB=(20,210,4),text_RGB=(255,255,255))
        text  =  f'Blur: {self.blur_value_now}: '
        img = ps.putBText(img,text,text_offset_x=image.shape[1]-200,text_offset_y=425,vspace=20,hspace=10, font_scale=1.0,background_RGB=(210,20,4),text_RGB=(255,255,255))


        self.setPhoto(img,label)

    def savePhoto(self):
        """ This function will save the image"""
        self.filename = 'Snapshot Plate Dtection'+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        self.filename2 = 'Snapshot Speed Detection'+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        if self.tmp is not None:
            cv2.imwrite(self.filename,self.tmp)
            print('Image saved as:',self.filename)
        if self.tmp2 is not None:
            cv2.imwrite(self.filename2,self.tmp2)
            print('Image saved as:',self.filename2)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plate Number Recognition | ISU - Echague GATE"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Start2"))
        self.label_2.setText(_translate("MainWindow", "Brightness"))
        self.label_3.setText(_translate("MainWindow", "Blur"))
        self.pushButton.setText(_translate("MainWindow", "Take picture"))

# Subscribe to PyShine Youtube channel for more detail! 

# WEBSITE: www.pyshine.com


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
