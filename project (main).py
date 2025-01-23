from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import random
from tkinter import ttk
import os



root_1=Tk()
root_1.title("MOBILE PHONE MANAGEMENT SYSTEM")
root_1.attributes("-fullscreen",True)
root_1.configure(bg="#031163")

my_pic=Image.open("Image-1.jpg")
resized=my_pic.resize((1235,675), Image.LANCZOS)

new_pic=ImageTk.PhotoImage(resized)
img=Label(root_1,image=new_pic)
img.place(x=20,y=20)

photo=PhotoImage(file="h.png")
root_1.iconphoto(True, photo)
    

#Exit function
def Exit():
    root_1.destroy()

#info function
def info():

    frame_=LabelFrame(root_1,bg="#4203c9",borderwidth=8, relief=RIDGE)
    frame_.place(x=20,y=20,height=680,width=1240)

    About_s=Label(frame_, text="===========    ABOUT  US    ============",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",44)).place(x=5,y=10)
    pro=Label(frame_, text="ABOUT PROJECT :",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",29)).place(x=25,y=80)

    inf=Label(frame_, text='''       Lets know about the features of this Mobile Management System, this project is designed for a completely virtualised \n management of any Mobile shop. A person can Register  cell phone details and can Search or Modify the related figures \n as well. They can also Delete the unnecessary data from databse, and can view the details that are present in the \n system according to theri needs. They can also view the Gallery. ''',bg='#4203c9',fg="#e8d71e",font=("cambria",17),justify='left').place(x=25,y=130)

    dev=Label(frame_, text="ABOUT DEVELOPERS :",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",29)).place(x=25,y=270)
    
    inf1=Label(frame_,text='        This project is created by Shubham as part of my class 12th C.S Project \n 2020 - 2021, under the able and vey helpful guidance of PGT Mr. ML Meena Sir, Kendiya Vidayalaya No.2 Delhi cantt. \n All the codes in this project are written by me only. All images and icons used under CC license.',bg='#4203c9',fg="#e8d71e",font=("cambria",17),justify='left').place(x=25,y=320)

    name=Label(frame_, text="SHUBHAM",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",18)).place(x=115,y=585)
           
    logo1=Image.open("shubham.jpg")
    resized1=logo1.resize((150,150), Image.LANCZOS)
    R_logo1=ImageTk.PhotoImage(resized1)
    lbal=Label(frame_, image=R_logo1)
    lbal.place(x=100,y=425)
 
   
    def retn():
        root_1.configure(bg="#031163")
        frame_.destroy()



    ret_btn=Button(frame_, text="RETURN",fg="white",bg="black" ,cursor='hand2',font=("Georgia",22),borderwidth=5,command=retn)
    ret_btn.place(x=0,y=630,height=35,width=1222)
    

    

def start():
    root=Toplevel()
    root.attributes("-fullscreen",True)
    root.title("MOBILE PHONE MANAGEMENT SYSTEM")
    root.configure(bg="#63c5ee")


    #submit function
    def submit():
        global res
        global Enter_btn
        global Search_btn
        global Modify_btn
        global Delete_btn
        global Gallery_btn
        global View_btn
        
        try:
            res=mysql.connector.connect(host='localhost', user=usernm.get(), password=key.get(),database='mobilesystemmanagement')
            if bool(res)==True:  
        
        #connect buttons widgets
                
                Enter_btn=Button(root, text="REGISTRATION",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,bd=5,activebackground="#0472e8",command=create)
                Enter_btn.place(x=30,y=120)
                Search_btn=Button(root, text="SEARCH ",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=search)
                Search_btn.place(x=30,y=205)
                Modify_btn=Button(root, text="MODIFY ",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=modify)
                Modify_btn.place(x=30,y=290)
                Delete_btn=Button(root, text="DELETE ",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=erase)
                Delete_btn.place(x=30,y=375)
                View_btn=Button(root, text="VIEW DETAILS",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=view)
                View_btn.place(x=30,y=460)
                Gallery_btn=Button(root, text="GALLERY",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=galry)
                Gallery_btn.place(x=30,y=545)
                exit_btn=Button(root, text="HOME",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,activebackground="#0472e8",command=exit)
                exit_btn.place(x=30,y=630)
                   
        except:
             Enter_btn=Button(root, text="REGISTRATION",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,bd=5,command=create)
             Enter_btn.place(x=30,y=120)
             Search_btn=Button(root, text="SEARCH ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=search)
             Search_btn.place(x=30,y=205)
             Modify_btn=Button(root, text="MODIFY ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=modify)
             Modify_btn.place(x=30,y=290)
             Delete_btn=Button(root, text="DELETE ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=erase)
             Delete_btn.place(x=30,y=375)
             View_btn=Button(root, text="VIEW DETAILS",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=view)
             View_btn.place(x=30,y=460)
             Gallery_btn=Button(root, text="GALLERY",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=galry)
             Gallery_btn.place(x=30,y=545)
             exit_btn=Button(root, text="HOME",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),padx=15,pady=8,borderwidth=5,command=exit)
             exit_btn.place(x=30,y=630)
             messagebox.showerror("Error","Invalid Username Or Password, Please Try Again",parent=root)
        new.destroy()
        
            
    #connect function

    def connect ():
        global usernm
        global key
        global new
        new=Toplevel()
        new.title("CONNECT TO MYsql")
        new.configure(bg="#b3b3b3")
        new.geometry("600x220")
        new.resizable(width=False,height=False)
        
        user_=Label(new, text="Username::",font=("Georgia",20),padx=20,bg="#b3b3b3").grid(row=1,column=0,sticky=W)
        usernm=Entry(new, width=35,borderwidth=3,bg="white",font=("Georgia",12))
        usernm.grid(row=1,column=1)

        temp=Label(new,text='',bg="#b3b3b3").grid(row=2,column=0)
        temp1=Label(new,text="",bg="#b3b3b3").grid(row=4,column=0)
        temp2=Label(new,text="",bg="#b3b3b3").grid(row=5,column=0)
        temp3=Label(new,text="",bg="#b3b3b3").grid(row=7,column=0)
        
        key_=Label(new, text="Password::",font=("Georgia",20),padx=20,bg="#b3b3b3").grid(row=3,column=0,sticky=W)
        key=Entry(new, width=35,borderwidth=3,bg="white",font=("Georgia",12),show="*")
        key.grid(row=3,column=1)


        btn_submit=Button(new, text="SUBMIT",fg="white",bg="black" ,cursor='hand2',font=("Georgia",22),borderwidth=5,command=submit,padx=20).grid(padx=20,row=6,column=0)
        btn_reset=Button(new, text="RESET",fg="white",bg="black" ,cursor='hand2',font=("Georgia",22),borderwidth=5,command=reset,padx=20).grid(padx=20,row=6,column=1,sticky=E)

        new.mainloop()

    

    #reset function
    def reset():
        key.delete(0, END)
        usernm.delete(0, END)
    #Exit function
    def exit():

        frame_mai=LabelFrame(root,padx=10,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_mai.place(x=430,y=205,height=495,width=840,bordermode=OUTSIDE)
           
        lbl1=Label(frame_mai, image=R_logo)
        lbl1.place(x=10,y=10)
 
        response= messagebox.askyesno("EXIT ","Do You Wish To Exit",parent=root)
        
        if response==1:
            root.destroy()
        else:
            Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
                 
       

    #Label widgets

    L1=Label(root,text="======WELCOME TO MOBILE PHONE MANAGEMENT SYSTEM===========   ",bg="black",fg='#ffffff',font=("Broadway",26),pady=20).place(x=0,y=0)


    #Reset Function
    def reset():
        
        Mod.delete(0, END)
        Internal.delete(0, END)
        Memory.delete(0, END)
        Cam.delete(0, END)
        Comp.delete(0, END)
        Cost.delete(0,END)
        byt.delete(0,END)
        byt1.delete(0,END)
        wto.delete(0,END)

    def reset1():
        
        Mod.delete(0, END)
        M_id.delete(0,END)
        M_id1.delete(0,END)
        Internal.delete(0, END)
        Memory.delete(0, END)
        Cam.delete(0, END)
        Comp.delete(0, END)
        Cost.delete(0,END)
        byt_s.delete(0,END)
        byt1_s.delete(0,END)
        wto_s.delete(0,END)

    def reset2():

            M_id1.delete(0,END)
            M_id2.delete(0,END)
            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)
            
            

   #create function
    def create():

        global Mod
        global Internal
        global Memory
        global Cam
        global Comp
        global Cost
        global byt
        global byt1
        global wto

        s=ttk.Style(root)
        s.theme_use("winnative")

        
        frame_main=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main.place(x=430,y=205,height=495,width=840)
 
        Mod_=Label(frame_main, text="Model Name              ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=19)
        Mod=Entry(frame_main, width=35,borderwidth=3,bg="white",font=("Georgia",14))
        Mod.place(x=360,y=19)
        
        Internal_=Label(frame_main, text="Internal Storage  ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=74)
        Internal=Entry(frame_main, width=26,borderwidth=3,bg="white",font=("Georgia",14))
        Internal.place(x=360,y=74)
        
        Memory_=Label(frame_main, text="Memory                      ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=129)
        Memory=Entry(frame_main, width=26,borderwidth=3,bg="white",font=("Georgia",14))
        Memory.place(x=360,y=129)
        
        Cam_=Label(frame_main, text="Camera px                     ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=184)
        Cam=Entry(frame_main, width=18,borderwidth=3,bg="white",font=("Georgia",14))
        Cam.place(x=360,y=184)
        
        Comp_=Label(frame_main, text="Company                     ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=239)
        Comp=Entry(frame_main, width=35,borderwidth=3,bg="white",font=("Georgia",14))
        Comp.place(x=360,y=239)

        Cost_=Label(frame_main, text="Price                   ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=294)
        Cost=Entry(frame_main, width=35,borderwidth=3,bg="white",font=("Georgia",14))
        Cost.place(x=360,y=294)
         
        
        Enter_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")
        Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")

        temp_13=Label(frame_main,text="--------Enter Valid Information Only -------",bg="#4203c9",fg="#e8d71e",font=("Georgia",12)).place(x=240,y=460)


        byt=ttk.Combobox(frame_main ,font=("Calibri",14,"bold"),width=6)
        byt['values'] = ("KB","MB","GB","TB")
        byt.place(x=701,y=74)

        byt1=ttk.Combobox(frame_main ,font=("Calibri",14,"bold"),width=6)
        byt1['values'] = ("KB","MB","GB","TB")
        byt1.place(x=701,y=129)

        wto=ttk.Combobox(frame_main ,font=("Calibri",14,"bold"),width=15)
        wto['values'] = ("Without_Camera")
        wto.place(x=610,y=184)
        

        
        def confirm():
            global a
            
            cr=res.cursor()

            num= random.sample(range(1000000,9999999),1)
            num1= ' '.join(str(i) for i in num)
        
                
            a= 'AS' + num1 + 'S'
            b= Mod.get()
            c= Internal.get()
            d= Memory.get()
            e= Cam.get()
            f= Comp.get()
            g=Cost.get()
            

            for i in b:
                if i.isspace()==True:
                    space_= i
                else:
                    space_=''

            for j in f:
                if j.isspace()==True:
                    Space_= j
                else:
                    Space_=''

            try:
                
                if (b.isalnum() == True or space_.isspace() == True) and (c.isdigit() == True) and (d.isdigit() == True) and (e.isdigit() == True or e=='') and (f.isalnum() == True or Space_.isspace==True) and (g.isdigit() == True):
                    
                    m,n,o,p,q,r=b.upper(),c.upper(),d.upper(),e.upper(),f.upper(),g.upper()
                    n=n + byt.get()
                    o=o + byt1.get()
                    p=p or wto.get()
                    data=(a,m,n,o,p,q,r)
                    qr = "INSERT INTO info (Mobile_id ,Name ,Storage ,Memory ,Camera_px ,Company,Price) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    cr.execute(qr,data)
                    res.commit()
                    messagebox.showinfo("Registered Successfully","ID: " + a,parent=root)
                    
                    Mod.delete(0, END)
                    Internal.delete(0, END)
                    Memory.delete(0, END)
                    Cam.delete(0, END)
                    Comp.delete(0, END)
                    Cost.delete(0,END)

                    byt.delete(0,END)
                    byt1.delete(0,END)
                    wto.delete(0,END)
                    
                else:
                    messagebox.showwarning("Type Error","Invalid Data Type , Please enter Valid data only",parent=root)

            except:
               messagebox.showwarning(" Error","Incomplete Data , Please enter Complete Data",parent=root)

        

        btn_conf=Button(frame_main, text="REGISTER",fg="white",cursor='hand2',bg="black" ,font=("Georgia",18),width=18,borderwidth=5,padx=20,command=confirm).place(x=20,y=400)
        btn_rset=Button(frame_main, text="RESET",fg="white",cursor='hand2',bg="black" ,font=("Georgia",18),width=18,borderwidth=5,padx=20,command=reset).place(x=490,y=400)
        #search function
    def srch(a):

        y=M_id1.get()
        if  y.lower()== 'mobile_id':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)
            
            M_id.configure(state='normal',bg="#bcbcbc")
            Mod.configure(state='disabled')
            Internal.configure(state='disabled')
            Memory.configure(state='disabled')
            Cam.configure(state='disabled')
            Comp.configure(state='disabled')
            Cost.configure(state='disabled')
            byt_s.configure(state='disabled')
            byt1_s.configure(state='disabled')
            wto_s.configure(state='disabled')

        elif y.lower()=='model_name':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)

            
            Mod.configure(state='normal',bg="#bcbcbc")
            M_id.configure(state='disabled')
            Internal.configure(state='disabled')
            Memory.configure(state='disabled')
            Cam.configure(state='disabled')
            Comp.configure(state='disabled')
            Cost.configure(state='disabled')
            byt_s.configure(state='disabled')
            byt1_s.configure(state='disabled')
            wto_s.configure(state='disabled')

        elif y.lower()=='internal_storage':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)

            
            Internal.configure(state='normal',bg="#bcbcbc")
            byt_s.configure(state='normal')
            M_id.configure(state='disabled')
            Mod.configure(state='disabled')
            Memory.configure(state='disabled')
            Cam.configure(state='disabled')
            Comp.configure(state='disabled')
            Cost.configure(state='disabled')
            byt1_s.configure(state='disabled')
            wto_s.configure(state='disabled')

        elif y.lower()=='memory':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)

            
            Memory.configure(state='normal',bg="#bcbcbc")
            byt1_s.configure(state='normal')
            M_id.configure(state='disabled')
            Mod.configure(state='disabled')
            Internal.configure(state='disabled')
            Cam.configure(state='disabled')
            Comp.configure(state='disabled')
            Cost.configure(state='disabled')
            byt_s.configure(state='disabled')
            wto_s.configure(state='disabled')

        elif y.lower()=='camera_px':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)

            
            Cam.configure(state='normal',bg="#bcbcbc")
            wto_s.configure(state='normal')
            M_id.configure(state='disabled')
            Mod.configure(state='disabled')
            Internal.configure(state='disabled')
            Memory.configure(state='disabled')
            Comp.configure(state='disabled')
            Cost.configure(state='disabled')
            byt_s.configure(state='disabled')
            byt1_s.configure(state='disabled')
            
             
        elif y.lower()=='company':

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)

            
            Comp.configure(state='normal',bg="#bcbcbc")
            M_id.configure(state='disabled')
            Mod.configure(state='disabled')
            Internal.configure(state='disabled')
            Memory.configure(state='disabled')
            Cam.configure(state='disabled')
            Cost.configure(state='disabled')
            byt_s.configure(state='disabled')
            byt1_s.configure(state='disabled')
            wto_s.configure(state='disabled')
            
        else:

            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)


            Cost.configure(state='normal',bg="#bcbcbc")
            M_id.configure(state='disabled')
            Mod.configure(state='disabled')
            Internal.configure(state='disabled')
            Memory.configure(state='disabled')
            Cam.configure(state='disabled')
            Comp.configure(state='disabled')
            byt_s.configure(state='disabled')
            byt1_s.configure(state='disabled')
            wto_s.configure(state='disabled')
            
    def search():
        
        global M_id1
        global M_id
        global Mod
        global Internal
        global Memory
        global Cam
        global Comp
        global Cost
        global byt_s
        global byt1_s
        global wto_s
        global frame_main2

        s=ttk.Style(root)
        s.theme_use("winnative")

        s.configure(".", font=("Calibri",11))
        s.configure("Treeview.Heading", foreground ='red',background='#babbc1', font=("ALGERIAN",12,'bold'),fieldbackground='#D3D3D3')
        s.map ('Treeview',background=[('selected','blue')])
        
        frame_main2=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main2.place(x=430,y=205,height=495,width=840)
 
        M_id_=Label(frame_main2, text="Mobile ID                    ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=19)
        M_id=Entry(frame_main2, width=16,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        M_id.place(x=360,y=19)

        M_id1=ttk.Combobox(frame_main2 ,font=("Calibri",14,"bold"),width=16)
        M_id1['values'] = ('Mobile_Id'  , 'Model_Name'  , 'Internal_Storage'  , 'Memory'  , 'Camera_px' ,  'Company'  ,'Price')
        M_id1.bind("<<ComboboxSelected>>",srch)
        M_id1.place(x=605,y=19)
        
        Mod_=Label(frame_main2, text="Model Name              ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=74)
        Mod=Entry(frame_main2, width=35,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Mod.place(x=360,y=74)
        
        Internal_=Label(frame_main2, text="Internal Storage  ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=129)
        Internal=Entry(frame_main2, width=26,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Internal.place(x=360,y=129)
        
        Memory_=Label(frame_main2, text="Memory                      ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=184)
        Memory=Entry(frame_main2, width=26,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Memory.place(x=360,y=184)
        
        Cam_=Label(frame_main2, text="Camera px                     ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=239)
        Cam=Entry(frame_main2, width=18,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Cam.place(x=360,y=239)
        
        Comp_=Label(frame_main2, text="Company                     ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=294)
        Comp=Entry(frame_main2, width=35,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Comp.place(x=360,y=294)

        Cost_=Label(frame_main2, text="Price                     ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=349)
        Cost=Entry(frame_main2, width=35,borderwidth=3,bg="white",font=("Georgia",14),state='disabled')
        Cost.place(x=360,y=349)
        
        temp_13=Label(frame_main2,text="--------Enter the related category you want to search-------",bg="#4203c9",fg="#e8d71e",font=("Georgia",12)).place(x=180,y=460)

      
        Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Search_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")
        Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")

        


        byt_s=ttk.Combobox(frame_main2 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        byt_s['values'] = ("KB","MB","GB","TB")
        byt_s.place(x=701,y=129)

        byt1_s=ttk.Combobox(frame_main2 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        byt1_s['values'] = ("KB","MB","GB","TB")
        byt1_s.place(x=701,y=184)

        wto_s=ttk.Combobox(frame_main2 ,font=("Calibri",14,"bold"),width=15,state='disabled')
        wto_s['values'] = ("Without_Camera")
        wto_s.place(x=610,y=239)



        def retn():

              
            frame_temp.destroy()
            Mod.delete(0, END)
            Internal.delete(0, END)
            Memory.delete(0, END)
            Cam.delete(0, END)
            Comp.delete(0, END)
            Cost.delete(0,END)
            M_id1.delete(0,END)
            M_id.delete(0,END)

            byt_s.delete(0,END)
            byt1_s.delete(0,END)
            wto_s.delete(0,END)


        def Confirm1():
                global frame_temp
                
                frame_temp=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
                frame_temp.place(x=430,y=205,height=495,width=840)
                
                tableframe=Frame(frame_temp, bd=5, relief=RIDGE, bg='#031163')
                tableframe.place(x=0,y=60,height=410, width=820)

                bck=Button(frame_temp, text="RETURN",fg="white",bg="black" ,font=("Georgia",18),width=54,borderwidth=5,padx=20,command=retn)
                bck.place(x=5,y=0)
                
                scrollx=Scrollbar(tableframe, orient=HORIZONTAL)
                scrolly=Scrollbar(tableframe, orient=VERTICAL)
                mobiletable=ttk.Treeview(tableframe, columns=(1,2,3,4,5,6,7),height=5, xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                mobiletable.column(1, width= 130 ,minwidth=130, anchor=CENTER)
                mobiletable.column(2, width= 150,minwidth=150, anchor=CENTER)
                mobiletable.column(3, width= 190,minwidth=190, anchor=CENTER)
                mobiletable.column(4, width= 120,minwidth=120, anchor=CENTER)
                mobiletable.column(5, width= 130,minwidth=130, anchor=CENTER)
                mobiletable.column(6, width= 150, minwidth=150, anchor=CENTER)
                mobiletable.column(7, width= 100,minwidth=100, anchor=CENTER)

                scrollx.configure(command=mobiletable.xview)
                scrolly.configure(command=mobiletable.yview)
                mobiletable.heading(1,text="MOBILE ID")
                mobiletable.heading(2,text="MODEL NAME")
                mobiletable.heading(3,text="INTERNAL STORAGE")
                mobiletable.heading(4,text="MEMORY")
                mobiletable.heading(5,text="CAMERA Px.")
                mobiletable.heading(6,text="COMPANY")
                mobiletable.heading(7,text="PRICE")
                mobiletable[  'show' ] = ' headings '
                mobiletable.pack(fill=BOTH, expand=1)

                s=ttk.Style(root)
                s.theme_use("winnative")

                s.configure(".", font=("Calibri",11))
                s.configure("Treeview.Heading", foreground ='red',background='#babbc1', font=("ALGERIAN",12,'bold'))

                mobiletable.tag_configure('oddrow', background="#e9e9e9")
                mobiletable.tag_configure('evenrow', background="lightblue")

                cr=res.cursor()

                a1 = M_id.get()
                b1= Mod.get()
                c1= Internal.get()
                d1= Memory.get()
                e1= Cam.get()
                f1= Comp.get()
                g1=Cost.get()

                m1,n1,o1,p1,q1,r1=b1,c1,d1,e1,f1,g1
                n1=n1 + byt_s.get()
                o1=o1 + byt1_s.get()
                p1=p1 or wto_s.get()

                qr1=" SELECT * FROM info WHERE Mobile_id = %s  OR Name = %s OR Storage = %s OR Memory = %s OR Camera_px = %s OR Company = %s OR Price = %s"
    
                cr.execute(qr1,(a1,b1,n1,o1,p1,q1,r1,))
                rows=cr.fetchall()
                total=cr.rowcount

                mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                if total==0:
                    messagebox.showinfo("Nothing Here"," Please Recheck Your Data And Try Again",parent=frame_main2)
                    retn()
                else:
                    messagebox.showinfo("Rows Effected"," No. Of Entries Affected : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1
    


        btn_conf1=Button(frame_main2, text="SEARCH",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=Confirm1).place(x=20,y=400)
        btn_rset1=Button(frame_main2, text="RESET",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=reset1).place(x=490,y=400)

#Modify function
        
    def select(event):
            if M_id2.get() =="COMPLETE_ENTRY":
                cr=res.cursor()
                query_="SELECT Mobile_id FROM info"
                cr.execute(query_)
                rows = cr.fetchall()
                res.commit()

                Mod1.delete(0,END)
                Mod2.delete(0, END)
                Internal1.delete(0,END)
                Internal2.delete(0, END)
                Internal3.delete(0,END)
                Internal4.delete(0,END)
                Memory1.delete(0,END)
                Memory2.delete(0, END)
                Memory3.delete(0,END)
                Memory4.delete(0,END)
                Cam1.delete(0,END)
                Cam2.delete(0, END)
                Cam3.delete(0,END)
                Cam4.delete(0,END)
                Comp1.delete(0,END)
                Comp2.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)
                
                M_id1.configure(state='normal',background='#ded9d9',values=rows)
                Mod2.configure(state='normal',background='#ded9d9')
                Internal2.configure(state='normal',background='#ded9d9')
                Internal4.configure(state='normal',background='#ded9d9')
                Memory2.configure(state='normal',background='#ded9d9')
                Memory4.configure(state='normal',background='#ded9d9')
                Cam2.configure(state='normal',background='#ded9d9')
                Cam4.configure(state='normal',background='#ded9d9')
                Comp2.configure(state='normal',background='#ded9d9')
                Cost2.configure(state='normal',background='#ded9d9')

                Mod1.configure(background='#ded9d9',state='disabled')
                Internal1.configure(background='#ded9d9',state='disabled')
                Internal3.configure(background='#ded9d9',state='disabled')
                Memory1.configure(background='#ded9d9',state='disabled')
                Memory3.configure(background='#ded9d9',state='disabled')
                Cam1.configure(background='#ded9d9',state='disabled')
                Cam3.configure(background='#ded9d9',state='disabled')
                Comp1.configure(background='#ded9d9',state='disabled')
                Cost1.configure(background='#ded9d9',state='disabled')
                
                M_id1.delete(0, END)

                

            elif M_id2.get()=="PARTICULAR_VALUE":

                v="Model_Name  Internal_Storage  Memory  Camera_px  Company  Price"
                M_id1.configure(background='#ded9d9',state='normal',values=v)
                M_id1.delete(0,END)
                M_id1.bind("<<ComboboxSelected>>",select2)

                Mod1.delete(0,END)
                Mod2.delete(0, END)
                Internal1.delete(0,END)
                Internal2.delete(0, END)
                Internal3.delete(0,END)
                Internal4.delete(0,END)
                Memory1.delete(0,END)
                Memory2.delete(0, END)
                Memory3.delete(0,END)
                Memory4.delete(0,END)
                Cam1.delete(0,END)
                Cam2.delete(0, END)
                Cam3.delete(0,END)
                Cam4.delete(0,END)
                Comp1.delete(0,END)
                Comp2.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)
                
                Mod1.configure(state='disabled',background='#ded9d9')
                Mod2.configure(state='disabled',background='#ded9d9')
                Internal1.configure(state='disabled',background='#ded9d9')
                Internal2.configure(state='disabled',background='#ded9d9')
                Internal3.configure(state='disabled',background='#ded9d9')
                Internal4.configure(state='disabled',background='#ded9d9')
                Memory1.configure(state='disabled',background='#ded9d9')
                Memory2.configure(state='disabled',background='#ded9d9')
                Memory3.configure(state='disabled',background='#ded9d9')
                Memory4.configure(state='disabled',background='#ded9d9')
                Cam1.configure(state='disabled',background='#ded9d9')
                Cam2.configure(state='disabled',background='#ded9d9')
                Cam3.configure(state='disabled',background='#ded9d9')
                Cam4.configure(state='disabled',background='#ded9d9')
                Comp1.configure(state='disabled',background='#ded9d9')
                Comp2.configure(state='disabled',background='#ded9d9')
                Cost1.configure(state='disabled',background='#ded9d9')
                Cost2.configure(state='disabled',background='#ded9d9')


            
            else:
                messagebox.showwarning(" Error","Invalid Selection , Please select from the given options only",parent=root)

    def select2(events):
        
        if (M_id1.get()).lower()=='model_name':

            cr=res.cursor()
            query_="SELECT Name FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()

            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)
            
            Internal1.configure(state='disabled',background='#ded9d9')
            Internal2.configure(state='disabled',background='#ded9d9')
            Internal3.configure(state='disabled',background='#ded9d9')
            Internal4.configure(state='disabled',background='#ded9d9')
            Memory1.configure(state='disabled',background='#ded9d9')
            Memory2.configure(state='disabled',background='#ded9d9')
            Memory3.configure(state='disabled',background='#ded9d9')
            Memory4.configure(state='disabled',background='#ded9d9')
            Cam1.configure(state='disabled',background='#ded9d9')
            Cam2.configure(state='disabled',background='#ded9d9')
            Cam3.configure(state='disabled',background='#ded9d9')
            Cam4.configure(state='disabled',background='#ded9d9')
            Comp1.configure(state='disabled',background='#ded9d9')
            Comp2.configure(state='disabled',background='#ded9d9')
            Cost1.configure(state='disabled',background='#ded9d9')
            Cost2.configure(state='disabled',background='#ded9d9')

            Mod1.configure(state='normal',background='#ded9d9',values=rows)
            Mod2.configure(state='normal',background='#ded9d9')
            
        elif (M_id1.get()).lower()=="internal_storage":

            cr=res.cursor()
            query_="SELECT Storage FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()

            got=[]
            k=''
            for row in rows:
                for i in row:
                    for j in i :
                       if j.isdigit()==True:
                           print(j)
                           k=k + str(j) 
                       else:
                           print(k)
                           got.append(k)
                           k=''



            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)
            
            Mod1.configure(state='disabled',background='#ded9d9')
            Mod2.configure(state='disabled',background='#ded9d9')
            Memory1.configure(state='disabled',background='#ded9d9')
            Memory2.configure(state='disabled',background='#ded9d9')
            Memory3.configure(state='disabled',background='#ded9d9')
            Memory4.configure(state='disabled',background='#ded9d9')
            Cam1.configure(state='disabled',background='#ded9d9')
            Cam2.configure(state='disabled',background='#ded9d9')
            Cam3.configure(state='disabled',background='#ded9d9')
            Cam4.configure(state='disabled',background='#ded9d9')
            Comp1.configure(state='disabled',background='#ded9d9')
            Comp2.configure(state='disabled',background='#ded9d9')
            Cost1.configure(state='disabled',background='#ded9d9')
            Cost2.configure(state='disabled',background='#ded9d9')

            Internal1.configure(state='normal',background='#ded9d9',values=got)
            Internal2.configure(state='normal',background='#ded9d9')
            Internal3.configure(state='normal',background='#ded9d9')
            Internal4.configure(state='normal',background='#ded9d9')

        elif (M_id1.get()).lower()=="memory":

            cr=res.cursor()
            query_="SELECT Memory FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()
            got=[]
            for row in rows:
                for i in row:
                    for j in i :
                       if j.isdigit()==True:
                           got.append(j)
                       else:
                           pass
                


            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)
            
            Mod1.configure(state='disabled',background='#ded9d9')
            Mod2.configure(state='disabled',background='#ded9d9')
            Internal1.configure(state='disabled',background='#ded9d9')
            Internal2.configure(state='disabled',background='#ded9d9')
            Internal3.configure(state='disabled',background='#ded9d9')
            Internal4.configure(state='disabled',background='#ded9d9')
            Cam1.configure(state='disabled',background='#ded9d9')
            Cam2.configure(state='disabled',background='#ded9d9')
            Cam3.configure(state='disabled',background='#ded9d9')
            Cam4.configure(state='disabled',background='#ded9d9')
            Comp1.configure(state='disabled',background='#ded9d9')
            Comp2.configure(state='disabled',background='#ded9d9')
            Cost1.configure(state='disabled',background='#ded9d9')
            Cost2.configure(state='disabled',background='#ded9d9')

            Memory1.configure(state='normal',background='#ded9d9',values=got)
            Memory2.configure(state='normal',background='#ded9d9')
            Memory3.configure(state='normal',background='#ded9d9')
            Memory4.configure(state='normal',background='#ded9d9')

        elif (M_id1.get()).lower()=="camera_px":

            cr=res.cursor()
            query_="SELECT Camera_px FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()


            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)
            
            Mod1.configure(state='disabled',background='#ded9d9')
            Mod2.configure(state='disabled',background='#ded9d9')
            Internal1.configure(state='disabled',background='#ded9d9')
            Internal2.configure(state='disabled',background='#ded9d9')
            Internal3.configure(state='disabled',background='#ded9d9')
            Internal4.configure(state='disabled',background='#ded9d9')
            Memory1.configure(state='disabled',background='#ded9d9')
            Memory2.configure(state='disabled',background='#ded9d9')
            Memory3.configure(state='disabled',background='#ded9d9')
            Memory4.configure(state='disabled',background='#ded9d9')
            Comp1.configure(state='disabled',background='#ded9d9')
            Comp2.configure(state='disabled',background='#ded9d9')
            Cost1.configure(state='disabled',background='#ded9d9')
            Cost2.configure(state='disabled',background='#ded9d9')

            Cam1.configure(state='normal',background='#ded9d9',values=rows)
            Cam2.configure(state='normal',background='#ded9d9')
            Cam3.configure(state='normal',background='#ded9d9')
            Cam4.configure(state='normal',background='#ded9d9')

        elif (M_id1.get()).lower()=="company":

            cr=res.cursor()
            query_="SELECT Company FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()


            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)

            Mod1.configure(state='disabled',background='#ded9d9')
            Mod2.configure(state='disabled',background='#ded9d9')
            Internal1.configure(state='disabled',background='#ded9d9')
            Internal2.configure(state='disabled',background='#ded9d9')
            Internal3.configure(state='disabled',background='#ded9d9')
            Internal4.configure(state='disabled',background='#ded9d9')
            Memory1.configure(state='disabled',background='#ded9d9')
            Memory2.configure(state='disabled',background='#ded9d9')
            Memory3.configure(state='disabled',background='#ded9d9')
            Memory4.configure(state='disabled',background='#ded9d9')
            Cam1.configure(state='disabled',background='#ded9d9')
            Cam2.configure(state='disabled',background='#ded9d9')
            Cam3.configure(state='disabled',background='#ded9d9')
            Cam4.configure(state='disabled',background='#ded9d9')
            Cost1.configure(state='disabled',background='#ded9d9')
            Cost2.configure(state='disabled',background='#ded9d9')

            Comp1.configure(state='normal',background='#ded9d9',values=rows)
            Comp2.configure(state='normal',background='#ded9d9')

        elif (M_id1.get()).lower()=="price":

            cr=res.cursor()
            query_="SELECT Price FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
            res.commit()


            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)

            Mod1.configure(state='disabled',background='#ded9d9')
            Mod2.configure(state='disabled',background='#ded9d9')
            Internal1.configure(state='disabled',background='#ded9d9')
            Internal2.configure(state='disabled',background='#ded9d9')
            Internal3.configure(state='disabled',background='#ded9d9')
            Internal4.configure(state='disabled',background='#ded9d9')
            Memory1.configure(state='disabled',background='#ded9d9')
            Memory2.configure(state='disabled',background='#ded9d9')
            Memory3.configure(state='disabled',background='#ded9d9')
            Memory4.configure(state='disabled',background='#ded9d9')
            Cam1.configure(state='disabled',background='#ded9d9')
            Cam2.configure(state='disabled',background='#ded9d9')
            Cam3.configure(state='disabled',background='#ded9d9')
            Cam4.configure(state='disabled',background='#ded9d9')
            Comp1.configure(state='disabled',background='#ded9d9')
            Comp2.configure(state='disabled',background='#ded9d9')

            Cost1.configure(state='normal',background='#ded9d9',values=rows)
            Cost2.configure(state='normal',background='#ded9d9')

        else:
            pass

            
    def confirm2():

 
        if M_id2.get()=="COMPLETE_ENTRY":

            
            a3=M_id1.get()
            b3=Mod2.get()
            c3=Internal2.get()
            d3=Internal4.get()
            e3=Memory2.get()
            f3=Memory4.get()
            g3=Cam2.get()
            h3=Cam4.get()
            i3=Comp2.get()
            j3=Cost2.get()

            c3=c3 + d3
            e3=e3 + f3
            g3=g3 or h3

            cr=res.cursor()
            query_1='''UPDATE info
                                SET Name = %s , Storage = %s, Memory = %s, Camera_px = %s, Company = %s, Price = %s
                                WHERE Mobile_id = %s

                                        '''
            cr.execute(query_1,(b3.upper(),c3,e3,g3,i3.upper(),j3,a3,))
            res.commit()

            frame_7=Frame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
            frame_7.place(x=430,y=205,height=495,width=840)

            Upd=Label(frame_7, text="Updated Data           ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",28,'bold'),padx=20).place(x=250,y=11)

            frame_8=LabelFrame(frame_7,padx=10,bg="#4203c9",borderwidth=1)
            frame_8.place(x=20,y=70,height=334,width=790)
     
            M_id_=Label(frame_8, text="Mobile ID                    ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=10)
            
            Mod_=Label(frame_8, text="Model Name              ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=55)
            
            Internal_=Label(frame_8, text="Internal Storage  ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=100)
            
            Memory_=Label(frame_8, text="Memory                      ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=145)
            
            Cam_=Label(frame_8, text="Camera px                     ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=190)
            
            Comp_=Label(frame_8, text="Company                     ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=235)

            Cost_=Label(frame_8, text="Price                     ", fg="#e8d71e",bg='#4203c9',font=("ALGERIAN",20),padx=10).place(x=0,y=280)

            frame2=LabelFrame(frame_8, bd=1, bg="#4203c9")
            frame2.place(x=280, y=5, width=494, height=46)

            frame3=LabelFrame(frame_8, bd=1,relief=RIDGE , bg="#4203c9")
            frame3.place(x=280, y=51, width=494, height=46)

            frame4=LabelFrame(frame_8, bd=1 , bg="#4203c9")
            frame4.place(x=280, y=97, width=494, height=46)

            frame5=LabelFrame(frame_8, bd=1,relief=RIDGE , bg="#4203c9")
            frame5.place(x=280, y=143, width=494, height=46)

            frame6=LabelFrame(frame_8, bd=1 , bg="#4203c9")
            frame6.place(x=280, y=189, width=494, height=46)

            frame7=LabelFrame(frame_8, bd=1,relief=RIDGE , bg="#4203c9")
            frame7.place(x=280, y=235, width=494, height=46)

            frame8=LabelFrame(frame_8, bd=1, bg="#4203c9")
            frame8.place(x=280, y=281, width=494, height=46)


            cr=res.cursor()
            qr=" SELECT * FROM info WHERE Mobile_id=%s"
            cr.execute(qr,(a3,))
            rows=cr.fetchall()
            for y in rows:
                pass

            lb=Label(frame2, text= y[0], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()
            lb1=Label(frame3, text= y[1], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()
            lb2=Label(frame4, text= y[2], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()
            lb3=Label(frame5, text= y[3], fg="#e8d71e", bg="#4203c9",anchor=E,justify=LEFT, font=("Bell MT",18,"bold")).pack()
            lb4=Label(frame6, text= y[4], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()
            lb5=Label(frame7, text= y[5], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()
            lb6=Label(frame8, text= y[6], fg="#e8d71e", bg="#4203c9",anchor=E, justify=LEFT,font=("Bell MT",18,"bold")).pack()

            def ohk():
                frame_7.destroy()
                modify()
                
            btn_ok=Button(frame_7, text="OK",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=ohk).place(x=130,y=410,width=550)
            
            
            messagebox.showinfo("Update Successful","  Data successfully Modified,    ID No. :" + a3,parent=root)



        elif M_id2.get()=="PARTICULAR_VALUE":
            
            
                    ####
            a3=M_id1.get()
            b_o=Mod1.get()
            b_n=Mod2.get()
                   ####
            
            c_o=Internal1.get()
            c_o1=Internal3.get()
            d_n=Internal2.get()
            d_n1=Internal4.get()
            
            e_o=Memory1.get()
            e_o1=Memory3.get()
            f_n=Memory2.get()
            f_n1=Memory4.get()
            
            g_o=Cam1.get()
            g_o1=Cam3.get()
            h_n=Cam2.get()
            h_n1=Cam4.get()
            
                    ####           
            i_o=Comp1.get()
            i_n=Comp2.get()
                    ####
            j_0=Cost2.get()
            j_n=Cost2.get()
                    ####
            
            c_o=c_o + c_o1
            d_n=d_n + d_n1
            e_o=e_o + e_o1
            f_n=f_n + f_n1
            g_o=g_o or g_o1
            h_n=h_n or h_n1

            cr=res.cursor()
            if (M_id1.get()).lower()=='model_name':

                query_2='''UPDATE info
                                    SET Name = %s
                                    WHERE Name = %s
                                  '''

                cr.execute(query_2,(b_n.upper(),b_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Mod1.delete(0,END)
                Mod2.delete(0, END)
                Mod1.configure(state='disabled',background='#ded9d9')
                Mod2.configure(state='disabled',background='#ded9d9')
                
            elif (M_id1.get()).lower()=='internal_storage':
                query_3='''UPDATE info
                                    SET Storage = %s
                                    WHERE Storage = %s
                                  '''
                cr.execute(query_3,(d_n,c_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Internal1.delete(0,END)
                Internal2.delete(0, END)
                Internal3.delete(0,END)
                Internal4.delete(0,END)
                Internal1.configure(state='disabled',background='#ded9d9')
                Internal2.configure(state='disabled',background='#ded9d9')
                Internal3.configure(state='disabled',background='#ded9d9')
                Internal4.configure(state='disabled',background='#ded9d9')
                
            elif (M_id1.get()).lower()=='memory':
                query_4='''UPDATE info
                                    SET Memory = %s
                                    WHERE Memory = %s
                                  '''
                cr.execute(query_4,(f_n,e_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Memory1.delete(0,END)
                Memory2.delete(0, END)
                Memory3.delete(0,END)
                Memory4.delete(0,END)
                Memory1.configure(state='disabled',background='#ded9d9')
                Memory2.configure(state='disabled',background='#ded9d9')
                Memory3.configure(state='disabled',background='#ded9d9')
                Memory4.configure(state='disabled',background='#ded9d9')
                    
            elif (M_id1.get()).lower()=='camera_px':
                query_5='''UPDATE info
                                    SET Camera_px = %s
                                    WHERE Camera_px = %s
                                  '''
                cr.execute(query_5,(h_n,g_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Cam1.delete(0,END)
                Cam2.delete(0, END)
                Cam3.delete(0,END)
                Cam4.delete(0,END)
                Cam1.configure(state='disabled',background='#ded9d9')
                Cam2.configure(state='disabled',background='#ded9d9')
                Cam3.configure(state='disabled',background='#ded9d9')
                Cam4.configure(state='disabled',background='#ded9d9')
                    
            elif (M_id1.get()).lower()=='company':
                query_6='''UPDATE info
                                    SET Company = %s
                                    WHERE Company = %s
                                  '''
                cr.execute(query_6,(i_n.upper(),i_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Comp1.delete(0,END)
                Comp2.delete(0, END)
                Comp1.configure(state='disabled',background='#ded9d9')
                Comp2.configure(state='disabled',background='#ded9d9')

                
            elif (M_id1.get()).lower()=='price':
                query_7='''UPDATE info
                                    SET Price = %s
                                    WHERE Price = %s
                                  '''
                cr.execute(query_7,(j_n,j_o,))
                messagebox.showinfo("Update Successful","  Data successfully Modified",parent=root)
                Cost1.delete(0,END)
                Cost2.delete(0,END)
                Cost1.configure(state='disabled',background='#ded9d9')
                Cost2.configure(state='disabled',background='#ded9d9')

            else:
                pass
                
            res.commit()
            M_id1.delete(0,END)
            M_id2.delete(0,END)
            Mod1.delete(0,END)
            Mod2.delete(0, END)
            Internal1.delete(0,END)
            Internal2.delete(0, END)
            Internal3.delete(0,END)
            Internal4.delete(0,END)
            Memory1.delete(0,END)
            Memory2.delete(0, END)
            Memory3.delete(0,END)
            Memory4.delete(0,END)
            Cam1.delete(0,END)
            Cam2.delete(0, END)
            Cam3.delete(0,END)
            Cam4.delete(0,END)
            Comp1.delete(0,END)
            Comp2.delete(0, END)
            Cost1.delete(0,END)
            Cost2.delete(0,END)

        else:
            messagebox.showwarning(" Error","Incomplete Data , Please enter Complete Data",parent=root)

            




        
        
    def modify():
        
        global M_id1
        global M_id2
        global Mod1
        global Mod2
        global Internal1
        global Internal2
        global Internal3
        global Internal4
        global Memory1
        global Memory2
        global Memory3
        global Memory4
        global Cam1
        global Cam2
        global Cam3
        global Cam4
        global Comp1
        global Comp2
        global Cost1
        global Cost2

        s=ttk.Style(root)
        s.theme_use("winnative")
        
        frame_main3=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main3.place(x=430,y=205,height=495,width=840)

        Upd=Label(frame_main3, text="Update            ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=19)
        
        M_id1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=16,state='disabled',height=5)
        M_id1['values'] = ('MOBILE_ID::')
        M_id1.current(0)
        M_id1.place(x=351,y=19)
        
        
        M_id2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=17,background="#ded9d9")
        M_id2['values'] = ('COMPLETE_ENTRY','PARTICULAR_VALUE')
        M_id2.place(x=595,y=19)
        M_id2.bind("<<ComboboxSelected>>",select)
        
        
        Mod_=Label(frame_main3, text="Model Name                ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=19,y=74)
        Mod_1=Label(frame_main3, text="Old          ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=74)
        Mod1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=12,state='disabled',height=5)
        Mod1['values'] = ()
        Mod1.place(x=390,y=74)
        Mod_2=Label(frame_main3, text="New         ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=74)
        Mod2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=12,state='disabled',height=5)
        Mod2['values'] = ()
        Mod2.place(x=645,y=74)

        
        Internal_=Label(frame_main3, text="Internal Storage             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=129)
        Internal_1=Label(frame_main3, text="Old             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=129)
        Internal1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=6,state='disabled',height=5)
        Internal1['values'] = ()
        Internal1.place(x=390,y=129)
        Internal3=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Internal3['values'] = ("KB","MB","GB","TB")
        Internal3.place(x=480,y=129)
        Internal_2=Label(frame_main3, text="New         ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=129)
        Internal2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        Internal2['values'] = ()
        Internal2.place(x=645,y=129)
        Internal4=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Internal4['values'] = ("KB","MB","GB","TB")
        Internal4.place(x=735,y=129)
        
        
        Memory_=Label(frame_main3, text="Memory  ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=184)
        Memory_1=Label(frame_main3, text="Old             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=184)
        Memory1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=6,state='disabled',height=5)
        Memory1['values'] = ()
        Memory1.place(x=390,y=184)
        Memory3=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Memory3['values'] = ("KB","MB","GB","TB")
        Memory3.place(x=480,y=184)
        Memory_2=Label(frame_main3, text="New         ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=184)
        Memory2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        Memory2['values'] = ()
        Memory2.place(x=645,y=184)
        Memory4=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Memory4['values'] = ("KB","MB","GB","TB")
        Memory4.place(x=735,y=184)
        
        
        Cam_=Label(frame_main3, text="Camera px              ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=239)
        Cam_1=Label(frame_main3, text="Old             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=239)
        Cam1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled',height=5)
        Cam1['values'] = ()
        Cam1.place(x=390,y=239)
        Cam3=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=7,state='disabled')
        Cam3['values'] = ("Without_Camera")
        Cam3.place(x=448,y=239)
        Cam_2=Label(frame_main3, text="New             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=239)
        Cam2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Cam2['values'] = ()
        Cam2.place(x=645,y=239)
        Cam4=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=7,state='disabled')
        Cam4['values'] = ("Without_Camera")
        Cam4.place(x=703,y=239)
        
        Comp_=Label(frame_main3, text="Company                    ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=294)
        Comp_1=Label(frame_main3, text="Old             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=294)
        Comp1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=13,state='disabled',height=5)
        Comp1['values'] = ()
        Comp1.place(x=388,y=294)
        Comp_2=Label(frame_main3, text="New           ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=294)
        Comp2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=13,state='disabled')
        Comp2['values'] = ()
        Comp2.place(x=643,y=294)
        
        Cost_=Label(frame_main3, text="Price            ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=349)
        Cost_1=Label(frame_main3, text="Old             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=325,y=349)
        Cost1=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=13,state='disabled',height=5)
        Cost1['values'] = ()
        Cost1.place(x=390,y=349)
        Cost_2=Label(frame_main3, text="New            ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=575,y=349)
        Cost2=ttk.Combobox(frame_main3 ,font=("Calibri",14,"bold"),width=13,state='disabled')
        Cost2['values'] = ()
        Cost2.place(x=645,y=349)
        
        temp_13=Label(frame_main3,text="--------Enter the Mobile ID you wish to Update/Modify-------",bg="#4203c9",fg="#e8d71e",font=("Georgia",12)).place(x=180,y=460)

       
        Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Modify_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")
        Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
            



        btn_conf2=Button(frame_main3, text="MODIFY",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=confirm2).place(x=20,y=400)
        btn_rset2=Button(frame_main3, text="RESET",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=reset2).place(x=490,y=400)
#Delete function

    def detall():
        cr=res.cursor()

        response= messagebox.askyesno("Delete All ","Do You Really Want To Delete All The Data",parent=root)
        
        if response==1:
            qr_="DELETE FROM info"
        
            cr.execute(qr_)
            res.commit()
        else:
            pass



    def delet(b):

            x=M_id2.get()
            if x.lower()=='mobile_id':

                cr=res.cursor()
                qr_="SELECT Mobile_id FROM info"                
                cr.execute(qr_)
                rows=cr.fetchall()
                res.commit()

                Mod1.delete(0, END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Comp1.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)
                
                M_id1.configure(state='normal', values = rows)
                
                Mod1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Comp1.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')

            elif x.lower()=='model_name':

                cr=res.cursor()
                qr_="SELECT Name FROM info"                
                cr.execute(qr_)
                rows=cr.fetchall()
                res.commit()

                M_id1.delete(0,END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Comp1.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)

                Mod1.configure(state='normal',values = rows)

                M_id1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Comp1.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')

            elif x.lower()=='internal_storage':

                cr=res.cursor()
                qr_="SELECT Storage FROM info"                
                cr.execute(qr_)
                rows=cr.fetchall()
                res.commit()

                got=[]
                k=''
                for row in rows:
                    for i in row:
                        for j in i :
                           if j.isdigit()==True:
                               k=k + str(j) 
                           else:
                               got.append(k)
                               k=''

                M_id1.delete(0,END)
                Mod1.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Comp1.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)

                Internal1.configure(state='normal',values = got)
                Internal2.configure(state='normal')
                Internal3.configure(state='normal')

                M_id1.configure(state='disabled')
                Mod1.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Comp1.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')


            elif x.lower()=='memory':

                cr=res.cursor()
                qr_="SELECT Memory FROM info"                
                cr.execute(qr_)
                rows=cr.fetchall()
                res.commit()

                got=[]
                for row in rows:
                    for i in row:
                        for j in i :
                           if j.isdigit()==True:
                               got.append(j)
                           else:
                               pass
                    

                M_id1.delete(0,END)
                Mod1.delete(0, END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Comp1.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)

                Memory1.configure(state='normal',values=got)
                Memory2.configure(state='normal')
                Memory3.configure(state='normal')

                M_id1.configure(state='disabled')
                Mod1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Comp1.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')

            elif x.lower()=='camera_px':

                cr=res.cursor()
                query_="SELECT Camera_px FROM info"
                cr.execute(query_)
                rows = cr.fetchall()
                res.commit()

                M_id1.delete(0,END)
                Mod1.delete(0, END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Comp1.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)

                Cam1.configure(state='normal')
                Cam3.configure(state='normal')

                M_id1.configure(state='disabled')
                Mod1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Comp1.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')

            elif x.lower()=='company':

                cr=res.cursor()
                query_="SELECT Company FROM info"
                cr.execute(query_)
                rows = cr.fetchall()
                res.commit()

                M_id1.delete(0,END)
                Mod1.delete(0, END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Cost1.delete(0,END)
                Cost2.delete(0,END)

                Comp1.configure(state='normal')

                M_id1.configure(state='disabled')
                Mod1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Cost1.configure(state='disabled')
                Cost2.configure(state='disabled')

            else:

                cr=res.cursor()
                query_="SELECT Price FROM info"
                cr.execute(query_)
                rows = cr.fetchall()
                res.commit()


                M_id1.delete(0,END)
                Mod1.delete(0, END)
                Internal1.delete(0, END)
                Internal2.delete(0, END)
                Internal3.delete(0, END)
                Memory1.delete(0, END)
                Memory2.delete(0, END)
                Memory3.delete(0, END)
                Cam1.delete(0, END)
                Cam3.delete(0, END)
                Comp1.delete(0, END)

                Cost1.configure(state='normal')
                Cost2.configure(state='normal')

                M_id1.configure(state='disabled')
                Mod1.configure(state='disabled')
                Internal1.configure(state='disabled')
                Internal2.configure(state='disabled')
                Internal3.configure(state='disabled')
                Memory1.configure(state='disabled')
                Memory2.configure(state='disabled')
                Memory3.configure(state='disabled')
                Cam1.configure(state='disabled')
                Cam3.configure(state='disabled')
                Comp1.configure(state='disabled')

                

    def confirm4():

        cr=res.cursor()

        a=M_id1.get()
        b=Mod1.get()
        c1=Internal1.get()
        c2=Internal2.get()
        c3=Internal3.get()
        d1=Memory1.get()
        d2=Memory2.get()
        d3=Memory3.get()
        e1=Cam1.get()
        e3=Cam3.get()
        f=Comp1.get()
        g1=Cost1.get()
        g2=Cost2.get()
        v=M_id2.get()

        c1=c1+c3
        d1=d1+d3
        e1=e1 or e3
        
        if v.lower()=='mobile_id':
            cr=res.cursor()
            qr=''' DELETE FROM info
                      WHERE Mobile_id = %s '''
            
            cr.execute(qr,(a,))
            res.commit()

            messagebox.showinfo("Deleted","Entry Successfully Erased With, ID :" + a,parent=root)

        elif v.lower()=='model_name':

            qr="DELETE FROM info WHERE Name = %s"
            cr.execute(qr,(b,))
            res.commit()

            messagebox.showinfo("Deleted","Entry Successfully Erased With, MODEL NAME :" + b,parent=root)

        elif v.lower()=='internal_storage':

            if c2 == '<':
                qr="DELETE FROM info WHERE Storage < %s"
                cr.execute(qr,(c1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, INTERNAL STORAGE < :" + c1,parent=root)

            elif c2 == '>':

                qr="DELETE FROM info WHERE Storage > %s"
                cr.execute(qr,(c1,))
                res.commit()


                messagebox.showinfo("Deleted","Entry Successfully Erased With, INTERNAL STORAGE > :" + c1,parent=root)

            elif c2 == '=':
                
                qr="DELETE FROM info WHERE Storage = %s"
                cr.execute(qr,(c1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, INTERNAL STORAGE :" + c1,parent=root)

            else:
                messagebox.showerror("Error","Please Select From The Options Only",parent=root)

        elif v.lower()=='memory':

             if d2 == '<':
                qr="DELETE FROM info WHERE Memory < %s"
                cr.execute(qr,(d1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, MEMORY < :" + d1, parent=root)

             elif d2 == '>':

                qr="DELETE FROM info WHERE Memory > %s"
                cr.execute(qr,(d1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, MEMORY > :" + d1, parent=root)

             elif d2 == '=':
                
                qr="DELETE FROM info WHERE Memory = %s"
                cr.execute(qr,(d1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, MEMORY :" + d1, parent=root)

             else:
                messagebox.showerror("Error","Please Select From The Options Only",parent=root)

        elif v.lower()=='camera_px':

            qr="DELETE FROM info WHERE Camera_px = %s"
            cr.execute(qr,(e1,))
            res.commit()

            messagebox.showinfo("Deleted","Entry Successfully Erased With, CAMERA Pix. :" + e1, parent=root)

        elif v.lower()=='company':

            qr="DELETE FROM info WHERE Company = %s"
            cr.execute(qr,(f,))
            res.commit()

            messagebox.showinfo("Deleted","Entry Successfully Erased With, COMPANY :" + f, parent=root)

        else:

             if g2 == '<':
                qr="DELETE FROM info WHERE Price < %s"
                cr.execute(qr,(g1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, PRICE < :" + g1, parent=root)

             elif g2 == '>':

                qr="DELETE FROM info WHERE Price > %s"
                cr.execute(qr,(g1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, PRICE > :" + g1,  parent=root)

             elif g2 == '=':
                
                qr="DELETE FROM info WHERE Price = %s"
                cr.execute(qr,(g1,))
                res.commit()

                messagebox.showinfo("Deleted","Entry Successfully Erased With, PRICE :" + g1,  parent=root)

             else:
                messagebox.showerror("Error","Please Select From The Options Only",parent=root)

        M_id1.delete(0,END)
        M_id2.delete(0,END)
        Mod1.delete(0, END)
        Internal1.delete(0, END)
        Internal2.delete(0, END)
        Internal3.delete(0, END)
        Memory1.delete(0, END)
        Memory2.delete(0, END)
        Memory3.delete(0, END)
        Cam1.delete(0, END)
        Cam3.delete(0, END)
        Comp1.delete(0, END)
        Cost1.delete(0,END)
        Cost2.delete(0,END)


                
    def erase():

        global M_id1
        global M_id2
        global Mod1
        global Internal1
        global Internal2
        global Internal3
        global Memory1
        global Memory2
        global Memory3
        global Cam1
        global Cam3
        global Comp1
        global Cost1
        global Cost2

        
        
        frame_main4=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main4.place(x=430,y=205,height=495,width=840)

        s=ttk.Style(root)
        s.theme_use("winnative")

        M_id_=Label(frame_main4, text="Mobile ID                    ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=19)
        M_id1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=16,state='disabled',height=5)
        M_id1['values'] = ()
        M_id1.place(x=360,y=19)

        M_id2=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=17,background="#ded9d9")
        M_id2['values'] = ('Mobile_Id'  , 'Model_Name'  , 'Internal_Storage'  , 'Memory'  , 'Camera_px' ,  'Company'  ,'Price')
        M_id2.place(x=593,y=19)
        M_id2.bind("<<ComboboxSelected>>",delet)

        Mod_=Label(frame_main4, text="Model Name                ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=19,y=74)
        Mod1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=40,state='disabled',height=5)
        Mod1['values'] = ()
        Mod1.place(x=360,y=74)

        Internal_=Label(frame_main4, text="Internal Storage             ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=129)
        Internal1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=23,state='disabled',height=5)
        Internal1['values'] = ()
        Internal1.place(x=430,y=129)
        Internal2=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Internal2['values'] = ("<",">","=")
        Internal2.place(x=360,y=129)
        Internal3=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        Internal3['values'] = ("KB","MB","GB","TB")
        Internal3.place(x=702,y=129)
        

        Memory_=Label(frame_main4, text="Memory  ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=184)
        Memory1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=23,state='disabled',height=5)
        Memory1['values'] = ()
        Memory1.place(x=430,y=184)
        Memory2=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Memory2['values'] = ("<",">","=")
        Memory2.place(x=360,y=184)
        Memory3=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=6,state='disabled')
        Memory3['values'] = ("KB","MB","GB","TB")
        Memory3.place(x=702,y=184)

        Cam_=Label(frame_main4, text="Camera px              ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=239)
        Cam1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=17,state='disabled',height=5)
        Cam1['values'] = ()
        Cam1.place(x=360,y=239)
        
        Cam3=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=19,state='disabled')
        Cam3['values'] = ("Without_Camera")
        Cam3.place(x=571,y=239)

        Comp_=Label(frame_main4, text="Company                    ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=294)
        Comp1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=40,state='disabled',height=5)
        Comp1['values'] = ()
        Comp1.place(x=360,y=294)

        Cost_=Label(frame_main4, text="Price            ",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20),padx=20).place(x=0,y=349)
        Cost1=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=33,state='disabled',height=5)
        Cost1['values'] = ()
        Cost1.place(x=430,y=349)
        Cost2=ttk.Combobox(frame_main4 ,font=("Calibri",14,"bold"),width=3,state='disabled')
        Cost2['values'] = ("<",">","=")
        Cost2.place(x=360,y=349)
        
        temp_24=Label(frame_main4,text="--------Enter the Mobile ID you wish to Delete/Erase-------",bg="#4203c9",fg="#e8d71e",font=("Georgia",12)).place(x=180,y=460)

        Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Delete_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")
        Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")

        btn_conf3=Button(frame_main4, text="DELETE",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=18,borderwidth=5,padx=20,command=confirm4).place(x=20,y=400)
        btn_deta3=Button(frame_main4, text="DELETE ALL",fg="white",cursor='hand2',bg="black" ,font=("Georgia",18),width=18,borderwidth=5,padx=20,command=detall).place(x=490,y=400)

        messagebox.showinfo("Info","  Please Select The Related Field According To Which You Want To Delete Entries",parent=frame_main4)

# VIEW FINCTION::

    def select3(e):
       
        z=field_.get()

        if z.lower() == "mobile_id" :

            cr=res.cursor()
            query_="SELECT Mobile_id FROM info"
            cr.execute(query_)
            rows = cr.fetchall()
                    
            Detail_.configure(state='normal',values = rows)
                
        elif z.lower() == "model_name":
            
            cr=res.cursor()
            query_="SELECT Name FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

        elif z.lower() == "internal_storage":
            
            cr=res.cursor()
            query_="SELECT Storage FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

        elif z.lower() == "memory":
            
            cr=res.cursor()
            query_="SELECT Memory FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

        elif z.lower() == "camera_px":
            
            cr=res.cursor()
            query_="SELECT Camera_px FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

        elif z.lower() == "company":
            
            cr=res.cursor()
            query_="SELECT Company FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

        else:

            cr=res.cursor()
            query_="SELECT Company FROM info"
            cr.execute(query_)
            rows = cr.fetchall()

            Detail_.configure(values = rows)

                            


    def view():

        global field_
        global Detail_
        frame_main6=LabelFrame(root,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main6.place(x=430,y=205,height=495,width=840)

        field=Label(frame_main6, text="FIELD :",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=20,y=20)
        field_=ttk.Combobox(frame_main6, font=("Calibri",14,"bold"),width=12,height=5)
        field_['values'] = ('Mobile_Id'  , 'Model_Name'  , 'Internal_Storage'  , 'Memory'  , 'Camera_px' ,  'Company'  ,'Price')
        field_.place(x=112,y=20)
        field_.bind("<<ComboboxSelected>>",select3)

        Detail=Label(frame_main6, text="DETAILS :",bg='#4203c9',fg="#e8d71e",font=("ALGERIAN",20)).place(x=340,y=20)
        Detail_=ttk.Combobox(frame_main6, font=("Calibri",14,"bold"),width=30,height=5)
        Detail_['values'] = ()
        Detail_.place(x=468,y=20)
              

        def seeall():
        
            cr=res.cursor()
            sql="SELECT * FROM info"
            cr.execute(sql)
            rows=cr.fetchall()
            total=cr.rowcount

            s=ttk.Style(root)
            s.theme_use("winnative")
            s.configure(".", font=("Calibri",11))
            s.configure("Treeview.Heading", foreground ='red',background='#babbc1', font=("ALGERIAN",12,'bold'))

            mobiletable.tag_configure('oddrow', background="#e9e9e9")
            mobiletable.tag_configure('evenrow', background="lightblue")

            for record in mobiletable.get_children():
                mobiletable.delete(record)

            Detail_.delete(0,END)
            field_.delete(0,END)
            
            mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))
            if total==0:
                messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
            else:
                count=0
                messagebox.showinfo("Found"," No. of Entries Found : " + str(total),parent=root)
                for i in rows:
                    if count%2==0:
                        mobiletable.insert('', 'end' , values=i, tags=('evenrow',))
                    else:
                        mobiletable.insert('', 'end' , values=i, tags=('oddrow',))
                    count=count+1

        def Get():
            z=field_.get()
            try  :
                if z.lower() == "mobile_id" :
                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Mobile_id = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))
                    
                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1
                elif z.lower() == "model_name":
               
                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Name = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count = count+1
                
                elif z.lower() == "internal_storage":

                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Storage = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count = count+1

                elif z.lower() == "memory":

                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Memory = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1

                elif z.lower() == "camera_px":

                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Camera_px = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1

                elif z.lower() == "company":

                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Company = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                        
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1

                else:

                    for record in mobiletable.get_children():
                        mobiletable.delete(record)
                    
                    r=Detail_.get()

                    cr=res.cursor()
                    query_="SELECT * FROM info WHERE Price = %s"
                    cr.execute(query_,(r,))
                    rows = cr.fetchall()
                    total=cr.rowcount

                    mobiletable.insert('', 'end' , values=(' ', ' ', ' ', ' ', ' ', ' ', ' '))

                    if total==0:
                        messagebox.showinfo("Nothing Here"," No Data Available In Database To Display",parent=root)
                    else:
                        messagebox.showinfo("Rows Effected"," No. Of Entries Found : " + str(total) ,parent=root)
                    count=0
                    for i in rows:
                     
                        if count%2==0:
                            mobiletable.insert('', 'end' , values=i,tags=('evenrow',))
                        else:
                            mobiletable.insert('', 'end' , values=i,tags=('oddrow',))
                        count=count+1
                        
            except:
                
                messagebox.showinfo("Empty"," Please Select The Field And Details : " + str(total) ,parent=root)

                

        tableframe=Frame(frame_main6, bd=5, relief=RIDGE, bg='#031163')
        tableframe.place(x=3,y=140,height=330, width=816)

        scrollx=Scrollbar(tableframe, orient=HORIZONTAL)
        scrolly=Scrollbar(tableframe, orient=VERTICAL)
        mobiletable=ttk.Treeview(tableframe, columns=(1,2,3,4,5,6,7),height=5, xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        mobiletable.column(1, width= 130 ,minwidth=130, anchor=CENTER)
        mobiletable.column(2, width= 150,minwidth=150, anchor=CENTER)
        mobiletable.column(3, width= 190,minwidth=190, anchor=CENTER)
        mobiletable.column(4, width= 120,minwidth=120, anchor=CENTER)
        mobiletable.column(5, width= 130,minwidth=130, anchor=CENTER)
        mobiletable.column(6, width= 150, minwidth=150, anchor=CENTER)
        mobiletable.column(7, width= 100,minwidth=100, anchor=CENTER)

        scrollx.configure(command=mobiletable.xview)
        scrolly.configure(command=mobiletable.yview)
        mobiletable.heading(1,text="MOBILE ID")
        mobiletable.heading(2,text="MODEL NAME")
        mobiletable.heading(3,text="INTERNAL STORAGE")
        mobiletable.heading(4,text="MEMORY")
        mobiletable.heading(5,text="CAMERA Px.")
        mobiletable.heading(6,text="COMPANY")
        mobiletable.heading(7,text="PRICE")
        mobiletable[  'show' ] = ' headings '
        mobiletable.pack(fill=BOTH, expand=1)

        s=ttk.Style(root)
        s.theme_use("winnative")

        s.configure(".", font=("Calibri",11))
        s.configure("Treeview.Heading", foreground ='red',background='#babbc1', font=("ALGERIAN",12,'bold'),fieldbackground='#D3D3D3')
        s.map ('Treeview',background=[('selected','blue')])

        mobiletable.tag_configure('oddrow', background="#e9e9e9")
        mobiletable.tag_configure('evenrow', background="lightblue")

        search_btn=Button(frame_main6, text="SEARCH",fg="white",bg="black" ,cursor='hand2',font=("Georgia",18),width=25,borderwidth=5,command=Get)
        search_btn.place(x=20,y=75)

        seeall_btn=Button(frame_main6, text="VIEW ALL",fg="white",bg="black",cursor='hand2' ,font=("Georgia",18),width=25,borderwidth=5,command=seeall)
        seeall_btn.place(x=435,y=75)



        Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Gallery_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        View_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")



#Gallery function

    def resize_image(frame_main5,image,label1):
        
        new_height=453
        new_width=706
        image1=image.resize((new_width,new_height))
        photo=ImageTk.PhotoImage(image1)
        label1.configure(image=photo)
        label1.image=photo

    def Next():
        
        global n
        global items_list
        n = (n + 1) % len(items_list)
        
        img1=items_list[n]
        image=Image.open('./pics/'+img1)
        photo=ImageTk.PhotoImage(image)

        label1=Label(frame_main5,image=photo)
        label1.bind('<configure>',resize_image(frame_main5,image,label1))
        label1.place(x=57,y=10)


    def previous():
        global n
        global items_list
        
        n = (n - 1) % len(items_list)
        img1=items_list[n]
        image=Image.open('./pics/'+img1)
        photo=ImageTk.PhotoImage(image)

        label1=Label(frame_main5,image=photo)
        label1.bind('<configure>',resize_image(frame_main,image,label1))
        label1.place(x=57,y=10)

    def galry():

        global n
        global items_list
        global label1
        global frame_main5
        
        
        frame_main5=LabelFrame(root,bg="#4203c9",borderwidth=8, relief=RIDGE)
        frame_main5.place(x=430,y=205,height=495,width=840)
        
        n=0

        items_list=os.listdir('./pics')

        img1=items_list[n]

        image=Image.open('./pics/'+img1)
        copy_of_image=image
        photo=ImageTk.PhotoImage(image)

        label1=Label(frame_main5,image=photo)
        label1.bind('<configure>',resize_image(frame_main5,copy_of_image,label1))
        label1.place(x=57,y=10)

        b1=Button(frame_main5,text=">>",width=5,height=25,bd=5,bg="black",fg="white",cursor='hand2',command=Next)
        b1.place(x=774,y=45)

        b2=Button(frame_main5,text="<<",width=5,height=25,bd=5,bg="black",fg="white",cursor='hand2',command=previous)
        b2.place(x=0,y=45)



        Enter_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Search_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Modify_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Delete_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")
        Gallery_btn.configure(relief=SUNKEN,bg="#0472e8",fg="black")
        View_btn.configure(relief=RAISED,bg="#031163",fg="#1fbfb8")

    frame_main=LabelFrame(root,padx=10,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
    frame_main.place(x=430,y=205,height=495,width=840,bordermode=OUTSIDE)

    logo=Image.open("logo5.png")
    resized=logo.resize((780,445), Image.LANCZOS)
    R_logo=ImageTk.PhotoImage(resized)
    lbl=Label(frame_main, image=R_logo)
    lbl.place(x=10,y=10)
 


    frame_connect=LabelFrame(root,padx=10,pady=5,bg="#4203c9",borderwidth=8, relief=RIDGE)
    frame_connect.place(x=490,y=100)
    btn_1L=Label(frame_connect,text="Click here to connect::",fg="#e8d71e",bg="#4203c9",font=("Ravie",16)).grid(row=3, column=3)
    btn1=Button(frame_connect, text="LOGIN TO DATABASE",fg="white",bg="#031163" ,cursor='hand2',font=("Georgia",22),borderwidth=5,command=connect).grid(row=3, column=4,padx=20)


   #BUTTONS

    Enter_btn1=Button(root, text="REGISTRATION",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=create)
    Enter_btn1.place(x=30,y=120)
    Search_btn1=Button(root, text="SEARCH ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=search)
    Search_btn1.place(x=30,y=205)
    Modify_btn1=Button(root, text="MODIFY ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=modify)
    Modify_btn1.place(x=30,y=290)
    Delete_btn1=Button(root, text="DELETE ",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=erase)
    Delete_btn1.place(x=30,y=375)
    View_btn1=Button(root, text="VIEW DETAILS",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=view)
    View_btn1.place(x=30,y=460)
    Gallery_btn1=Button(root, text="GALLERY",fg="#1fbfb8",bg="#031163" ,width=20,font=("Snap ITC",15),padx=15,pady=8,state=DISABLED,borderwidth=5,command=galry)
    Gallery_btn1.place(x=30,y=545)
    exit_btn1=Button(root, text="HOME",fg="#1fbfb8",bg="#031163" ,width=20,cursor='hand2',font=("Snap ITC",15),activebackground="#0472e8",padx=15,pady=8,borderwidth=5,command=exit)
    exit_btn1.place(x=30,y=630)

    
    root.mainloop()


abt_btn=Button(root_1,text="ABOUT US",fg="red",bg="yellow" ,width=14,cursor='hand2',font=("Verdana",18,'bold'),activebackground="#f5d269",padx=5,pady=5,bd=6,command=info)
abt_btn.place(x=505,y=210)

exit_btn=Button(root_1,text="EXIT",fg="red",bg="yellow" ,width=14,cursor='hand2',font=("Verdana",18,'bold'),activebackground="#f5d269",padx=5,pady=5,borderwidth=6,command=Exit)
exit_btn.place(x=845,y=260)

open_btn=Button(root_1,text="  MAIN MENU  ",fg="red",bg="yellow" ,width=16,cursor='hand2',font=("Verdana",18,'bold'),activebackground="#f5d269",padx=5,pady=5,borderwidth=6,command=start)
open_btn.place(x=145,y=155)


root_1.mainloop()


