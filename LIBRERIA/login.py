import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import *
from empleado import ventana_empleado
from administrador import ventana_administrador

def login(entry_usuario: tk.Entry, entry_contraseña: tk.Entry, ventana1: tk.Tk):
    usuario=entry_usuario.get()
    contraseña=entry_contraseña.get()
    
    try:
        mysqlConn=mysql.connector.connect(host='localhost', user='root', password='', database='libreria')
        cursor=mysqlConn.cursor()

        cursor.execute(f"SELECT * from usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}'")  
        
        usuario=cursor.fetchone()

        if usuario:
            if usuario[5] == "administrador":
                messagebox.showinfo("Login exitoso", "Bienvenido al menu de administrador")
                ventana1.destroy()
                ventana_administrador()
            else:
                messagebox.showinfo("Login exitoso", "Bienvenido al menu de empleado")
                ventana1.destroy()
                ventana_empleado()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"Error: {error}")

def ventana_login():

    ventana1=tk.Tk()
    ventana1.title("Login")
    ventana1.geometry("400x250")
    ventana1.configure(bg="#2980b9")

    label1=tk.Label(ventana1, text="Login", font=("Lexend",16,"bold"), bg="#2980b9", fg="#d6eaf8")
    label1.place(x=150, y=5)

    label_usuario=tk.Label(ventana1, text="Usuario", font=("Lexend",10,"bold"), bg="#2980b9", fg="#d6eaf8")
    label_usuario.place(x=100, y=40)

    label_contraseña=tk.Label(ventana1, text="Contraseña", font=("Lexend",10,"bold"), bg="#2980b9", fg="#d6eaf8")
    label_contraseña.place(x=100, y=100)

    entry_usuario=tk.Entry(ventana1, width=30)
    entry_usuario.place(x=100, y=65)

    entry_contraseña=tk.Entry(ventana1, show="*", width=30)
    entry_contraseña.place(x=100, y=125)

    button_usuario=tk.Button(ventana1, text="Acceder", command=lambda: login(entry_usuario=entry_usuario, entry_contraseña=entry_contraseña, ventana1=ventana1), width=25, relief="raised", bg="#d6eaf8")
    button_usuario.place(x=100, y=160)

    ventana1.bind('<Return>', lambda event: button_usuario.invoke())

    ventana1.mainloop()