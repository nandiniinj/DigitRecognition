import pygame, sys
from pygame.locals import *
import numpy as np 
from keras.model import load_model
import cv2

WHITE=(255,255,255)
BLACK=(0,0,0)

MODEL =load_model("D:\model development\mnist.h5")
pygame.init()
BOUNDARYINC=5
WINDOWSIZEX=640
WINDOWSIZEY=480
IMAGESAVE=False

displaysurface=pygame.display.set_model((640,480))
white_int=displaysurface.map_rgb(WHITE)
pygame.display.set_caption("My Model")

PREDICT = True

imwriting= False

number_xcord=[]
number_ycord=[]
inmg_cnt=1

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord =event.pos
            pygame.draw.circle(displaysurface, WHITE,(xcord,ycord),4,0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)

        if event.type==MOUSEBUTTONDOWN:
            iswriting= True
        
        if event.type == MOUSEBUTTONUP:
            iswriting= False
            number_xcord=sorted(number_xcord)
            number_ycord=sorted(number_ycord)

            rect_min_x , rect_max_x =max(number_xcord[0]-BOUNDARYINC,0),min(WINDOWSIZEX, number_xcord[-1]+BOUNDARYINC)

            rect_min_y , rect_max_y =max(number_ycord[0]-BOUNDARYINC,0),min(WINDOWSIZEY, number_ycord[-1]+BOUNDARYINC)

            number_xcord=[]
            number_ycord=[]
            img_arr=np.array(pygame.PixelArray(displaysurface))
            if IMAGESAVE:
                cv2.imwrite("image.png")
                img.count+=1
            
            if PREDICT:
                image=cv2.resize(img_arr,(28,28))
                image=np.pad(image, (10,10),'constant',constant_values=0)
                image=cv2.resize(image,(28,28))/white_int
                label=str(LABELS[np.argmax(MODEL.predict(image.reshape(1,28,28,1)))]).title()
                pygame.draw.rect(displaysurface,RED,(rect_min_x,rect_min_y,rect_max_x-rect_max_y,rect_max_y-rect_min_y),3)
            
            if event.type==KEYDOWN:
                if event.unicode=='N':
                    displaysurface.fill(BLACK)

        pygame.display.update()