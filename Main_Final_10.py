from random import randint
from tkinter import *
import tkinter.font as font
import Red
import Blue
import Yellow
import Green
import Redroll
import winsound
from winsound import *
import pygame
import time
import math

root = Tk()
root.title("Ludo")
root.geometry('450x650')
frame1 = LabelFrame(root, height=300, width=500, bd=1)
frame2 = LabelFrame(root, height=100, width=500, bd=1)
frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)

def roll( minimum=1, maximum=6):
    """ Rolling of Dice"""
    global x
    x = 0
    x = randint(minimum, maximum)
    #time.sleep(1)
    print( x)

def roll_cancel(minimum=1, maximum=6):
    """ Rolling of Dice"""
    global x,y,z
    x = y = z = 0
    return x, y, z

rr1 = Redroll.Redroll()
def leftclick_redroll(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("DiceRoll.mp3")
    pygame.mixer.music.play()
    root.after(500, roll())
    #roll()
    label1 = Label(root,text=str(x),relief = RAISED,padx=20,pady=20,fg='red',bd=10)
    label1.config(font=("Courier",60))
    label1.grid(row=0,column=0)



button_redroll = Button(frame2, text='ROLL',height=2,width=6,bd=10,activebackground='red',activeforeground='red',bg='red',fg='black',relief=RAISED)
button_redroll['font']=font.Font(size=15)
button_redroll.grid(row=1, column=0)
button_redroll.bind("<Button-1>", leftclick_redroll)

def board():
    global canvas
    canvas = Canvas(frame1,bg="black",height=600,width=1300,cursor='dot')
    for i in range(15):
        for j in range(15):
            x1 = 40*i
            y1= 40*j
            x2=40*(i+1)
            y2=40*(j+1)
            goti_place_offset = 15 
            
            if (i) in (0,1,2,3,4,5):
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline='white')
            if (i) in (0,1,2,3,4,5):
                if j == 0:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red',outline='red')
            if (i) in (0,1,2,3,4,5):
                if j == 5:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red',outline='red')
            if (i) ==0:
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red',outline='red')
            if (i) ==5:
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red',outline='red')                
            if (i) ==2:
                if j == 2:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==4:
                if j == 2:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==2:
                if j == 4:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==4:
                if j ==4:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')

                    
                    
            if (i) in (9,10,11,12,13,14):
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline='white')
            if (i) in (9,10,11,12,13,14):
                if j == 0:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green',outline='green')
            if (i) in (9,10,11,12,13,14):
                if j == 5:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green',outline='green')
            if (i) ==9:
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green',outline='green')
            if (i) ==14:
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green',outline='green')
            if (i) ==11:
                if j == 2:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==13:
                if j == 2:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==11:
                if j == 4:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==13:
                if j ==4:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')



                    
                    
            if (i) in (9,10,11,12,13,14):
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline='white')
            if (i) in (9,10,11,12,13,14):
                if j == 9:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow',outline='yellow')
            if (i) in (9,10,11,12,13,14):
                if j == 14:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow',outline='yellow')
            if (i) ==9:
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow',outline='yellow')
            if (i) ==14:
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow',outline='yellow')
            if (i) ==11:
                if j == 11:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==13:
                if j == 11:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==11:
                if j == 13:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==13:
                if j ==13:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')


                   
            if (i) in (0,1,2,3,4,5):
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline='white')
            if (i) in (0,1,2,3,4,5):
                if j == 9:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue',outline='blue')
            if (i) in (0,1,2,3,4,5):
                if j == 14:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue',outline='blue')
            if (i) ==0:
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue',outline='blue')
            if (i) ==5:
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue',outline='blue')
            if (i) ==2:
                if j == 11:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==4:
                if j == 11:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==4:
                if j == 13:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')
            if (i) ==2:
                if j ==13:
                    canvas.create_oval(x1-goti_place_offset,y1-goti_place_offset,x2-goti_place_offset,y2-goti_place_offset,fill='white',outline='white')




                    
