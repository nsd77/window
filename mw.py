
from tkinter import*
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk


w=Tk()
w.geometry('900x500')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.title('face recognition')



def default_home():
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)


   
def home():
    f1.destroy()
    f2=Frame(w,width=600,height=455,bg='#262626')
    f2.place(x=50,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    face()

def student():

    face()



def detection():

    face()


def attendence():
    
    face()


def data():

    face()


def photos():

    face()





def face():
    global f1
    f1=Frame(w,width=300,height=500,bg='#d3d3d3')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,95,'Home','#C6E2FF','#FFFAFA',home)
    bttn(0,130,'Student detail','#C6E2FF','#FFFAFA',student)
    bttn(0,165,'face detection','#C6E2FF','#FFFAFA',detection)
    bttn(0,200,'Attendence','#C6E2FF','#FFFAFA',attendence)
    
    bttn(0,235,'train data','#C6E2FF','#FFFAFA',data)
    bttn(0,270,'photos','#C6E2FF','#FFFAFA',photos)

    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=face,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open(r"D:\project pics\close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)



default_home()

img1 = ImageTk.PhotoImage(Image.open(r"D:\project pics\open.png"))

global b2
b2=Button(w,image=img1,
       command=face,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)
    





w.mainloop()
