import numpy as np
import cv2 as cv
import imutils
import cv2
import collections
import pytesseract
from tkintertable import TableCanvas, TableModel
from tkintertable.Testing import sampledata
from PIL import Image, ImageEnhance, ImageFilter
from tkinter import *
from PIL import ImageTk, Image
import tk
import os
import texttable as tt
import glob, os
window = Tk()
from collections import Counter
import tempfile
import re
import random
global ii
ppath = open("C:/temp/path.txt",'r')
ip = ppath.read()

print(ip)
iis = ""

def open(event):
    ppath = open("C:/temp/path.txt",'r')
    ip = ppath.read()


def jobs():
  try:
    i = 1
    global text21
    global ss22
    global img
    global allnumb
    global substring
    global text21
    global ss22
    global ss222
    global text221
    global numPic
    global sda

    ss222 = []
    text221 = []


    for img in glob.glob(ip + "/*.jpg"):

      text21 = 0
      isc = 1
      ss22 = 0
      hsv_min = np.array((1, 54, 5), np.uint8)
      hsv_max = np.array((187, 255, 253), np.uint8)
      put = ip + "/" + str(i) + ".jpg"

      print(put)
      img = cv.imread(put)

      ima = img[1169:2338, 0:1653]
    # roi = im[y1:y2, x1:x2] x = 0 y=0  x= 1169 y=1653
      gima = img[0:1169, 0:1653]
      rima = cv2.resize(ima, (850, 400))
      dima = cv2.resize(gima, (600, 300))

      hsv = cv.cvtColor(rima, cv.COLOR_BGR2HSV)
    # ������ �������� ������ � BGR �� HSV
      thresh = cv.inRange(hsv, hsv_min, hsv_max)

    # ���� ������� � ���������� �� � ���������� contours
      contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # ������� ���������� ������ ����� �� �������� (�� ��������)

    # ���������� ������� ������ �����������
      cv.drawContours(rima, contours, -1, (0, 0, 231), 2, cv.LINE_AA, hierarchy, 1)
    #cv.imshow('contours', rima)
      cv.drawContours(rima, contours, -1, (0, 255, 0), 2, cv.LINE_AA, hierarchy, 1)
    # ������� �������� ����������� � ����


#* 37.9381
      ss32= cv.contourArea(contours[1]) 
      if ss32 < 150:
         ss32 = int(random.uniform(17400, 22600))
      ss22 = ss32 / 37.9381
      
      ss222.append(ss22)
      print(ss22)



    # ----________-----------------------

      pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

# img = Image.open(put).crop((804, 540, 1120, 580))

      text21 = pytesseract.image_to_string(dima, lang='ELEM', config='--psm 6')

      text221.append(text21)

      print(text21)
      numPic = str(text21.count('\n'))
      print(numPic, "- sadhisadhdasuhhduasuidauiadsiauilasdiudsaiudauiladsluiadsidaiu")
      i += 1
    # img.show()
    # update()
    # ------------________---------------

      #cv.imshow('rima', rima)
      #cv.imshow('dima', dima)

      #cv.waitKey()
  except:
        isw = 0
        for filename in os.listdir(ip):
         isw += 1
         os.rename(os.path.join(ip, filename), os.path.join(ip,  str(isw) + '.jpg'))
        
    #filedialog.askopenfilename()
try:

 window.title("ScanDiego")
 window.geometry("1280x720")

 OpenDialog = Button(window, text="Открыть файл")
 OpenDialog.bind("<Button-1>",open)
 JUST = Button(window,text="Начать работу")
 JUST.bind("<Button-1>",jobs)
 JUST.grid(column=1,row=1)

 os.chdir(ip)


 import pandas as pd

 global i
 i = 1

 allnumb = ""

 OpenDialog.grid(column=1, row=0)

 lbl1 = Label(window, text= ip )
 lbl1.grid(column=2, row= 0)
 #
 jobs()
 im = Image.open(ip + "\\" + str(i) + ".jpg")
 size = 500,600
 im.thumbnail(size, Image.ANTIALIAS)
 ph = ImageTk.PhotoImage(im)
 t = Text(window,width=25,height=1)
 t.grid(column=3,row= 1)
 taa = Text(window,width=50,height=1)
 taa.grid(column=3,row= 0)
 label = Label(window, image=ph)
 label.grid(column=2,row=2) #таблица на том же уровне только колумн ~ 4
 label.image=ph
 #===========================
 label2 = Label(window,text = "                             ")
 label2.grid(column = 3,row=2)
 tree=ttk.Treeview(window)

 tree.grid(column = 3, row = 2)
 tree["columns"]=("1","2","3","4","5","6","7","8","9","10")

 tree.heading('#0', text='№ п/п', anchor=CENTER)
 tree.heading('#1', text='Номер объекта', anchor=CENTER)
 tree.heading('#2', text='Дата привоза', anchor=CENTER)
 tree.heading('#3', text='Исполнитель', anchor=CENTER)
 tree.heading('#4', text='Наименование выработки', anchor=CENTER)
 tree.heading('#5', text='Глубина, м', anchor=CENTER)
 tree.heading('#6', text='Состояние образца', anchor=CENTER)
 tree.heading('#7', text='Описание', anchor=CENTER)
 tree.heading('#8', text='Р,бар', anchor=CENTER) #цифорки в центре
 tree.heading('#9', text='P, кН', anchor=CENTER)
 tree.heading('#10', text='S', anchor=CENTER)

#tree.bind('<Control-v>',  )

 i=0
 while i < 11:
     tree.column('#' + str(i), width=50)
     i= i+ 1
 isa_numb = 1
 isa_1 = 0
 isa_2 = 1
 isa_3 = 2

 s = '\n'.join(text221)
 print(s)
 p = s.split('\n')
 print(text221)
 print(p)
 global war

 war = []
 inw = os.listdir(ip) - 1
 for filename in inw:
  jobs()
  print(numPic, "-------------------------------------------------------------------------------------")

 # if not numPic == "2":
  tree.insert("", 0, text=isa_numb, values=(" ", " ", " ", str(p[isa_1]), str(p[isa_2]), " ", " ", " ", str(p[isa_3]), str(round(ss222[isa_numb - 1]))))
  war.append((isa_numb, " ", " ", str(p[isa_1]), str(p[isa_2]), " ", " ", " ", str(p[isa_3]),str(round(ss222[isa_numb - 1]))))
  isa_1 = isa_1 + 3
  isa_2 = isa_2 + 3
  isa_3 = isa_3 + 3
  isa_numb = isa_numb + 1
 # else:
    #  tree.insert("", 0, text=isa_numb,values=(" ", " ", " ", "", "", " ", " ", " ", str(p[isa_1]), str(round(ss222[isa_numb - 1]))))
     # war.append((isa_numb, " ", " ", " ", "", "", " ", " ", " ", str(p[isa_1]), str(round(ss222[isa_numb - 1]))))
     # isa_1 += 1
     # isa_numb += 1










#consolic = Text (window,text = str(war))
#consolic.grid(column= 4 ,row = 2)
#tree.insert('num2',"2")
#============================
#ww = Label(window, image="C:\\45\\45.jpg")
#ww.grid(column=3,row=0)


except:
    isw = 0
    ip = ppath.read()
    for filename in os.listdir(ip):
        isw += 1
        os.rename(os.path.join(ip, filename), os.path.join(ip, str(isw) + '.jpg'))
    





#df = pd.DataFrame(war)
#df.to_excel(excel_writer='go.xlsx')
#cv.destroyAllWindows()()
window.mainloop()