##            if i in (6,7,8):
##                if j in (6,7,8):
##                    canvas.create_rectangle(x1,y1,x2,y2,fill='magenta',outline="black")
            #Home
            canvas.create_polygon(240,360,300,300,360,360,fill='blue',outline="black")
            canvas.create_polygon(360,360,300,300,360,240,fill='yellow',outline="black")
            canvas.create_polygon(360,240,300,300,240,240,fill='green',outline="black")
            canvas.create_polygon(240,240,300,300,240,360,fill='red',outline="black")

            #Arrow
            canvas.create_line(300,570,300,590,fill='blue')
            canvas.create_line(300,570,290,580,fill='blue',width=1)
            canvas.create_line(300,570,310,580,fill='blue',width=1)
            
            canvas.create_line(570,300,590,300,fill='yellow')
            canvas.create_line(570,300,580,290,fill='yellow',width=1)
            canvas.create_line(570,300,580,310,fill='yellow',width=1)
            
            canvas.create_line(300,10,300,30,fill='green',width=1)
            canvas.create_line(300,30,290,20,fill='green',width=1)
            canvas.create_line(300,30,310,20,fill='green',width=1)
            
            canvas.create_line(10,300,30,300,fill='red',width=1)
            canvas.create_line(30,300,20,290,fill='red',width=1)
            canvas.create_line(30,300,20,310,fill='red',width=1)

            #Star
            #canvas.create_polygon(100,330,85,350,115,350,fill='red',outline="black")
            #canvas.create_polygon(100,350,85,330,115,330,fill='red',outline="black")

            x = 100
            y = 340
            r = 20
            points=[
                x-int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x+int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x-int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5)),
                x,
                y-r,
                x+int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5))
                ]
            canvas.create_polygon(points,fill='white',outline="black")
            

            x = 260
            y = 100
            r = 20
            points=[
                x-int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x+int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x-int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5)),
                x,
                y-r,
                x+int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5))
                ]
            canvas.create_polygon(points,fill='white',outline="black")

            x = 500
            y = 260
            r = 20
            points=[
                x-int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x+int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x-int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5)),
                x,
                y-r,
                x+int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5))
                ]
            canvas.create_polygon(points,fill='white',outline="black")

            x = 340
            y = 500
            r = 20
            points=[
                x-int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x+int(r*math.sin(2*math.pi/5)),
                y-int(r*math.cos(2*math.pi/5)),
                x-int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5)),
                x,
                y-r,
                x+int(r*math.sin(math.pi/5)),
                y+int(r*math.cos(math.pi/5))
                ]
            canvas.create_polygon(points,fill='white',outline="black")

                    
            if i in (0,1,2,3,4,5):
                if j in (6,7,8):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white')
            if i in (1,2,3,4,5):
                if j == 7:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red')
            if i == 1:
                if j == 6:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='red')


            if i in (9,10,11,12,13,14):
                if j in (6,7,8):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white')
            if i in (9,10,11,12,13):
                if j ==7:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow')
            if i == 13:
                if j ==8:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='yellow')


            if i in (6,7,8):
                if j in (9,10,11,12,13,14):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white')
            if i == 7:
                if j in (9,10,11,12,13):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue')
            if i == 6:
                if j ==13:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='blue')


            if i in (6,7,8):
                if j in (0,1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white')
            if i ==7:
                if j in (1,2,3,4,5):
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green')
            if i ==8:
                if j == 1:
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green')
                    
##            if i == 2:
##                if j == 8:
##                    canvas.create_rectangle([(x1+10,y1+10),(x2-10,y2-10)])
##            if i == 6:
##                if j == 2:
##                    canvas.create_rectangle([(x1+10,y1+10),(x2-10,y2-10)])
##            if i == 12:
##                if j == 6:
##                    canvas.create_rectangle([(x1+10,y1+10),(x2-10,y2-10)])
##            if i == 8:
##                if j == 12:
##                    canvas.create_rectangle([(x1+10,y1+10),(x2-10,y2-10)])
    canvas.grid(row=100,columnspan=500)    


board()

goti_size=20
goti_position = 10
red_1_x = 65
red_1_y = 85
red_1 = canvas.create_polygon(red_1_x, red_1_y, red_1_x-goti_size, red_1_y-goti_size, red_1_x+goti_size, red_1_y-goti_size,fill='red',outline="black",width=2)
red_2_x = 65+80
red_2_y = 85
red_2 = canvas.create_polygon(red_2_x, red_2_y, red_2_x+goti_size, red_2_y-goti_size, red_2_x+goti_size, red_2_y+goti_size,fill='red',outline="black",width=2)
red_3_x = 65
red_3_y = 85+80
red_3 = canvas.create_polygon(red_3_x,red_3_y,red_3_x+goti_size, red_3_y-goti_size, red_3_x+goti_size, red_3_y+goti_size,fill='red',outline="black",width=2)
red_4_x = 65+80
red_4_y = 85+80
red_4 = canvas.create_polygon(red_4_x,red_4_y,red_4_x+goti_size, red_4_y-goti_size, red_4_x+goti_size, red_4_y+goti_size,fill='red',outline="black",width=2)
green_1_x = 420
green_1_y = 85
green_1 = canvas.create_polygon(green_1_x,green_1_y,green_1_x+goti_size, green_1_y-goti_size, green_1_x+goti_size, green_1_y+goti_size,fill='green',outline="black",width=2)
green_2_x = 420+80
green_2_y = 85
green_2 = canvas.create_polygon(green_2_x,green_2_y,green_2_x+goti_size, green_2_y-goti_size, green_2_x+goti_size, green_2_y+goti_size,fill='green',outline="black",width=2)
green_3_x = 420
green_3_y = 85+80
green_3 = canvas.create_polygon(green_3_x,green_3_y,green_3_x+goti_size, green_3_y-goti_size, green_3_x+goti_size, green_3_y+goti_size,fill='green',outline="black",width=2)
green_4_x = 420+80
green_4_y = 85+80
green_4 = canvas.create_polygon(green_4_x,green_4_y,green_4_x+goti_size, green_4_y-goti_size, green_4_x+goti_size, green_4_y+goti_size,fill='green',outline="black",width=2)
yellow_1_x = 420
yellow_1_y = 445
yellow_1 = canvas.create_polygon(yellow_1_x,yellow_1_y,yellow_1_x+goti_size, yellow_1_y-goti_size, yellow_1_x+goti_size, yellow_1_y+goti_size,fill='yellow',outline="black",width=2)
yellow_2_x = 420+80
yellow_2_y = 445
yellow_2 = canvas.create_polygon(yellow_2_x,yellow_2_y,yellow_2_x+goti_size, yellow_2_y-goti_size, yellow_2_x+goti_size, yellow_2_y+goti_size,fill='yellow',outline="black",width=2)
yellow_3_x = 420
yellow_3_y = 445+80
yellow_3 = canvas.create_polygon(yellow_3_x,yellow_3_y,yellow_3_x+goti_size, yellow_3_y-goti_size, yellow_3_x+goti_size, yellow_3_y+goti_size,fill='yellow',outline="black",width=2)
yellow_4_x = 420+80
yellow_4_y = 445+80
yellow_4 = canvas.create_polygon(yellow_4_x,yellow_4_y,yellow_4_x+goti_size, yellow_4_y-goti_size, yellow_4_x+goti_size, yellow_4_y+goti_size,fill='yellow',outline="black",width=2)
blue_1_x = 60
blue_1_y = 445
blue_1 = canvas.create_polygon(blue_1_x,blue_1_y,blue_1_x+goti_size, blue_1_y-goti_size, blue_1_x+goti_size, blue_1_y+goti_size,fill='blue',outline="black",width=2)
blue_2_x = 60+80
blue_2_y = 445
blue_2 = canvas.create_polygon(blue_2_x,blue_2_y,blue_2_x+goti_size, blue_2_y-goti_size, blue_2_x+goti_size, blue_2_y+goti_size,fill='blue',outline="black",width=2)
blue_3_x = 60
blue_3_y = 445+80
blue_3 = canvas.create_polygon(blue_3_x,blue_3_y,blue_3_x+goti_size, blue_3_y-goti_size, blue_3_x+goti_size, blue_3_y+goti_size,fill='blue',outline="black",width=2)
blue_4_x = 60+80
blue_4_y = 445+80
blue_4 = canvas.create_polygon(blue_4_x,blue_4_y,blue_4_x+goti_size, blue_4_y-goti_size, blue_4_x+goti_size, blue_4_y+goti_size,fill='blue',outline="black",width=2)


r1 = Red.Red()
r2 = Red.Red()
r3 = Red.Red()
r4 = Red.Red()
b1 = Blue.Blue()
b2 = Blue.Blue()
b3 = Blue.Blue()
b4 = Blue.Blue()
b1 = Yellow.Yellow()
b2 = Yellow.Yellow()
b3 = Yellow.Yellow()
b4 = Yellow.Yellow()
b1 = Green.Green()
b2 = Green.Green()
b3 = Green.Green()
b4 = Green.Green()


def redkill_1():
    if r1.position>=1 and r1.position<=12 and r1.position !=8:
        if r1.position == g1.position-39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r1.position == g2.position-39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r1.position == g3.position-39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r1.position == g4.position-39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r1.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r1.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r1.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r1.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r1.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r1.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r1.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r1.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r1.position>=14 and r1.position<=25 and r1.position !=21:
        if r1.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r1.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r1.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r1.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r1.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r1.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r1.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r1.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r1.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r1.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r1.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r1.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

    if r1.position>=27 and r1.position<=38 and r1.position !=34:
        if r1.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r1.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r1.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r1.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r1.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r1.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r1.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r1.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r1.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r1.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r1.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r1.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r1.position>=40 and r1.position<=50 and r1.position !=47:
        if r1.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r1.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r1.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r1.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r1.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r1.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r1.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r1.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r1.position == b1.position+39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r1.position == b2.position+39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r1.position == b3.position+39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r1.position == b4.position+39:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()



def redkill_2():
    if r2.position>=1 and r2.position<=12 and r2.position !=8:
        if r2.position == g1.position-39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r2.position == g2.position-39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r2.position == g3.position-39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r2.position == g4.position-39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r2.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r2.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r2.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r2.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r2.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r2.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r2.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3._init__()
        if r2.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r2.position>=14 and r2.position<=25 and r2.position !=21:
        if r2.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r2.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r2.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r2.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r2.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r2.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r2.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r2.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r2.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r2.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r2.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r2.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

    if r2.position>=27 and r2.position<=38 and r2.position !=34:
        if r2.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r2.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r2.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r2.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r2.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r2.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r2.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r2.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r2.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r2.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r2.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r2.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r2.position>=40 and r2.position<=50 and r2.position !=47:
        if r2.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r2.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r2.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r2.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r2.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r2.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r2.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r2.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r2.position == b1.position+39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r2.position == b2.position+39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r2.position == b3.position+39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r2.position == b4.position+39:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

def redkill_3():
    if r3.position>=1 and r3.position<=12 and r3.position !=8:
        if r3.position == g1.position-39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r3.position == g2.position-39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r3.position == g3.position-39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r3.position == g4.position-39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r3.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r3.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r3.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r3.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r3.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r3.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r3.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r3.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r3.position>=14 and r3.position<=25 and r3.position !=21:
        if r3.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r3.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r3.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r3.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r3.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r3.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r3.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r3.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r3.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r3.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r3.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r3.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

    if r3.position>=27 and r3.position<=38 and r3.position !=34:
        if r3.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r3.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r3.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r3.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r3.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r3.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r3.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r3.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r3.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r3.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r3.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r3.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r3.position>=40 and r3.position<=50 and r3.position !=47:
        if r3.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r3.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r3.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r3.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r3.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r3.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r3.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r3.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r3.position == b1.position+39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r3.position == b2.position+39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r3.position == b3.position+39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r3.position == b4.position+39:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

def redkill_4():
    if r4.position>=1 and r4.position<=12 and r4.position !=8:
        if r4.position == g1.position-39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r4.position == g2.position-39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r4.position == g3.position-39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r4.position == g4.position-39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r4.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r4.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r4.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r4.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r4.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r4.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r4.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r4.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r4.position>=14 and r4.position<=25 and r4.position !=21:
        if r4.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r4.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r4.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r4.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r4.position == y1.position-26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r4.position == y2.position-26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r4.position == y3.position-26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r4.position == y4.position-26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r4.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r4.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r4.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r4.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()

    if r4.position>=27 and r4.position<=38 and r4.position !=34:
        if r4.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r4.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r4.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r4.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r4.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r4.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r4.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r4.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r4.position == b1.position-13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r4.position == b2.position-13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r4.position == b3.position-13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r4.position == b4.position-13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()


    if r4.position>=40 and r4.position<=50 and r4.position !=47:
        if r4.position == g1.position+13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if r4.position == g2.position+13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if r4.position == g3.position+13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if r4.position == g4.position+13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if r4.position == y1.position+26:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if r4.position == y2.position+26:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if r4.position == y3.position+26:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if r4.position == y4.position+26:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if r4.position == b1.position+39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if r4.position == b2.position+39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if r4.position == b3.position+39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if r4.position == b4.position+39:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()




def bluekill_1():
    if b1.position>=1 and b1.position<=12 and b1.position !=8:
        if b1.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b1.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b1.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b1.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b1.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b1.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b1.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b1.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b1.position == r1.position-39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b1.position == r2.position-39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b1.position == r3.position-39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b1.position == r4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b1.position>=14 and b1.position<=25 and b1.position !=21:
        if b1.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b1.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b1.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b1.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b1.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b1.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b1.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b1.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b1.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b1.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b1.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b1.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if b1.position>=27 and b1.position<=38 and b1.position !=34:
        if b1.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b1.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b1.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b1.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b1.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b1.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b1.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b1.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b1.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b1.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b1.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b1.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b1.position>=40 and b1.position<=50 and b1.position !=47:
        if b1.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b1.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b1.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b1.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b1.position == y1.position+39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b1.position == y2.position+39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2+20)
            y2.__init__()
        if b1.position == y3.position+39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b1.position == y4.position+39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b1.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b1.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2+20)
            r2.__init__()
        if b1.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b1.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def bluekill_2():
    if b2.position>=1 and b2.position<=12 and b2.position !=8:
        if b2.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b2.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b2.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b2.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b2.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b2.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b2.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b2.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b2.position == r1.position-39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b2.position == r2.position-39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b2.position == r3.position-39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b2.position == r4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b2.position>=14 and b2.position<=25 and b2.position !=21:
        if b2.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b2.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b2.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b2.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b2.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b2.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b2.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b2.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b2.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b2.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b2.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b2.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if b2.position>=27 and b2.position<=38 and b2.position !=34:
        if b2.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b2.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b2.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b2.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b2.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b2.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b2.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b2.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b2.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b2.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b2.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b2.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b2.position>=40 and b2.position<=50 and b2.position !=47:
        if b2.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b2.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b2.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b2.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b2.position == y1.position+39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b2.position == y2.position+39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2+20)
            y2.__init__()
        if b2.position == y3.position+39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b2.position == y4.position+39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b2.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b2.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2+20)
            r2.__init__()
        if b2.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b2.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def bluekill_3():
    if b3.position>=1 and b3.position<=12 and b3.position !=8:
        if b3.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b3.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b3.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b3.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b3.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b3.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b3.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b3.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b3.position == r1.position-39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b3.position == r2.position-39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b3.position == r3.position-39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b3.position == r4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b3.position>=14 and b3.position<=25 and b3.position !=21:
        if b3.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b3.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b3.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b3.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b3.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b3.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b3.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b3.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b3.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b3.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b3.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b3.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if b3.position>=27 and b3.position<=38 and b3.position !=34:
        if b3.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b3.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b3.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b3.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b3.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b3.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b3.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b3.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b3.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b3.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b3.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b3.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b3.position>=40 and b3.position<=50 and b3.position !=47:
        if b3.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b3.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b3.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b3.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b3.position == y1.position+39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b3.position == y2.position+39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2+20)
            y2.__init__()
        if b3.position == y3.position+39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b3.position == y4.position+39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b3.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b3.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2+20)
            r2.__init__()
        if b3.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b3.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def bluekill_4():
    if b4.position>=1 and b4.position<=12 and b4.position !=8:
        if b4.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b4.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b4.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b4.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b4.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b4.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b4.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b4.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b4.position == r1.position-39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b4.position == r2.position-39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b4.position == r3.position-39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b4.position == r4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b4.position>=14 and b4.position<=25 and b4.position !=21:
        if b4.position == g1.position-26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b4.position == g2.position-26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b4.position == g3.position-26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b4.position == g4.position-26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b4.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b4.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b4.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b4.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b4.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b4.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b4.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b4.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if b4.position>=27 and b4.position<=38 and b4.position !=34:
        if b4.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b4.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b4.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b4.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b4.position == y1.position-13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b4.position == y2.position-13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if b4.position == y3.position-13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b4.position == y4.position-13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b4.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b4.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if b4.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b4.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if b4.position>=40 and b4.position<=50 and b4.position !=47:
        if b4.position == g1.position+26:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if b4.position == g2.position+26:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if b4.position == g3.position+26:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if b4.position == g4.position+26:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if b4.position == y1.position+39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if b4.position == y2.position+39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2+20)
            y2.__init__()
        if b4.position == y3.position+39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if b4.position == y4.position+39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if b4.position == r1.position+13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if b4.position == r2.position+13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2+20)
            r2.__init__()
        if b4.position == r3.position+13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if b4.position == r4.position+13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()








