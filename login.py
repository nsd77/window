from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image

class login:
    def __init__(self,window):
     self.window=window
     self.window.geometry('1530x790+0+0')
     #self.window.state('zoomed')
     

     #self.bg_frame=Image.open(r"D:\project pics\lbg.png")
     #bg_frame=bg_frame.resize((1530,790),Image.ANTIALIAS)
     # photo=ImageTk.PhotoImage(self.bg_frame)
     
     #self.bg_panel=Label(self.window,image=photo)
     #self.bg_panel.image=photo
     #self.bg_panel.pack(fill='both',expand='true')


     #bg image
     img=Image.open(r"D:\project pics\lbg.png")
     img=img.resize((1530,790),Image.ANTIALIAS)
     self.photoimg=ImageTk.PhotoImage(img)

     fbl=Label(self.window,image=self.photoimg)
     fbl.place(x=0,y=0,width=1530,height=790)

     #login frame
     self.lgn_frame=Frame(self.window,bg="#000000",width="1150",height=700)
     self.lgn_frame.place(x=200,y=70)
     self.txt='Welcome ! ! !'
     self.heading=Label(self.lgn_frame,text=self.txt,font=('Times new roman',30,'bold'),bg='#000000',fg='white')
     self.heading.place(x=80,y=30,width=300,height=30)

     leftimg=Image.open(r"D:\project pics\new.png")
     leftimg=leftimg.resize((590,520),Image.ANTIALIAS)
     self.photoimg1=ImageTk.PhotoImage(leftimg)


     
     leftbl=Label(self.window,image=self.photoimg1,bg='#000000')
     leftbl.place(x=200,y=230,width=590,height=520)

     #sign up part
     signimg=Image.open(r"D:\project pics\hyy.png")
     signimg=signimg.resize((160,130),Image.ANTIALIAS)
     self.photoimg2=ImageTk.PhotoImage(signimg)
     signlbl=Label(self.window,image=self.photoimg2,bg='#000000')
     signlbl.place(x=977,y=100,width=160,height=130)
    
     self.txt1="Sign in"
     self.sign_in_lbl=Label(self.lgn_frame,text=self.txt1,font=('Times new roman',25,'bold'),bg='#000000',fg='white')
     self.sign_in_lbl.place(x=725,y=110,width=250,height=180)

     #username
     self.txt2="username"
     self.sign_in_lbl=Label(self.lgn_frame,text=self.txt2,font=('Times new roman',16,'bold'),bg='#000000',fg='#4f4d4e')
     self.sign_in_lbl.place(x=625,y=250,width=180,height=50)

     self.username_entry=Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='black',fg='white',font=('comic sans ms',15,'bold'),cursor='hand2')
     self.username_entry.place(x=700,y=305,width=370)

     self.username_line=Canvas(self.lgn_frame,width=400,height=2.0,bg='#bdb9b1',highlightthickness=0)
     self.username_line.place(x=668,y=338)

     userimg=Image.open(r"D:\project pics\username_icon.png")
     userimg=userimg.resize((40,30),Image.ANTIALIAS)
     self.photoimg3=ImageTk.PhotoImage(userimg)
     userlbl=Label(self.window,image=self.photoimg3,bg='#000000')
     userlbl.place(x=860,y=375,width=40,height=30)

     #password
     self.txt3="password"
     self.pswdlbl=Label(self.lgn_frame,text=self.txt3,font=('Times new roman',16,'bold'),bg='#000000',fg='#4f4d4e')
     self.pswdlbl.place(x=625,y=340,width=180,height=50)

     self.pswdentry=Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='black',fg='white',font=('comic sans ms',15,'bold'),show='*',cursor='hand2')
     self.pswdentry.place(x=700,y=395,width=370)

     self.pswdline=Canvas(self.lgn_frame,width=400,height=2.0,bg='#bdb9b1',highlightthickness=0)
     self.pswdline.place(x=668,y=428)

     psdimg=Image.open(r"D:\project pics\password_icon.png")
     psdimg=psdimg.resize((40,30),Image.ANTIALIAS)
     self.photoimg4=ImageTk.PhotoImage(psdimg)
     plbl=Label(self.window,image=self.photoimg4,bg='#000000')
     plbl.place(x=860,y=465,width=40,height=30)


     
     lgnbuttonimg=Image.open(r"D:\project pics\login2.png")
     lgnbuttonimg=lgnbuttonimg.resize((200,60),Image.ANTIALIAS)
     self.photoimg5=ImageTk.PhotoImage(lgnbuttonimg)
     lgnbbl=Button(self.window,image=self.photoimg5,bg='#000000',activebackground='#040405',cursor='hand2',bd=0)
     lgnbbl.place(x=975,y=525,width=200,height=60)

     #self.lgn_button=Button(self.lgn_frame,text="LOGIN",font=('Times new roman',13,'bold'),width=25,bd=0,bg='#3047ff',cursor='hand2',activebackground='#3047ff',fg='white')
     #self.lgn_button.place(x=20,y=10)

     #forget password
     self.forgetb=Button(self.lgn_frame,text='Forget password?',font=('Times new roman',14,'bold underline'),fg='red',width=25,bd=0,bg='#040405',activebackground='#040405',cursor='hand2')
     self.forgetb.place(x=740,y=520)

     #sign up
     self.sign_up= Label(self.lgn_frame,text="No account yet?",font=('Times new roman',13,'bold'),background='#040405',fg='white')
     self.sign_up.place(x=665,y=570)

     
     signbuttonimg=Image.open(r"D:\project pics\s3.png")
     signbuttonimg=signbuttonimg.resize((150,60),Image.ANTIALIAS)
     self.photoimg6=ImageTk.PhotoImage(signbuttonimg)
     sbl=Button(self.window,image=self.photoimg6,bg='#000000',activebackground='#040405',cursor='hand2',bd=0)
     sbl.place(x=1000,y=640,width=150,height=60)

     #show/hide
     showbuttonimg=Image.open(r"D:\project pics\show.png")
     showbuttonimg=showbuttonimg.resize((15,15),Image.ANTIALIAS)
     self.photoimg7=ImageTk.PhotoImage(showbuttonimg)
     swbl=Button(self.window,image=self.photoimg7,bg='black',activebackground='black',cursor='hand2',bd=0,command=show)
     swbl.place(x=1275,y=475,width=15,height=15)

     hidebuttonimg=Image.open(r"D:\project pics\hide.png")
     hidebuttonimg=hidebuttonimg.resize((15,15),Image.ANTIALIAS)
     self.photoimg8=ImageTk.PhotoImage(hidebuttonimg)
     
def show(self):


    self.hidebl=Button(self.window,image=self.photoimg8,bg='white',activebackground='white',cursor='hand2',bd=0,command=hide)
    self.hidebl.place(x=1275,y=475,width=15,height=15)
    self.pswdentry.config(show=' ')

def hide(self):
    self.photoimg7=ImageTk.PhotoImage(showbuttonimg)
    swbl=Button(self.window,image=self.photoimg7,bg='black',activebackground='black',cursor='hand2',bd=0,command=show)
    swbl.place(x=1275,y=475,width=15,height=15)
    self.pswdentry(show='*')

















     



    







#def page():
   # window=Tk()
    #login(window)
    #window.mainloop()


#if __name__=='__main__':
    #page()


if __name__=="__main__":
    window=Tk()
    obj=login(window)
    window.mainloop()