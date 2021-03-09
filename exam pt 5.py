#importing all necessary libraies for the program
import serial 
from time import sleep
from guizero import App, PushButton, Text, TextBox, Drawing,Box
from threading import Thread

#settingup serial connection to arduino
montr= serial.Serial("/dev/ttyACM0", 9600)
montr.flush()
sleep(3)

#function used to write a string to the arduino that will be used for digital pin8
def Pin8button():
    montr.write(str('Pin8').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    sleep(.2)

#function used to write a string to the arduino that will be used for digital pin9    
def Pin9button():
    montr.write(str('Pin9').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    sleep(.2)
    
#function used to write a string to the arduino that will be used for digital pin10
def Pin10button():
    montr.write(str('Pin10').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    sleep(.2)

#function used to write a string to the arduino that will be used for digital pin11
def Pin11button():
    montr.write(str('Pin11').encode('utf-8'))
    montr.write(str("\n").encode('utf-8'))
    montr.flush()
    sleep(.2)
    
#function used to close the app/gui window
def quit_window():
    app.destroy()
    
#function thread containg the bulk of the code needed for the arduino. Reads data from the arduino and is used to determined things happening within the GUI, such as ovals for the simulated lights
def IOthread():
    while True:
        montr.flush()
        ArdReader=montr.readline().decode('utf-8')
        Ardstring=ArdReader.split(',')
        
        AI0=float(Ardstring[0])
        AI1=float(Ardstring[1])
        AI2=float(Ardstring[2])
        AI3=float(Ardstring[3])
        
        A0text.value=AI0
        A1text.value=AI1
        A2text.value=AI2
        A3text.value=AI3
        
        DI0=float(Ardstring[4])
        DI1=float(Ardstring[5])
        DI2=float(Ardstring[6])
        DI3=float(Ardstring[7])
        
        if DI0 ==1:
            light0.oval(5,25,25,45,color="red",outline=True)
        else:
            light0.clear()
        if DI1 ==1:
            light1.oval(5,25,25,45,color="red",outline=True)
        else:
            light1.clear()
        if DI2 ==1:
            light2.oval(5,25,25,45,color="red",outline=True)
        else:
            light2.clear()
        if DI3 ==1:
            light3.oval(5,25,25,45,color="red",outline=True)
        else:
            light3.clear()
            

#block of code sttingup basic components of the GUI, sectioning things into boxes and creating things like the exit button and titles
app=App(title="GUI", layout="grid")
text=Text(app,text="IO data aquisition system GUI", grid=[0,0])
exitbutton= PushButton(app, command=quit_window, text="Exit", grid=[3,4])
outputbox=Box(app, layout="grid", grid=[0,1])
AIbox=Box(app, layout="grid", grid=[1,1])
DIbox=Box(app, layout="grid", grid=[0,2], align="left")

#setting up the box that contains the Digital output pushbuttons and their corresponding pins and labels
DOtitle=Text(outputbox, text="output", grid=[0,0])
pb1=PushButton(outputbox, command=Pin8button,text="pin8", grid=[0,1])
pb2=PushButton(outputbox, command=Pin9button,text="pin9", grid=[0,2])
pb3=PushButton(outputbox, command=Pin10button,text="pin10", grid=[1,1])
pb4=PushButton(outputbox, command=Pin11button,text="pin11", grid=[1,2])

#setting up the Analog input box that contains the pot values in textboxes as well as all asscoicated titles/labels
AItitle=Text(AIbox,text="input analog", grid=[0,0])
antitle0=Text(AIbox, text="A0", grid= [0,1])
antitle1=Text(AIbox, text="A1", grid= [0,2])
antitle2=Text(AIbox, text="A2", grid= [0,3])
antitle3=Text(AIbox, text="A3", grid= [0,4])
A0text=TextBox(AIbox, grid= [1,1])
A1text=TextBox(AIbox, grid= [1,2])
A2text=TextBox(AIbox, grid= [1,3])
A3text=TextBox(AIbox, grid= [1,4])

#setting up the box that contains the digital inputs that are connected to physical buttons. uses simulated lights from the draw module 
DItitle=Text(DIbox, text="input digital", grid=[0,0])
light0= Drawing(DIbox,grid=[0,1])
light1= Drawing(DIbox,grid=[1,1])
light2= Drawing(DIbox,grid=[2,1])
light3= Drawing(DIbox,grid=[3,1])
light0title=Text(DIbox,grid=[0,2])
light1title=Text(DIbox,grid=[1,2])
light2title=Text(DIbox,grid=[2,2])
light3title=Text(DIbox,grid=[3,2])

#function call and code to start the thread function and have it run at the same time the as display code
thread=Thread(target=IOthread)
thread.start()

#displays the app window used by GUI
app.display()