def yellowkill_1():
    if y1.position>=1 and y1.position<=12 and y1.position !=8:
        if y1.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y1.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y1.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y1.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y1.position == b1.position-39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y1.position == b2.position-39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y1.position == b3.position-39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y1.position == b4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            b4.__init__()
        if y1.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y1.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y1.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y1.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y1.position>=14 and y1.position<=25 and y1.position !=21:
        if y1.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y1.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y1.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y1.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y1.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y1.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y1.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y1.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y1.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y1.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y1.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y1.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if y1.position>=27 and y1.position<=38 and y1.position !=34:
        if y1.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y1.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y1.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y1.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y1.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y1.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y1.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y1.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y1.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y1.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y1.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y1.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y1.position>=40 and y1.position<=50 and y1.position !=47:
        if y1.position == g1.position+39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y1.position == g2.position+39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y1.position == g3.position+39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y1.position == g4.position+39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y1.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y1.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y1.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y1.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y1.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y1.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y1.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y1.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def yellowkill_2():
    if y2.position>=1 and y2.position<=12 and y2.position !=8:
        if y2.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y2.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y2.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y2.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y2.position == b1.position-39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y2.position == b2.position-39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y2.position == b3.position-39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y2.position == b4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            b4.__init__()
        if y2.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y2.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y2.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y2.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y2.position>=14 and y2.position<=25 and y2.position !=21:
        if y2.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y2.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y2.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y2.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y2.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y2.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y2.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y2.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y2.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y2.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y2.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y2.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if y2.position>=27 and y2.position<=38 and y2.position !=34:
        if y2.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y2.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y2.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y2.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y2.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y2.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y2.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y2.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y2.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y2.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y2.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y2.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y2.position>=40 and y2.position<=50 and y2.position !=47:
        if y2.position == g1.position+39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y2.position == g2.position+39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y2.position == g3.position+39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y2.position == g4.position+39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y2.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y2.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y2.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y2.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y2.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y2.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y2.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y2.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def yellowkill_3():
    if y3.position>=1 and y3.position<=12 and y3.position !=8:
        if y3.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y3.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y3.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y3.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y3.position == b1.position-39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y3.position == b2.position-39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y3.position == b3.position-39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y3.position == b4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            b4.__init__()
        if y3.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y3.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y3.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y3.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y3.position>=14 and y3.position<=25 and y3.position !=21:
        if y3.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y3.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y3.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y3.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y3.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y3.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y3.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y3.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y3.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y3.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y3.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y3.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if y3.position>=27 and y3.position<=38 and y3.position !=34:
        if y3.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y3.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y3.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y3.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y3.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y3.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y3.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y3.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y3.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y3.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y3.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y3.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y3.position>=40 and y3.position<=50 and y3.position !=47:
        if y3.position == g1.position+39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y3.position == g2.position+39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y3.position == g3.position+39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y3.position == g4.position+39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y3.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y3.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y3.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y3.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y3.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y3.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y3.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y3.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def yellowkill_4():
    if y4.position>=1 and y4.position<=12 and y4.position !=8:
        if y4.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y4.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y4.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y4.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y4.position == b1.position-39:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y4.position == b2.position-39:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y4.position == b3.position-39:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y4.position == b4.position-39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            b4.__init__()
        if y4.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y4.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y4.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y4.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y4.position>=14 and y4.position<=25 and y4.position !=21:
        if y4.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y4.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y4.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y4.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y4.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y4.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y4.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y4.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y4.position == r1.position-26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y4.position == r2.position-26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y4.position == r3.position-26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y4.position == r4.position-26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if y4.position>=27 and y4.position<=38 and y4.position !=34:
        if y4.position == g1.position-13:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y4.position == g2.position-13:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y4.position == g3.position-13:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y4.position == g4.position-13:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y4.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y4.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y4.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y4.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y4.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y4.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y4.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y4.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if y4.position>=40 and y4.position<=50 and y4.position !=47:
        if y4.position == g1.position+39:
            canvas.coords(green_1,green_1_x,green_1_y,green_1_x+20,green_1_y-20,green_1_x+20,green_1_y+20)
            g1.__init__()
        if y4.position == g2.position+39:
            canvas.coords(green_2,green_2_x,green_2_y,green_2_x+20,green_2_y-20,green_2_x+20,green_2_y+20)
            g2.__init__()
        if y4.position == g3.position+39:
            canvas.coords(green_3,green_3_x,green_3_y,green_3_x+20,green_3_y-20,green_3_x+20,green_3_y+20)
            g3.__init__()
        if y4.position == g4.position+39:
            canvas.coords(green_4,green_4_x,green_4_y,green_4_x+20,green_4_y-20,green_4_x+20,green_4_y+20)
            g4.__init__()
        if y4.position == b1.position+13:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if y4.position == b2.position+13:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if y4.position == b3.position+13:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if y4.position == b4.position+13:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if y4.position == r1.position+26:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if y4.position == r2.position+26:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if y4.position == r3.position+26:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if y4.position == r4.position+26:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()






