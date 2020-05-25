import tkinter as tk
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math as m
import psutil
from scipy.io.wavfile import write
from numpy import linspace, sin, pi, int16, cos, tan, float32
import winsound as ws
import numpy as np
import datetime
import os
now = datetime.datetime.now()
# print ("Current date and time : ")
dt = now.strftime("D - %y-%m-%d T - %H-%M-%S")
if os.path.isdir('pictures') == False:
    os.mkdir('pictures')
    os.mkdir('sound samples')
    os.mkdir('Data')


#WINDOW & CANVAS
window = tk.Tk()
window.title('D I G I T A L    O S C I L L O S C O P E')
window.resizable(0,0)
canvas = tk.Canvas(window, height=600, width=800, bg='#1a2024').pack()

#FRAMES
F1=tk.Frame(window,height=446,width=536,bg='#1d2730',relief=SUNKEN).place(x=14,y=35)

F2=tk.Frame(window,height=40,width=215,bg='#1d2730',relief=SUNKEN).place(x=574,y=35)

F3=tk.Frame(window,height=310,width=215,bg='#1d2730',relief=SUNKEN).place(x=574,y=85)

F4=tk.Frame(window,height=105,width=140,bg='#1d2730',relief=SUNKEN).place(x=574,y=405)

#AMPLITUDE
amp = DoubleVar()
a = float()
Amplitude = tk.Scale(canvas, label='Oscilloscope Gain', orient=HORIZONTAL, relief=FLAT, showvalue=1
                , from_=1, to=5, resolution=0.1, bd=0, bg='#283238', fg='white', length=200
                 , activebackground='#708b99', troughcolor='#1a2024', width=12, variable=amp).place(x=580, y=90)


#FREQUENCY
freq=DoubleVar()
f=float()
Frequency=tk.Scale(canvas,label='Frequency Input(Hz)',orient=HORIZONTAL,relief=FLAT,showvalue=1,
                from_=5,to=1000,resolution=5,bd=0,bg='#283238',fg='white',length=200
                ,activebackground='#708b99',troughcolor='#1a2024',width=12,variable=freq).place(x=580,y=170)


#HORIZONTAL OFFSET
hoff=DoubleVar()
ho=float()
HorizontalOffset=tk.Scale(canvas,label='Horizontal Offset(-10 to +10)',orient=HORIZONTAL,relief=FLAT,
                          showvalue=1,from_=-10,to=10,resolution=1,bd=0,bg='#283238',fg='white',length=200
                ,activebackground='#708b99',troughcolor='#1a2024',width=12,variable=hoff).place(x=580,y=250)


#VERTICAL OFFSET
voff=DoubleVar()
vo=float()
VerticalOffset=tk.Scale(canvas,label='Vertical Offset(-10 to +10)',orient=HORIZONTAL,relief=FLAT,
                        showvalue=1,from_=-10,to=10,resolution=1,bd=0,bg='#283238',fg='white',length=200
                ,activebackground='#708b99',troughcolor='#1a2024',width=12,variable=voff).place(x=580,y=330)


