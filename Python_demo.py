import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = pass_input.get()

    if email == 'prasanna@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    elif email == 'ganesh142008@gmail.com' and password == 'cheppanura':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')

root = tk.Tk()
root.configure(background='#0096DC')
root.title("Login Form")
root.minsize(400,400)
root.iconbitmap('calculator-favicon.ico')
root.geometry('400x400')
img = Image.open('flipkart-logo-39911.png')
resized_img = img.resize((200,100))
img=ImageTk.PhotoImage(resized_img)
img_label = tk.Label(root, image=img)
img_label.pack(pady=(10,10))
#added pading
text_label = tk.Label(root, text='Flipkart', font=("Arial", 16), fg='white',bg='#0096DC')
text_label.pack()

email_label = tk.Label(root, text='Enter email', font=("Arial", 16), fg='white', bg='#0096DC')
email_label.pack(fill="x")

email_input = tk.Entry(root, width=50)
email_input.pack()

pass_label = tk.Label(root, text='Enter pwd', font=("Arial", 16), fg='white', bg='#0096DC')
pass_label.pack(fill="x")

pass_input = tk.Entry(root, width=50,show="*")
pass_input.pack()

Login_btn = tk.Button(root,text='Login here',bg='white',fg='black',command=handle_login)
Login_btn.pack(pady = (10,20))

root.mainloop()