def greenkill_1():
    if g1.position>=1 and g1.position<=12 and g1.position !=8:
        if g1.position == y1.position-39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y4.__init__()
        if g1.position == y2.position-39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g1.position == y3.position-39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g1.position == y4.position-39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g1.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g1.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g1.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g1.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g1.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g1.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g1.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g1.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g1.position>=14 and g1.position<=25 and g1.position !=21:
        if g1.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g1.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g1.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g1.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g1.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g1.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g1.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g1.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g1.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g1.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g1.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g1.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if g1.position>=27 and g1.position<=38 and g1.position !=34:
        if g1.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g1.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g1.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g1.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g1.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g1.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g1.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g1.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g1.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g1.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g1.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g1.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g1.position>=40 and g1.position<=50 and g1.position !=47:
        if g1.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g1.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g1.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g1.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g1.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g1.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g1.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g1.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g1.position == r1.position+39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g1.position == r2.position+39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g1.position == r3.position+39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g1.position == r4.position+39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def greenkill_2():
    if g2.position>=1 and g2.position<=12 and g2.position !=8:
        if g2.position == y1.position-39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y4.__init__()
        if g2.position == y2.position-39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g2.position == y3.position-39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g2.position == y4.position-39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g2.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g2.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g2.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g2.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g2.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g2.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g2.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g2.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g2.position>=14 and g2.position<=25 and g2.position !=21:
        if g2.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g2.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g2.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g2.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g2.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g2.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g2.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g2.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g2.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g2.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g2.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g2.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if g2.position>=27 and g2.position<=38 and g2.position !=34:
        if g2.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g2.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g2.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g2.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g2.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g2.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g2.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g2.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g2.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g2.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g2.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g2.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g2.position>=40 and g2.position<=50 and g2.position !=47:
        if g2.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g2.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g2.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g2.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g2.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g2.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g2.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g2.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g2.position == r1.position+39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g2.position == r2.position+39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g2.position == r3.position+39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g2.position == r4.position+39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def greenkill_3():
    if g3.position>=1 and g3.position<=12 and g3.position !=8:
        if g3.position == y1.position-39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y4.__init__()
        if g3.position == y2.position-39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g3.position == y3.position-39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g3.position == y4.position-39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g3.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g3.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g3.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g3.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g3.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g3.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g3.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g3.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g3.position>=14 and g3.position<=25 and g3.position !=21:
        if g3.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g3.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g3.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g3.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g3.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g3.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g3.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g3.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g3.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g3.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g3.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g3.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if g3.position>=27 and g3.position<=38 and g3.position !=34:
        if g3.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g3.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g3.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g3.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g3.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g3.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g3.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g3.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g3.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g3.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g3.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g3.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g3.position>=40 and g3.position<=50 and g3.position !=47:
        if g3.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g3.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g3.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g3.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g3.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g3.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g3.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g3.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g3.position == r1.position+39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g3.position == r2.position+39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g3.position == r3.position+39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g3.position == r4.position+39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


def greenkill_4():
    if g4.position>=1 and g4.position<=12 and g4.position !=8:
        if g4.position == y1.position-39:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y4.__init__()
        if g4.position == y2.position-39:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g4.position == y3.position-39:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g4.position == y4.position-39:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g4.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g4.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g4.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g4.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g4.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g4.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g4.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g4.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g4.position>=14 and g4.position<=25 and g4.position !=21:
        if g4.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g4.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g4.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g4.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g4.position == b1.position-26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g4.position == b2.position-26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g4.position == b3.position-26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g4.position == b4.position-26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g4.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g4.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g4.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g4.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()

    if g4.position>=27 and g4.position<=38 and g4.position !=34:
        if g4.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g4.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g4.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g4.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g4.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g4.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g4.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g4.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g4.position == r1.position-13:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g4.position == r2.position-13:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g4.position == r3.position-13:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g4.position == r4.position-13:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()


    if g4.position>=40 and g4.position<=50 and g4.position !=47:
        if g4.position == y1.position+13:
            canvas.coords(yellow_1,yellow_1_x,yellow_1_y,yellow_1_x+20,yellow_1_y-20,yellow_1_x+20,yellow_1_y+20)
            y1.__init__()
        if g4.position == y2.position+13:
            canvas.coords(yellow_2,yellow_2_x,yellow_2_y,yellow_2_x+20,yellow_2_y-20,yellow_2_x+20,yellow_2_y+20)
            y2.__init__()
        if g4.position == y3.position+13:
            canvas.coords(yellow_3,yellow_3_x,yellow_3_y,yellow_3_x+20,yellow_3_y-20,yellow_3_x+20,yellow_3_y+20)
            y3.__init__()
        if g4.position == y4.position+13:
            canvas.coords(yellow_4,yellow_4_x,yellow_4_y,yellow_4_x+20,yellow_4_y-20,yellow_4_x+20,yellow_4_y+20)
            y4.__init__()
        if g4.position == b1.position+26:
            canvas.coords(blue_1,blue_1_x,blue_1_y,blue_1_x+20,blue_1_y-20,blue_1_x+20,blue_1_y+20)
            b1.__init__()
        if g4.position == b2.position+26:
            canvas.coords(blue_2,blue_2_x,blue_2_y,blue_2_x+20,blue_2_y-20,blue_2_x+20,blue_2_y+20)
            b2.__init__()
        if g4.position == b3.position+26:
            canvas.coords(blue_3,blue_3_x,blue_3_y,blue_3_x+20,blue_3_y-20,blue_3_x+20,blue_3_y+20)
            b3.__init__()
        if g4.position == b4.position+26:
            canvas.coords(blue_4,blue_4_x,blue_4_y,blue_4_x+20,blue_4_y-20,blue_4_x+20,blue_4_y+20)
            b4.__init__()
        if g4.position == r1.position+39:
            canvas.coords(red_1,red_1_x,red_1_y,red_1_x+20,red_1_y-20,red_1_x+20,red_1_y+20)
            r1.__init__()
        if g4.position == r2.position+39:
            canvas.coords(red_2,red_2_x,red_2_y,red_2_x+20,red_2_y-20,red_2_x+20,red_2_y+20)
            r2.__init__()
        if g4.position == r3.position+39:
            canvas.coords(red_3,red_3_x,red_3_y,red_3_x+20,red_3_y-20,red_3_x+20,red_3_y+20)
            r3.__init__()
        if g4.position == r4.position+39:
            canvas.coords(red_4,red_4_x,red_4_y,red_4_x+20,red_4_y-20,red_4_x+20,red_4_y+20)
            r4.__init__()










#--------------------------------------------------------------------------------------------
def red1():
    if r1.open == -1:
        r1.x = x
        if r1.x == 6:
            r1.opening()
            r1.remainder = r1.remainder
            r1.position = 0
            r1.firstmove = True
            r1.path()
            r1.xcord1 = r1.xcord1+goti_position*0
            r1.ycord1 = r1.ycord1+goti_position*1-4
            if r1.position == 0:
                canvas.coords(red_1,r1.xcord1,r1.ycord1,r1.xcord1+goti_size*.25,r1.ycord1-goti_size*.25,r1.xcord1+goti_size*.25,r1.ycord1+goti_size*.25)
            print(r1.x ,r1.position, r1.remainder)
        else:
            roll_cancel()
          
    elif r1.open==0 & r1.firstmove == False:
        if r1.remainder > 0:
            r1.previous_position = r1.position
            r1.x = x          
            r1.move()
            r1.path()
            r1.xcord1 = r1.xcord1+goti_position*0
            r1.ycord1 = r1.ycord1+goti_position*1-4
            if r1.position == 8 or r1.position ==13 or r1.position==21 or r1.position==26 or r1.position==34 or r1.position==39 or r1.position==47 or r1.position==56:
                canvas.coords(red_1,r1.xcord1,r1.ycord1,r1.xcord1+goti_size*.25,r1.ycord1-goti_size*.25,r1.xcord1+goti_size*.25,r1.ycord1+goti_size*.25)
            else:
                canvas.coords(red_1,r1.xcord1,r1.ycord1,r1.xcord1+goti_size,r1.ycord1-goti_size,r1.xcord1+goti_size,r1.ycord1+goti_size)

            redkill_1()
            r1.last_postiveRemainder = r1.remainder
            if r1.remainder==6:
                r1.remainder = r1.remainder -r1.x
            else:
                r1.remainder = r1.remainder - r1.x
            
        elif r1.remainder < 0:
            r1.xcord1 = r1.xcord1+goti_position*0
            r1.ycord1 = r1.ycord1+goti_position*1-4          
            canvas.coords(red_1,r1.xcord1,r1.ycord1,r1.xcord1+goti_size,r1.ycord1-goti_size,r1.xcord1+goti_size,r1.ycord1+goti_size)
            r1.position = r1.previous_position
            r1.remainder = r1.last_postiveRemainder
        elif r1.remainder == 0: 
            print("Home")
        #print(r1.x ,r1.position, r1.remainder)
#---------------------------------------------------------------------------------------------
def red2():
    if r2.open == -1:
        r2.x = x
        if r2.x == 6:
            r2.opening()
            r2.remainder = r2.remainder
            r2.position = 0
            r2.firstmove = True
            r2.path()
            r2.xcord1 = r2.xcord1+goti_position*0
            r2.ycord1 = r2.ycord1+goti_position*2-4
            if r2.position == 0:
                canvas.coords(red_2,r2.xcord1,r2.ycord1,r2.xcord1+goti_size*.25,r2.ycord1-goti_size*.25,r2.xcord1+goti_size*.25,r2.ycord1+goti_size*.25)
            print(r2.x ,r2.position, r2.remainder)
        else:
            roll_cancel()
          
    elif r2.open==0 & r2.firstmove == False:
        if r2.remainder > 0:
            r2.previous_position = r2.position
            r2.x = x          
            r2.move()
            r2.path()
            r2.xcord1 = r2.xcord1+goti_position*0
            r2.ycord1 = r2.ycord1+goti_position*2-4
            if r2.position == 8 or r2.position ==13 or r2.position==21 or r2.position==26 or r2.position==34 or r2.position==39 or r2.position==47 or r2.position==56:
                canvas.coords(red_2,r2.xcord1,r2.ycord1,r2.xcord1+goti_size*.25,r2.ycord1-goti_size*.25,r2.xcord1+goti_size*.25,r2.ycord1+goti_size*.25)
            else:
                canvas.coords(red_2,r2.xcord1,r2.ycord1,r2.xcord1+goti_size,r2.ycord1-goti_size,r2.xcord1+goti_size,r2.ycord1+goti_size)

            redkill_2()
            r2.last_postiveRemainder = r2.remainder
            if r2.remainder==6:
                r2.remainder = r2.remainder -r2.x
            else:
                r2.remainder = r2.remainder - r2.x
            
        elif r2.remainder < 0:
            r2.xcord1 = r2.xcord1+goti_position*0
            r2.ycord1 = r2.ycord1+goti_position*2-4          
            canvas.coords(red_2,r2.xcord1,r2.ycord1,r2.xcord1+goti_size,r2.ycord1-goti_size,r2.xcord1+goti_size,r2.ycord1+goti_size)
            r2.position = r2.previous_position
            r2.remainder = r2.last_postiveRemainder
        elif r2.remainder == 0: 
            print("Home")
        #print(r2.x ,r2.position, r2.remainder)