#TEXT
Wavetext=tk.Label(canvas,text='D I G I T A L    O S C I L L O S C O P E',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',15,'bold')).place(x=240,y=5)

wavytext=tk.Label(canvas,text='''Click on the 'REFRESH' button to start the grapher.''',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',15,'bold')).place(x=40,y=280)

copyright=tk.Label(canvas,text='copyright ©\nDesigned by j0f!N',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=710,y=5)

#FILE CREATION
count=0
file=open('Data/Digital osciiloscope tablesetvalue.txt','w+')
file.close()

#FUNCTIONS
def ref():
    #print(p.cpu_percent())
    a=amp.get()
    # print('AMPLITUDE  = ', a)
    f=freq.get()
    # print('FREQUENCY  = ', f)
    ho=hoff.get()
    # print('HORI OFF   = ', ho)
    vo=voff.get()
    # print('VERI OFF   = ', vo)
    # print(' ')
    x=list()
    y=list()
    s=float()
    for i in range(1,200,1):
        x.append(i)
        if opt.get()==1:
            s=a*m.sin((2*3.14*f*i)+ho)+vo
            y.append(s)
        elif opt.get()==2:
            s=a*m.sin((2*3.14*f*i)+ho)+vo
            if s<0.0:
                y.append(-1)
            elif s>0.0:
                y.append(1)
            elif s==0.0:
                y.append(0)
            
        elif opt.get()==3:
            s=-(2*a/3.14)*m.atan(1/m.tan(i*3.14*f+ho))+vo
            y.append(s)
        elif opt.get()==4:
            s=(2*a/3.14)*m.asin(m.sin(i*2*3.14*f+ho))+vo
            y.append(s)
        else:
            y.append(0)

    fig=Figure(figsize=(7,5),dpi=75,facecolor='aqua')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=2.5)
    aggg.grid(True,color='black')
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#071770')
    c=FigureCanvasTkAgg(fig,master=window)
    
    #tool=NavigationToolbar2Tk(c,window)
    #stool.update()
    c.get_tk_widget().place(x=20,y=100)
    cpu=tk.Label(canvas,text='CPU : {} %'.format(psutil.cpu_percent()),fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=10,y=10)

    blank1=tk.Label(canvas,text='             ',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=720,y=410)

    blank2=tk.Label(canvas,text='             ',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=720,y=460)
    

    
    window.update_idletasks()
    
def rst():
    amp.set(1.0)
    freq.set(5)
    hoff.set(0)
    voff.set(0)
    opt.set(5)
    fig=Figure(figsize=(7,5),dpi=75,facecolor='aqua')
    aggg=fig.add_subplot(111)
    aggg.plot(0,0,color='#00f7ff',linewidth=2.5)
    aggg.grid(True,color='black')
    aggg.set_facecolor('#071770')
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=100)
    #tool=NavigationToolbar2Tk(c,window)
    #stool.update()

    cpu=tk.Label(canvas,text='CPU : {} %'.format(psutil.cpu_percent()),fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=10,y=10)

    fig=Figure(figsize=(4,2),dpi=50,facecolor='#1a2024')
    aggg=fig.add_subplot(111)
    aggg.plot(0,0,color='#00f7ff',linewidth=6)
    aggg.grid(False)
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#1a2024')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=490)

def sav():
    a=amp.get()
    f=freq.get()
    ho=hoff.get()
    vo=voff.get()
    count=0
    file=open('Data/Digital osciiloscope tablesetvalue.txt','r')
    l=file.read().split()
    count=l.count('TEST')
    file.close()
    s=str()
    file=open('Data/Digital osciiloscope tablesetvalue.txt','a+')
    if opt.get()==1:
        s='''['TEST CASE' :'{}',
    'name':'SINE WAVE',
    'Amplitude':{},
    'Frequency':{},
    'Horizontal Offset':{},
    'Vertical Offset':{}],'''.format(dt,a,f,ho,vo)
    elif opt.get()==2:
        s='''['TEST CASE' :'{}',
    'name':'SQUARE WAVE',
    'Amplitude':{},
    'Frequency':{},
    'Horizontal Offset':{},
    'Vertical Offset':{}],'''.format(dt,a,f,ho,vo)
    elif opt.get()==3:
        s='''['TEST CASE' :'{}',
    'name':'SAWTOOTH WAVE',
    'Amplitude':{},
    'Frequency':{},
    'Horizontal Offset':{},
    'Vertical Offset':{}],'''.format(dt,a,f,ho,vo)
    elif opt.get()==4:
        s='''['TEST CASE' :'{}',
    'name':'TRIANGLE WAVE',
    'Amplitude':{},
    'Frequency':{},
    'Horizontal Offset':{},
    'Vertical Offset':{}],'''.format(dt,a,f,ho,vo)
    file.write(' \n')
    file.write(s)
    #file.write('\n--------------------------------\n')
    file.close()
    saved=tk.Label(canvas,text='Saved...',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=720,y=410)

def savpng():
    a=amp.get()
    f=freq.get()
    ho=hoff.get()
    vo=voff.get()
    count=0
    file=open('Data/Digital osciiloscope tablesetvalue.txt','r')
    l=file.read().split()
    count=l.count('TEST')
    file.close()

    x=list()
    y=list()
    s=float()
    for i in range(1,200,1):
        x.append(i)
        if opt.get()==1:
            s=a*m.sin((2*3.14*f*i)+ho)+vo
            y.append(s)
        elif opt.get()==2:
            s=a*m.sin((2*3.14*f*i)+ho)+vo
            if s<0.0:
                y.append(-1)
            elif s>0.0:
                y.append(1)
            elif s==0.0:
                y.append(0)

        elif opt.get()==3:
            s=-(2*a/3.14)*m.atan(1/m.tan(i*3.14*f+ho))+vo
            y.append(s)
        elif opt.get()==4:
            s=(2*a/3.14)*m.asin(m.sin(i*2*3.14*f+ho))+vo
            y.append(s)
        else:
            y.append(0)

    data=np.asarray(y*440)
    qwe=data.astype(float32)
    write("sound samples/sample {}.wav".format(dt),44100,qwe)
    fig=Figure(figsize=(7,5),dpi=75,facecolor='aqua')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=2.5)
    aggg.grid(True,color='black')
    aggg.set_facecolor('#071770')
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_title('Figure {}'.format(dt))
    aggg.get_figure().savefig('pictures/figure {}.pdf'.format(dt,format='pdf'))

    saved=tk.Label(canvas,text='Saved...',fg='white',relief=FLAT,
                  bg='#1a2024',font=('AgencyFB',8,'normal')).place(x=720,y=460)

    window.update_idletasks()

