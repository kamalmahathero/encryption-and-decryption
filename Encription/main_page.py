from tkinter import *
from tkinter import messagebox
import ast
import tkinter as tk
from cryptography.fernet import Fernet
import base64
import hashlib
from datetime import datetime, timedelta


from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(app, default_limits=["30 per minute"])
@app.route('/')
@limiter.limit("30/minute")
def index():
    return"!"
if __name__ == '__main__':
    app.run()


root=Tk()
root.title("Encrypt Decrypt Login")
root.geometry("925x500+300+200")
root.resizable(False,False)
root.configure(bg="#fff")



###This is Login page######
def signin():
    username=user.get()
    password=code.get()
    
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    #print(r.keys())
    #print(r.values())
    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Message ENcode and Decode")
        screen.geometry("500x300+300+200")
        screen.config(bg="white")
        screen.resizable(False,False)
        
        Label(screen, text="Encode / Decode",bg= '#fff', font=("Calibri(Body)",20,'bold')).pack()
        Label(screen,text='Keep a secret message!', font='System 10 bold').pack(side=BOTTOM)
        
        Text= StringVar()
        private_key = StringVar()
        mode= StringVar()
        Result= StringVar()
        
        def Encode(key,message):
            enc = []
            
            for i in range(len(message)):
                key_c = key[i % len(key)]
                enc.append(chr((ord(message[i])+ ord(key_c)) % 256))
            return base64.urlsafe_b64encode("".join(enc).encode()).decode()
        def Decode(key, message):
            dec =[]
            message= base64.urlsafe_b64decode(message).decode()
            
            for i in range(len(message)):
                key_c=key[i % len(key)]
                dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
            return "".join(dec)
        
        def Mode():
            if(mode.get() == 'e'):
                Result.set(Encode(private_key.get(), Text.get()))
            elif(mode.get() == 'd'):
                Result.set(Decode(private_key.get(), Text.get()))
            else:
                Result.set('Invalid Mode')
                
        def Exit():
                screen.destroy()
                
        def Reset():
            Text.set("")
            private_key.set("")
            mode.set("")
            Result.set("")
            
        Label(screen, font= 'Roboto 12', text='Message').place(x=60, y=60)
        Entry(screen, font='roboto 10', textvariable= Text,bg='ghost white').place(x=290,y=60)
        
        Label(screen, font= 'Roboto 12', text='Key').place(x=60, y=90)
        Entry(screen, font='roboto 10', textvariable= private_key,bg='ghost white').place(x=290,y=90)
                
        Label(screen, font= 'Roboto 12', text='MODE(e-encode, d-decode)').place(x=60, y=120)
        Entry(screen, font='roboto 10', textvariable= mode,bg='ghost white').place(x=290,y=120)
             
        Entry(screen, font='roboto 10', textvariable= Result,bg='ghost white',width=52).place(x=65,y=150)

        Button(screen,font='Roboto 10 bold',bd=0,text='Encrypt / Decrypt', padx=10, pady=2, bg='LimeGreen', fg='white', command=Mode).place(x=65, y=200)
        Button(screen,font='Roboto 10 bold',bd=0,width=6,text='Reset', padx=2, pady=2, bg='Red', fg='white', command=Reset).place(x=300, y=200)
        Button(screen,font='Roboto 10 bold',bd=0,text='Exit', padx=2, pady=2, bg='orange', fg='white', command=Exit).place(x=375, y=200)
        
        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'Invalid usrname or password')
    
def signup_command():
    window=Toplevel(root)
    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.resizable(False,False)
    window.configure(bg="#fff")

    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()
    
        if password==confirm_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                dict2={username:hashed_password}
                r.update(dict2)
                file.truncate(0)
                file.close()
            
                file=open('datasheet.txt', 'w')
                w=file.write(str(r))
            
                messagebox.showinfo('Signup',"Sucessfully sign up")
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Both Password should match")
    def sign():
        window.destroy()       
        
    
    img = PhotoImage(file='D:\Semester 3\Programming\Course_work_2\signup.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)
    
    frame=Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480,y=50)
    
    heading=Label(frame,text="Sign up", fg='#57a1f8', bg="white", font=("Microsoft YaHei UI Light",23,'bold'))
    heading.place(x=100,y=5)

    #Username
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name =='':
            user.insert(0, 'Username')
    user=Entry(frame,width=25, fg="black", border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    user.place(x=30,y=80)
    user.insert(0, "Username")
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>', on_leave)


    Frame(frame,width=295, height=2, bg="black").place(x=25,y=107)

    #Password
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() =='':
            code.insert(0, 'Password')

    code=Entry(frame,width=25, fg="black", border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    code.place(x=30,y=150)
    code.insert(0, "Password")
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295, height=2, bg="black").place(x=25,y=177)

    #Repassword
    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        if confirm_code.get() =='':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code=Entry(frame,width=25, fg="black", border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0, "Confirm Password")
    confirm_code.bind('<FocusIn>',on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295, height=2, bg="black").place(x=25,y=247)


    #Sign up Button
    Button(frame,width=39,pady=7, text="Sign Up",bg="#57a1f8",fg="white",border=0, command=signup).place(x=35,y=280)
    label=Label(frame,text="I have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=90, y=340)



    sign_up= Button(frame,width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg="#57a1f8",command=sign)
    sign_up.place(x=200, y=340)




    window.mainloop()

img = PhotoImage(file='C:/Users/romes/OneDrive/Documents/Encription decriptiion/Encription/login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text="ENCRYPT / DECRYPT \nLOGIN ", fg='#57a1f8', bg="white", font=("Times New Romans",23,'bold'))
heading.place(x=30,y=1)

#Username
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0, 'Username')
user=Entry(frame,width=25, fg="black", border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0, "Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=107)

#password
def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e):
    name=code.get()
    if name =='':
        code.insert(0, 'Password')


code=Entry(frame,width=25, fg="black", border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0, "Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=177)

#Button
Button(frame,width=39,pady=7, text="Sign In",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204) #when sign in click 
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75, y=270)


sign_in= Button(frame,width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg="#57a1f8",command=signup_command)
sign_in.place(x=215, y=270)
######Login finish###############

root.mainloop()