#----------------------------------------------------------------------------------------------
def red3():
    if r3.open == -1:
        r3.x = x
        if r3.x == 6:
            r3.opening()
            r3.remainder = r3.remainder
            r3.position = 0
            r3.firstmove = True
            r3.path()
            r3.xcord1 = r3.xcord1+goti_position*0
            r3.ycord1 = r3.ycord1+goti_position*3-4
            if r3.position == 0:
                canvas.coords(red_3,r3.xcord1,r3.ycord1,r3.xcord1+goti_size*.25,r3.ycord1-goti_size*.25,r3.xcord1+goti_size*.25,r3.ycord1+goti_size*.25)
            print(r3.x ,r3.position, r3.remainder)
        else:
            roll_cancel()
          
    elif r3.open==0 & r3.firstmove == False:
        if r3.remainder > 0:
            r3.previous_position = r3.position
            r3.x = x          
            r3.move()
            r3.path()
            r3.xcord1 = r3.xcord1+goti_position*0
            r3.ycord1 = r3.ycord1+goti_position*3-4
            if r3.position == 8 or r3.position ==13 or r3.position==21 or r3.position==26 or r3.position==34 or r3.position==39 or r3.position==47 or r3.position==56:
                canvas.coords(red_3,r3.xcord1,r3.ycord1,r3.xcord1+goti_size*.25,r3.ycord1-goti_size*.25,r3.xcord1+goti_size*.25,r3.ycord1+goti_size*.25)
            else:
                canvas.coords(red_3,r3.xcord1,r3.ycord1,r3.xcord1+goti_size,r3.ycord1-goti_size,r3.xcord1+goti_size,r3.ycord1+goti_size)

            redkill_3()
            r3.last_postiveRemainder = r3.remainder
            if r3.remainder==6:
                r3.remainder = r3.remainder -r3.x
            else:
                r3.remainder = r3.remainder - r3.x
            
        elif r3.remainder < 0:
            r3.xcord1 = r3.xcord1+goti_position*0
            r3.ycord1 = r3.ycord1+goti_position*3-4          
            canvas.coords(red_3,r3.xcord1,r3.ycord1,r3.xcord1+goti_size,r3.ycord1-goti_size,r3.xcord1+goti_size,r3.ycord1+goti_size)
            r3.position = r3.previous_position
            r3.remainder = r3.last_postiveRemainder
        elif r3.remainder == 0: 
            print("Home")
        #print(r3.x ,r3.position, r3.remainder)
#----------------------------------------------------------------------------------------------
def red4():
    if r4.open == -1:
        r4.x = x
        if r4.x == 6:
            r4.opening()
            r4.remainder = r4.remainder
            r4.position = 0
            r4.firstmove = True
            r4.path()
            r4.xcord1 = r4.xcord1+goti_position*0
            r4.ycord1 = r4.ycord1+goti_position*4-4
            if r4.position == 0:
                canvas.coords(red_4,r4.xcord1,r4.ycord1,r4.xcord1+goti_size*.25,r4.ycord1-goti_size*.25,r4.xcord1+goti_size*.25,r4.ycord1+goti_size*.25)
            print(r4.x ,r4.position, r4.remainder)
        else:
            roll_cancel()
          
    elif r4.open==0 & r4.firstmove == False:
        if r4.remainder > 0:
            r4.previous_position = r4.position
            r4.x = x          
            r4.move()
            r4.path()
            r4.xcord1 = r4.xcord1+goti_position*0
            r4.ycord1 = r4.ycord1+goti_position*4-4
            if r4.position == 8 or r4.position ==13 or r4.position==21 or r4.position==26 or r4.position==34 or r4.position==39 or r4.position==47 or r4.position==56:
                canvas.coords(red_4,r4.xcord1,r4.ycord1,r4.xcord1+goti_size*.25,r4.ycord1-goti_size*.25,r4.xcord1+goti_size*.25,r4.ycord1+goti_size*.25)
            else:
                canvas.coords(red_4,r4.xcord1,r4.ycord1,r4.xcord1+goti_size,r4.ycord1-goti_size,r4.xcord1+goti_size,r4.ycord1+goti_size)

            redkill_4()
            r4.last_postiveRemainder = r4.remainder
            if r4.remainder==6:
                r4.remainder = r4.remainder -r4.x
            else:
                r4.remainder = r4.remainder - r4.x
            
        elif r4.remainder < 0:
            r4.xcord1 = r4.xcord1+goti_position*0
            r4.ycord1 = r4.ycord1+goti_position*4-4          
            canvas.coords(red_4,r4.xcord1,r4.ycord1,r4.xcord1+goti_size,r4.ycord1-goti_size,r4.xcord1+goti_size,r4.ycord1+goti_size)
            r4.position = r4.previous_position
            r4.remainder = r4.last_postiveRemainder
        elif r4.remainder == 0: 
            print("Home")
        #print(r4.x ,r4.position, r4.remainder)
#--------------------------------------------------------------------------------------------
def blue1():
    if b1.open == -1:
        b1.x = x
        if b1.x == 6:
            b1.opening()
            b1.remainder = b1.remainder
            b1.position = 0
            b1.firstmove = True
            b1.path()
            b1.xcord1 = b1.xcord1+goti_position*1
            b1.ycord1 = b1.ycord1+goti_position*1-4
            if b1.position == 0:
                canvas.coords(blue_1,b1.xcord1,b1.ycord1,b1.xcord1+goti_size*.25,b1.ycord1-goti_size*.25,b1.xcord1+goti_size*.25,b1.ycord1+goti_size*.25)
            print(b1.x ,b1.position, b1.remainder)
        else:
            roll_cancel()
          
    elif b1.open==0 & b1.firstmove == False:
        if b1.remainder > 0:
            b1.previous_position = b1.position
            b1.x = x          
            b1.move()
            b1.path()
            b1.xcord1 = b1.xcord1+goti_position*1
            b1.ycord1 = b1.ycord1+goti_position*1-4
            if b1.position == 8 or b1.position ==13 or b1.position==21 or b1.position==26 or b1.position==34 or b1.position==39 or b1.position==47 or b1.position==56:
                canvas.coords(blue_1,b1.xcord1,b1.ycord1,b1.xcord1+goti_size*.25,b1.ycord1-goti_size*.25,b1.xcord1+goti_size*.25,b1.ycord1+goti_size*.25)
            else:
                canvas.coords(blue_1,b1.xcord1,b1.ycord1,b1.xcord1+goti_size,b1.ycord1-goti_size,b1.xcord1+goti_size,b1.ycord1+goti_size)

            bluekill_1()
            b1.last_postiveRemainder = b1.remainder
            if b1.remainder==6:
                b1.remainder = b1.remainder -b1.x
            else:
                b1.remainder = b1.remainder - b1.x
            
        elif b1.remainder < 0:
            b1.xcord1 = b1.xcord1+goti_position*1
            b1.ycord1 = b1.ycord1+goti_position*1-4          
            canvas.coords(blue_1,b1.xcord1,b1.ycord1,b1.xcord1+goti_size,b1.ycord1-goti_size,b1.xcord1+goti_size,b1.ycord1+goti_size)
            b1.position = b1.previous_position
            b1.remainder = b1.last_postiveRemainder
        elif b1.remainder == 0: 
            print("Home")
        #print(b1.x ,b1.position, b1.remainder)
#---------------------------------------------------------------------------------------------
def blue2():
    if b2.open == -1:
        b2.x = x
        if b2.x == 6:
            b2.opening()
            b2.remainder = b2.remainder
            b2.position = 0
            b2.firstmove = True
            b2.path()
            b2.xcord1 = b2.xcord1+goti_position*1
            b2.ycord1 = b2.ycord1+goti_position*2-4
            if b2.position == 0:
                canvas.coords(blue_2,b2.xcord1,b2.ycord1,b2.xcord1+goti_size*.25,b2.ycord1-goti_size*.25,b2.xcord1+goti_size*.25,b2.ycord1+goti_size*.25)
            print(b2.x ,b2.position, b2.remainder)
        else:
            roll_cancel()
          
    elif b2.open==0 & b2.firstmove == False:
        if b2.remainder > 0:
            b2.previous_position = b2.position
            b2.x = x          
            b2.move()
            b2.path()
            b2.xcord1 = b2.xcord1+goti_position*1
            b2.ycord1 = b2.ycord1+goti_position*2-4
            if b2.position == 8 or b2.position ==13 or b2.position==21 or b2.position==26 or b2.position==34 or b2.position==39 or b2.position==47 or b2.position==56:
                canvas.coords(blue_2,b2.xcord1,b2.ycord1,b2.xcord1+goti_size*.25,b2.ycord1-goti_size*.25,b2.xcord1+goti_size*.25,b2.ycord1+goti_size*.25)
            else:
                canvas.coords(blue_2,b2.xcord1,b2.ycord1,b2.xcord1+goti_size,b2.ycord1-goti_size,b2.xcord1+goti_size,b2.ycord1+goti_size)

            bluekill_2()
            b2.last_postiveRemainder = b2.remainder
            if b2.remainder==6:
                b2.remainder = b2.remainder -b2.x
            else:
                b2.remainder = b2.remainder - b2.x
            
        elif b2.remainder < 0:
            b2.xcord1 = b2.xcord1+goti_position*1
            b2.ycord1 = b2.ycord1+goti_position*2-4          
            canvas.coords(blue_2,b2.xcord1,b2.ycord1,b2.xcord1+goti_size,b2.ycord1-goti_size,b2.xcord1+goti_size,b2.ycord1+goti_size)
            b2.position = b2.previous_position
            b2.remainder = b2.last_postiveRemainder
        elif b2.remainder == 0: 
            print("Home")
        #print(b2.x ,b2.position, b2.remainder)