def sine():
    x=list()
    y=list()
    s=float()
    for i in range(0,33,1):
        x.append(i)
        s=m.sin(i*0.2)
        y.append(s)

    fig=Figure(figsize=(4,2),dpi=50,facecolor='#1a2024')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=6)
    aggg.grid(False)
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#1a2024')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=490)

def square():
    x=list()
    y=list()
    s=float()
    for i in range(0,33,1):
        x.append(i)
        s=m.sin(i*0.2)
        if s<0.0:
            y.append(-1.0)
        elif s>0.0:
            y.append(1.0)
        elif s==0.0:
            y.append(0.0)


    fig=Figure(figsize=(4,2),dpi=50,facecolor='#1a2024')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=6)
    aggg.grid(False)
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#1a2024')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=490)

def saw():
    x=list()
    y=list()
    s=float()
    for i in range(1,40,1):
        x.append(i)
        s=-(2*1/3.14)*m.atan(1/m.tan(i*3.14*0.1))
        y.append(s)

    fig=Figure(figsize=(4,2),dpi=50,facecolor='#1a2024')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=6)
    aggg.grid(False)
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#1a2024')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=490)

def tri():
    x=list()
    y=list()
    s=float()
    for i in range(1,40,1):
        x.append(i)
        s=(2*1/3.14)*m.asin(m.sin(i*2*3.14*0.1))
        y.append(s)

    fig=Figure(figsize=(4,2),dpi=50,facecolor='#1a2024')
    aggg=fig.add_subplot(111)
    aggg.plot(x,y,color='#00f7ff',linewidth=6)
    aggg.grid(False)
    aggg.set_xlabel('time')
    aggg.set_ylabel('amplitude')
    aggg.set_facecolor('#1a2024')
    c=FigureCanvasTkAgg(fig,master=window)
    c.get_tk_widget().place(x=20,y=490)



#BUTTONS
refresh=tk.Button(canvas,text='REFRESH',padx=10,pady=2,fg='black',bg='cyan',relief=
                  FLAT,command=ref,activebackground='cyan').place(x=705,y=40)

reset=tk.Button(canvas,text='RESET',padx=10,pady=2,fg='black',bg='cyan',relief=
                  FLAT,command=rst,activebackground='cyan').place(x=580,y=40)

save1=tk.Button(canvas,text='SAVE VALUES',padx=10,pady=2,fg='black',bg='cyan',relief=
                  FLAT,command=sav,activebackground='cyan').place(x=580,y=410)

save2=tk.Button(canvas,text='SAVE GRAPH AND\nSAMPLE',padx=10,pady=2,fg='black',bg='cyan',relief=
                  FLAT,command=savpng,activebackground='cyan').place(x=580,y=460)

#CHECKBUTTONS
opt=IntVar()
C1=tk.Radiobutton(canvas,text='SINE WAVE',variable=opt,value=1,height=2,width=12,fg='white'
                  ,bg='#283238',activebackground='#283238',activeforeground='white',selectcolor='#1a2024',
                  relief=FLAT,command=sine).place(x=20,y=40)


C1=tk.Radiobutton(canvas,text='SQUARE WAVE',variable=opt,value=2,height=2,width=12,fg='white'
                  ,bg='#283238',activebackground='#283238',activeforeground='white',selectcolor='#1a2024',
                  relief=FLAT,command=square).place(x=140,y=40)

C1=tk.Radiobutton(canvas,text='SAWTOOTH WAVE',variable=opt,value=3,height=2,width=16,fg='white'
                  ,bg='#283238',activebackground='#283238',activeforeground='white',selectcolor='#1a2024',
                  relief=FLAT, command=saw).place(x=260,y=40)

C1=tk.Radiobutton(canvas,text='TRIANGLE WAVE',variable=opt,value=4,height=2,width=15,fg='white'
                  ,bg='#283238',activebackground='#283238',activeforeground='white',selectcolor='#1a2024',
                  relief=FLAT, command=tri).place(x=410,y=40)


window.mainloop()
os.system('python "C:/Users/jfa/Documents/programz/digital oscilloscope/Data Creator.py')