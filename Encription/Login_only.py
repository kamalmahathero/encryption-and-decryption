from tkinter import *
from tkinter import messagebox
import tkinter as tk
from cryptography.fernet import Fernet



root=Tk()
root.title("Encrypt Decrypt Login")
root.geometry("925x500+300+200")
root.resizable(False,False)
root.configure(bg="#fff")

###This is Login page######
def signin():
    username=user.get()
    password=code.get()
    
    if username =='test' and password=="test":
        screen=Toplevel(root)
        screen.title("Message ENcode and Decode")
        screen.geometry("500x300+300+200")
        screen.config(bg="white")
        screen.resizable(False,False)
        
        Label(screen, text="Encode / Decode",bg= '#fff', font=("Calibri(Body)",20,'bold')).pack()
        
        screen.mainloop()
    elif username!='test' and password!='test':
        messagebox.showerror('Invalid',"Invalid username or password")
    elif password!='test':
        messagebox.showerror('Invalid',"Invalid password ")
    elif username!='test':
        messagebox.showerror('Invalid',"Invalid  username")
    
    
    
    
    
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


sign_in= Button(frame,width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg="#57a1f8")
sign_in.place(x=215, y=270)
######Login finish###############

root.mainloop()