#----------------------------------------------------------------------------------------------
def blue3():
    if b3.open == -1:
        b3.x = x
        if b3.x == 6:
            b3.opening()
            b3.remainder = b3.remainder
            b3.position = 0
            b3.firstmove = True
            b3.path()
            b3.xcord1 = b3.xcord1+goti_position*1
            b3.ycord1 = b3.ycord1+goti_position*3-4
            if b3.position == 0:
                canvas.coords(blue_3,b3.xcord1,b3.ycord1,b3.xcord1+goti_size*.25,b3.ycord1-goti_size*.25,b3.xcord1+goti_size*.25,b3.ycord1+goti_size*.25)
            print(b3.x ,b3.position, b3.remainder)
        else:
            roll_cancel()
          
    elif b3.open==0 & b3.firstmove == False:
        if b3.remainder > 0:
            b3.previous_position = b3.position
            b3.x = x          
            b3.move()
            b3.path()
            b3.xcord1 = b3.xcord1+goti_position*1
            b3.ycord1 = b3.ycord1+goti_position*3-4
            if b3.position == 8 or b3.position ==13 or b3.position==21 or b3.position==26 or b3.position==34 or b3.position==39 or b3.position==47 or b3.position==56:
                canvas.coords(blue_3,b3.xcord1,b3.ycord1,b3.xcord1+goti_size*.25,b3.ycord1-goti_size*.25,b3.xcord1+goti_size*.25,b3.ycord1+goti_size*.25)
            else:
                canvas.coords(blue_3,b3.xcord1,b3.ycord1,b3.xcord1+goti_size,b3.ycord1-goti_size,b3.xcord1+goti_size,b3.ycord1+goti_size)

            bluekill_3()
            b3.last_postiveRemainder = b3.remainder
            if b3.remainder==6:
                b3.remainder = b3.remainder -b3.x
            else:
                b3.remainder = b3.remainder - b3.x
            
        elif b3.remainder < 0:
            b3.xcord1 = b3.xcord1+goti_position*1
            b3.ycord1 = b3.ycord1+goti_position*3-4          
            canvas.coords(blue_3,b3.xcord1,b3.ycord1,b3.xcord1+goti_size,b3.ycord1-goti_size,b3.xcord1+goti_size,b3.ycord1+goti_size)
            b3.position = b3.previous_position
            b3.remainder = b3.last_postiveRemainder
        elif b3.remainder == 0: 
            print("Home")
        #print(b3.x ,b3.position, b3.remainder)
#----------------------------------------------------------------------------------------------
def blue4():
    if b4.open == -1:
        b4.x = x
        if b4.x == 6:
            b4.opening()
            b4.remainder = b4.remainder
            b4.position = 0
            b4.firstmove = True
            b4.path()
            b4.xcord1 = b4.xcord1+goti_position*1
            b4.ycord1 = b4.ycord1+goti_position*4-4
            if b4.position == 0:
                canvas.coords(blue_4,b4.xcord1,b4.ycord1,b4.xcord1+goti_size*.25,b4.ycord1-goti_size*.25,b4.xcord1+goti_size*.25,b4.ycord1+goti_size*.25)
            print(b4.x ,b4.position, b4.remainder)
        else:
            roll_cancel()
          
    elif b4.open==0 & b4.firstmove == False:
        if b4.remainder > 0:
            b4.previous_position = b4.position
            b4.x = x          
            b4.move()
            b4.path()
            b4.xcord1 = b4.xcord1+goti_position*1
            b4.ycord1 = b4.ycord1+goti_position*4-4
            if b4.position == 8 or b4.position ==13 or b4.position==21 or b4.position==26 or b4.position==34 or b4.position==39 or b4.position==47 or b4.position==56:
                canvas.coords(blue_4,b4.xcord1,b4.ycord1,b4.xcord1+goti_size*.25,b4.ycord1-goti_size*.25,b4.xcord1+goti_size*.25,b4.ycord1+goti_size*.25)
            else:
                canvas.coords(blue_4,b4.xcord1,b4.ycord1,b4.xcord1+goti_size,b4.ycord1-goti_size,b4.xcord1+goti_size,b4.ycord1+goti_size)

            bluekill_4()
            b4.last_postiveRemainder = b4.remainder
            if b4.remainder==6:
                b4.remainder = b4.remainder -b4.x
            else:
                b4.remainder = b4.remainder - b4.x
            
        elif b4.remainder < 0:
            b4.xcord1 = b4.xcord1+goti_position*1
            b4.ycord1 = b4.ycord1+goti_position*4-4         
            canvas.coords(blue_4,b4.xcord1,b4.ycord1,b4.xcord1+goti_size,b4.ycord1-goti_size,b4.xcord1+goti_size,b4.ycord1+goti_size)
            b4.position = b4.previous_position
            b4.remainder = b4.last_postiveRemainder
        elif b4.remainder == 0: 
            print("Home")
#print(b4.x ,b4.position, b4.remainder)
#---------------------------------------------------------------------------------------------

def yellow1():
    if y1.open == -1:
        y1.x = x
        if y1.x == 6:
            y1.opening()
            y1.remainder = y1.remainder
            y1.position = 0
            y1.firstmove = True
            y1.path()
            y1.xcord1 = y1.xcord1+goti_position*2
            y1.ycord1 = y1.ycord1+goti_position*1-4
            if y1.position == 0:
                canvas.coords(yellow_1,y1.xcord1,y1.ycord1,y1.xcord1+goti_size*.25,y1.ycord1-goti_size*.25,y1.xcord1+goti_size*.25,y1.ycord1+goti_size*.25)
            print(y1.x ,y1.position, y1.remainder)
        else:
            roll_cancel()
          
    elif y1.open==0 & y1.firstmove == False:
        if y1.remainder > 0:
            y1.previous_position = y1.position
            y1.x = x          
            y1.move()
            y1.path()
            y1.xcord1 = y1.xcord1+goti_position*2
            y1.ycord1 = y1.ycord1+goti_position*1-4
            if y1.position == 8 or y1.position ==13 or y1.position==21 or y1.position==26 or y1.position==34 or y1.position==39 or y1.position==47 or y1.position==56:
                canvas.coords(yellow_1,y1.xcord1,y1.ycord1,y1.xcord1+goti_size*.25,y1.ycord1-goti_size*.25,y1.xcord1+goti_size*.25,y1.ycord1+goti_size*.25)
            else:
                canvas.coords(yellow_1,y1.xcord1,y1.ycord1,y1.xcord1+goti_size,y1.ycord1-goti_size,y1.xcord1+goti_size,y1.ycord1+goti_size)

            yellowkill_1()
            y1.last_postiveRemainder = y1.remainder
            if y1.remainder==6:
                y1.remainder = y1.remainder -y1.x
            else:
                y1.remainder = y1.remainder - y1.x
            
        elif y1.remainder < 0:
            y1.xcord1 = y1.xcord1+goti_position*2
            y1.ycord1 = y1.ycord1+goti_position*1-4          
            canvas.coords(yellow_1,y1.xcord1,y1.ycord1,y1.xcord1+goti_size,y1.ycord1-goti_size,y1.xcord1+goti_size,y1.ycord1+goti_size)
            y1.position = y1.previous_position
            y1.remainder = y1.last_postiveRemainder
        elif y1.remainder == 0: 
            print("Home")
        #print(y1.x ,y1.position, y1.remainder)
#---------------------------------------------------------------------------------------------
def yellow2():
    if y2.open == -1:
        y2.x = x
        if y2.x == 6:
            y2.opening()
            y2.remainder = y2.remainder
            y2.position = 0
            y2.firstmove = True
            y2.path()
            y2.xcord1 = y2.xcord1+goti_position*2
            y2.ycord1 = y2.ycord1+goti_position*2-4
            if y2.position == 0:
                canvas.coords(yellow_2,y2.xcord1,y2.ycord1,y2.xcord1+goti_size*.25,y2.ycord1-goti_size*.25,y2.xcord1+goti_size*.25,y2.ycord1+goti_size*.25)
            print(y2.x ,y2.position, y2.remainder)
        else:
            roll_cancel()
          
    elif y2.open==0 & y2.firstmove == False:
        if y2.remainder > 0:
            y2.previous_position = y2.position
            y2.x = x          
            y2.move()
            y2.path()
            y2.xcord1 = y2.xcord1+goti_position*2
            y2.ycord1 = y2.ycord1+goti_position*2-4
            if y2.position == 8 or y2.position ==13 or y2.position==21 or y2.position==26 or y2.position==34 or y2.position==39 or y2.position==47 or y2.position==56:
                canvas.coords(yellow_2,y2.xcord1,y2.ycord1,y2.xcord1+goti_size*.25,y2.ycord1-goti_size*.25,y2.xcord1+goti_size*.25,y2.ycord1+goti_size*.25)
            else:
                canvas.coords(yellow_2,y2.xcord1,y2.ycord1,y2.xcord1+goti_size,y2.ycord1-goti_size,y2.xcord1+goti_size,y2.ycord1+goti_size)

            yellowkill_2()
            y2.last_postiveRemainder = y2.remainder
            if y2.remainder==6:
                y2.remainder = y2.remainder -y2.x
            else:
                y2.remainder = y2.remainder - y2.x
            
        elif y2.remainder < 0:
            y2.xcord1 = y2.xcord1+goti_position*2
            y2.ycord1 = y2.ycord1+goti_position*2-4          
            canvas.coords(yellow_2,y2.xcord1,y2.ycord1,y2.xcord1+goti_size,y2.ycord1-goti_size,y2.xcord1+goti_size,y2.ycord1+goti_size)
            y2.position = y2.previous_position
            y2.remainder = y2.last_postiveRemainder
        elif y2.remainder == 0: 
            print("Home")
        #print(y2.x ,y2.position, y2.remainder)
#----------------------------------------------------------------------------------------------
def yellow3():
    if y3.open == -1:
        y3.x = x
        if y3.x == 6:
            y3.opening()
            y3.remainder = y3.remainder
            y3.position = 0
            y3.firstmove = True
            y3.path()
            y3.xcord1 = y3.xcord1+goti_position*2
            y3.ycord1 = y3.ycord1+goti_position*3-4
            if y3.position == 0:
                canvas.coords(yellow_3,y3.xcord1,y3.ycord1,y3.xcord1+goti_size*.25,y3.ycord1-goti_size*.25,y3.xcord1+goti_size*.25,y3.ycord1+goti_size*.25)
            print(y3.x ,y3.position, y3.remainder)
        else:
            roll_cancel()
          
    elif y3.open==0 & y3.firstmove == False:
        if y3.remainder > 0:
            y3.previous_position = y3.position
            y3.x = x          
            y3.move()
            y3.path()
            y3.xcord1 = y3.xcord1+goti_position*2
            y3.ycord1 = y3.ycord1+goti_position*3-4
            if y3.position == 8 or y3.position ==13 or y3.position==21 or y3.position==26 or y3.position==34 or y3.position==39 or y3.position==47 or y3.position==56:
                canvas.coords(yellow_3,y3.xcord1,y3.ycord1,y3.xcord1+goti_size*.25,y3.ycord1-goti_size*.25,y3.xcord1+goti_size*.25,y3.ycord1+goti_size*.25)
            else:
                canvas.coords(yellow_3,y3.xcord1,y3.ycord1,y3.xcord1+goti_size,y3.ycord1-goti_size,y3.xcord1+goti_size,y3.ycord1+goti_size)

            yellowkill_3()
            y3.last_postiveRemainder = y3.remainder
            if y3.remainder==6:
                y3.remainder = y3.remainder -y3.x
            else:
                y3.remainder = y3.remainder - y3.x
            
        elif y3.remainder < 0:
            y3.xcord1 = y3.xcord1+goti_position*2
            y3.ycord1 = y3.ycord1+goti_position*3-4          
            canvas.coords(yellow_3,y3.xcord1,y3.ycord1,y3.xcord1+goti_size,y3.ycord1-goti_size,y3.xcord1+goti_size,y3.ycord1+goti_size)
            y3.position = y3.previous_position
            y3.remainder = y3.last_postiveRemainder
        elif y3.remainder == 0: 
            print("Home")
        #print(y3.x ,y3.position, y3.remainder)
#----------------------------------------------------------------------------------------------
def yellow4():
    if y4.open == -1:
        y4.x = x
        if y4.x == 6:
            y4.opening()
            y4.remainder = y4.remainder
            y4.position = 0
            y4.firstmove = True
            y4.path()
            y4.xcord1 = y4.xcord1+goti_position*2
            y4.ycord1 = y4.ycord1+goti_position*4-4
            if y4.position == 0:
                canvas.coords(yellow_4,y4.xcord1,y4.ycord1,y4.xcord1+goti_size*.25,y4.ycord1-goti_size*.25,y4.xcord1+goti_size*.25,y4.ycord1+goti_size*.25)
            print(y4.x ,y4.position, y4.remainder)
        else:
            roll_cancel()
          
    elif y4.open==0 & y4.firstmove == False:
        if y4.remainder > 0:
            y4.previous_position = y4.position
            y4.x = x          
            y4.move()
            y4.path()
            y4.xcord1 = y4.xcord1+goti_position*2
            y4.ycord1 = y4.ycord1+goti_position*4-4
            if y4.position == 8 or y4.position ==13 or y4.position==21 or y4.position==26 or y4.position==34 or y4.position==39 or y4.position==47 or y4.position==56:
                canvas.coords(yellow_4,y4.xcord1,y4.ycord1,y4.xcord1+goti_size*.25,y4.ycord1-goti_size*.25,y4.xcord1+goti_size*.25,y4.ycord1+goti_size*.25)
            else:
                canvas.coords(yellow_4,y4.xcord1,y4.ycord1,y4.xcord1+goti_size,y4.ycord1-goti_size,y4.xcord1+goti_size,y4.ycord1+goti_size)

            yellowkill_4()
            y4.last_postiveRemainder = y4.remainder
            if y4.remainder==6:
                y4.remainder = y4.remainder -y4.x
            else:
                y4.remainder = y4.remainder - y4.x
            
        elif y4.remainder < 0:
            y4.xcord1 = y4.xcord1+goti_position*2
            y4.ycord1 = y4.ycord1+goti_position*4-4          
            canvas.coords(yellow_4,y4.xcord1,y4.ycord1,y4.xcord1+goti_size,y4.ycord1-goti_size,y4.xcord1+goti_size,y4.ycord1+goti_size)
            y4.position = y4.previous_position
            y4.remainder = y4.last_postiveRemainder
        elif y4.remainder == 0: 
            print("Home")
#print(y4.x ,y4.position, y4.remainder)
#-------------------------------------------------------------------------------------------------------
def green1():
    if g1.open == -1:
        g1.x = x
        if g1.x == 6:
            g1.opening()
            g1.remainder = g1.remainder
            g1.position = 0
            g1.firstmove = True
            g1.path()
            g1.xcord1 = g1.xcord1+goti_position*3
            g1.ycord1 = g1.ycord1+goti_position*1-4
            if g1.position == 0:
                canvas.coords(green_1,g1.xcord1,g1.ycord1,g1.xcord1+goti_size*.25,g1.ycord1-goti_size*.25,g1.xcord1+goti_size*.25,g1.ycord1+goti_size*.25)
            print(g1.x ,g1.position, g1.remainder)
        else:
            roll_cancel()
          
    elif g1.open==0 & g1.firstmove == False:
        if g1.remainder > 0:
            g1.previous_position = g1.position
            g1.x = x          
            g1.move()
            g1.path()
            g1.xcord1 = g1.xcord1+goti_position*3
            g1.ycord1 = g1.ycord1+goti_position*1-4
            if g1.position == 8 or g1.position ==13 or g1.position==21 or g1.position==26 or g1.position==34 or g1.position==39 or g1.position==47 or g1.position==56:
                canvas.coords(green_1,g1.xcord1,g1.ycord1,g1.xcord1+goti_size*.25,g1.ycord1-goti_size*.25,g1.xcord1+goti_size*.25,g1.ycord1+goti_size*.25)
            else:
                canvas.coords(green_1,g1.xcord1,g1.ycord1,g1.xcord1+goti_size,g1.ycord1-goti_size,g1.xcord1+goti_size,g1.ycord1+goti_size)

            greenkill_1()
            g1.last_postiveRemainder = g1.remainder
            if g1.remainder==6:
                g1.remainder = g1.remainder -g1.x
            else:
                g1.remainder = g1.remainder - g1.x
            
        elif g1.remainder < 0:
            g1.xcord1 = g1.xcord1+goti_position*3
            g1.ycord1 = g1.ycord1+goti_position*1-4          
            canvas.coords(green_1,g1.xcord1,g1.ycord1,g1.xcord1+goti_size,g1.ycord1-goti_size,g1.xcord1+goti_size,g1.ycord1+goti_size)
            g1.position = g1.previous_position
            g1.remainder = g1.last_postiveRemainder
        elif g1.remainder == 0: 
            print("Home")
        #print(g1.x ,g1.position, g1.remainder)
#---------------------------------------------------------------------------------------------
def green2():
    if g2.open == -1:
        g2.x = x
        if g2.x == 6:
            g2.opening()
            g2.remainder = g2.remainder
            g2.position = 0
            g2.firstmove = True
            g2.path()
            g2.xcord1 = g2.xcord1+goti_position*3
            g2.ycord1 = g2.ycord1+goti_position*2-4
            if g2.position == 0:
                canvas.coords(green_2,g2.xcord1,g2.ycord1,g2.xcord1+goti_size*.25,g2.ycord1-goti_size*.25,g2.xcord1+goti_size*.25,g2.ycord1+goti_size*.25)
            print(g2.x ,g2.position, g2.remainder)
        else:
            roll_cancel()
          
    elif g2.open==0 & g2.firstmove == False:
        if g2.remainder > 0:
            g2.previous_position = g2.position
            g2.x = x          
            g2.move()
            g2.path()
            g2.xcord1 = g2.xcord1+goti_position*3
            g2.ycord1 = g2.ycord1+goti_position*2-4
            if g2.position == 8 or g2.position ==13 or g2.position==21 or g2.position==26 or g2.position==34 or g2.position==39 or g2.position==47 or g2.position==56:
                canvas.coords(green_2,g2.xcord1,g2.ycord1,g2.xcord1+goti_size*.25,g2.ycord1-goti_size*.25,g2.xcord1+goti_size*.25,g2.ycord1+goti_size*.25)
            else:
                canvas.coords(green_2,g2.xcord1,g2.ycord1,g2.xcord1+goti_size,g2.ycord1-goti_size,g2.xcord1+goti_size,g2.ycord1+goti_size)

            greenkill_2()
            g2.last_postiveRemainder = g2.remainder
            if g2.remainder==6:
                g2.remainder = g2.remainder -g2.x
            else:
                g2.remainder = g2.remainder - g2.x
            
        elif g2.remainder < 0:
            g2.xcord1 = g2.xcord1+goti_position*3
            g2.ycord1 = g2.ycord1+goti_position*2-4          
            canvas.coords(green_2,g2.xcord1,g2.ycord1,g2.xcord1+goti_size,g2.ycord1-goti_size,g2.xcord1+goti_size,g2.ycord1+goti_size)
            g2.position = g2.previous_position
            g2.remainder = g2.last_postiveRemainder
        elif g2.remainder == 0: 
            print("Home")
        #print(g2.x ,g2.position, g2.remainder)
#----------------------------------------------------------------------------------------------
def green3():
    if g3.open == -1:
        g3.x = x
        if g3.x == 6:
            g3.opening()
            g3.remainder = g3.remainder
            g3.position = 0
            g3.firstmove = True
            g3.path()
            g3.xcord1 = g3.xcord1+goti_position*3
            g3.ycord1 = g3.ycord1+goti_position*3-4
            if g3.position == 0:
                canvas.coords(green_3,g3.xcord1,g3.ycord1,g3.xcord1+goti_size*.25,g3.ycord1-goti_size*.25,g3.xcord1+goti_size*.25,g3.ycord1+goti_size*.25)
            print(g3.x ,g3.position, g3.remainder)
        else:
            roll_cancel()
          
    elif g3.open==0 & g3.firstmove == False:
        if g3.remainder > 0:
            g3.previous_position = g3.position
            g3.x = x          
            g3.move()
            g3.path()
            g3.xcord1 = g3.xcord1+goti_position*3
            g3.ycord1 = g3.ycord1+goti_position*3-4
            if g3.position == 8 or g3.position ==13 or g3.position==21 or g3.position==26 or g3.position==34 or g3.position==39 or g3.position==47 or g3.position==56:
                canvas.coords(green_3,g3.xcord1,g3.ycord1,g3.xcord1+goti_size*.25,g3.ycord1-goti_size*.25,g3.xcord1+goti_size*.25,g3.ycord1+goti_size*.25)
            else:
                canvas.coords(green_3,g3.xcord1,g3.ycord1,g3.xcord1+goti_size,g3.ycord1-goti_size,g3.xcord1+goti_size,g3.ycord1+goti_size)

            greenkill_3()
            g3.last_postiveRemainder = g3.remainder
            if g3.remainder==6:
                g3.remainder = g3.remainder -g3.x
            else:
                g3.remainder = g3.remainder - g3.x
            
        elif g3.remainder < 0:
            g3.xcord1 = g3.xcord1+goti_position*3
            g3.ycord1 = g3.ycord1+goti_position*3-4          
            canvas.coords(green_3,g3.xcord1,g3.ycord1,g3.xcord1+goti_size,g3.ycord1-goti_size,g3.xcord1+goti_size,g3.ycord1+goti_size)
            g3.position = g3.previous_position
            g3.remainder = g3.last_postiveRemainder
        elif g3.remainder == 0: 
            print("Home")
        #print(g3.x ,g3.position, g3.remainder)
#----------------------------------------------------------------------------------------------
def green4():
    if g4.open == -1:
        g4.x = x
        if g4.x == 6:
            g4.opening()
            g4.remainder = g4.remainder
            g4.position = 0
            g4.firstmove = True
            g4.path()
            g4.xcord1 = g4.xcord1+goti_position*3
            g4.ycord1 = g4.ycord1+goti_position*4-4
            if g4.position == 0:
                canvas.coords(green_4,g4.xcord1,g4.ycord1,g4.xcord1+goti_size*.25,g4.ycord1-goti_size*.25,g4.xcord1+goti_size*.25,g4.ycord1+goti_size*.25)
            print(g4.x ,g4.position, g4.remainder)
        else:
            roll_cancel()
          
    elif g4.open==0 & g4.firstmove == False:
        if g4.remainder > 0:
            g4.previous_position = g4.position
            g4.x = x          
            g4.move()
            g4.path()
            g4.xcord1 = g4.xcord1+goti_position*3
            g4.ycord1 = g4.ycord1+goti_position*4-4
            if g4.position == 8 or g4.position ==13 or g4.position==21 or g4.position==26 or g4.position==34 or g4.position==39 or g4.position==47 or g4.position==56:
                canvas.coords(green_4,g4.xcord1,g4.ycord1,g4.xcord1+goti_size*.25,g4.ycord1-goti_size*.25,g4.xcord1+goti_size*.25,g4.ycord1+goti_size*.25)
            else:
                canvas.coords(green_4,g4.xcord1,g4.ycord1,g4.xcord1+goti_size,g4.ycord1-goti_size,g4.xcord1+goti_size,g4.ycord1+goti_size)

            greenkill_4()
            g4.last_postiveRemainder = g4.remainder
            if g4.remainder==6:
                g4.remainder = g4.remainder -g4.x
            else:
                g4.remainder = g4.remainder - g4.x
            
        elif g4.remainder < 0:
            g4.xcord1 = g4.xcord1+goti_position*3
            g4.ycord1 = g4.ycord1+goti_position*4-4          
            canvas.coords(green_4,g4.xcord1,g4.ycord1,g4.xcord1+goti_size,g4.ycord1-goti_size,g4.xcord1+goti_size,g4.ycord1+goti_size)
            g4.position = g4.previous_position
            g4.remainder = g4.last_postiveRemainder
        elif g4.remainder == 0: 
            print("Home")
#print(g4.x ,g4.position, g4.remainder)
#----------------------------------------------------------------------------------


            
r1 = Red.Red()
def leftclick_r1(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    red1()
r2 = Red.Red()
def leftclick_r2(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    red2()
b3 = Red.Red()
def leftclick_r3(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()    
    red3()
r4 = Red.Red()
def leftclick_r4(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    red4()
b1 = Blue.Blue()
def leftclick_b1(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    blue1()
b2 = Blue.Blue()
def leftclick_b2(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    blue2()
b3 = Blue.Blue()
def leftclick_b3(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    blue3()
b4 = Blue.Blue()
def leftclick_b4(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    blue4()
y1 = Yellow.Yellow()
def leftclick_y1(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    yellow1()
y2 = Yellow.Yellow()
def leftclick_y2(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    yellow2()
y3 = Yellow.Yellow()
def leftclick_y3(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    yellow3()
y4 = Yellow.Yellow()
def leftclick_y4(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    yellow4()  
g1 = Green.Green()
def leftclick_g1(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    green1()
g2 = Green.Green()
def leftclick_g2(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    green2()
g3 = Green.Green()
def leftclick_g3(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    green3()
g4 = Green.Green()
def leftclick_g4(event):
    pygame.mixer.init()    
    pygame.mixer.music.load("click_sound.mp3")
    pygame.mixer.music.play()
    green4()

canvas.tag_bind(red_1,"<Button-1>", leftclick_r1)
canvas.tag_bind(red_2,"<Button-1>", leftclick_r2)
canvas.tag_bind(red_3,"<Button-1>", leftclick_r3)
canvas.tag_bind(red_4,"<Button-1>", leftclick_r4)
canvas.tag_bind(blue_1,"<Button-1>", leftclick_b1)
canvas.tag_bind(blue_2,"<Button-1>", leftclick_b2)
canvas.tag_bind(blue_3,"<Button-1>", leftclick_b3)
canvas.tag_bind(blue_4,"<Button-1>", leftclick_b4)
canvas.tag_bind(yellow_1,"<Button-1>", leftclick_y1)
canvas.tag_bind(yellow_2,"<Button-1>", leftclick_y2)
canvas.tag_bind(yellow_3,"<Button-1>", leftclick_y3)
canvas.tag_bind(yellow_4,"<Button-1>", leftclick_y4)
canvas.tag_bind(green_1,"<Button-1>", leftclick_g1)
canvas.tag_bind(green_2,"<Button-1>", leftclick_g2)
canvas.tag_bind(green_3,"<Button-1>", leftclick_g3)
canvas.tag_bind(green_4,"<Button-1>", leftclick_g4)



root.mainloop()

















