import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *

def ventana_administrador():
   
    root = tk.Tk()
    root.geometry("1000x500")
    root.config(bg="#2980b9")

    tk.Label(root,text="ADMINISTRAR EMPLEADOS",font=("lexend",20,"bold"),bg="#2980b9",fg="#d6eaf8").place(x=250,y=0)

    labelid = tk.Label(root, text="ID", font=("Arial", 12, "bold"),bg="#2980b9",fg="#d6eaf8")
    labelid.place(x=250, y=50)

    labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12, "bold"),bg="#2980b9",fg="#d6eaf8")
    labelnombre.place(x=250, y=80)

    labelapellido = tk.Label(root, text="Apellido", font=("Arial", 12, "bold"),bg="#2980b9",fg="#d6eaf8")
    labelapellido.place(x=250, y=110)

    labelusuario = tk.Label(root, text="Usuario", font=("Arial", 12, "bold"),bg="#2980b9",fg="#d6eaf8")
    labelusuario.place(x=250, y=140)

    labelcontraseña = tk.Label(root, text="Contraseña", font=("Arial", 12, "bold"),bg="#2980b9",fg="#d6eaf8")
    labelcontraseña.place(x=250, y=170)

    identificador = tk.Entry(root, relief="flat")
    identificador.place(x=370, y=50)
    identificador.config(state="readonly")

    name = tk.Entry(root)
    name.place(x=370, y=80)

    lastname = tk.Entry(root)
    lastname.place(x=370, y=110)

    user = tk.Entry(root)
    user.place(x=370, y=140)

    password = tk.Entry(root)
    password.place(x=370, y=170)

    tk.Button(root,text="Crear",command=lambda: add(identificador=identificador, name=name, lastname=lastname, user=user, password=password, listbox=listbox),  width=10, font=("Arial",12),bg="#b4c5e4").place(x=550,y=50)
    tk.Button(root,text="Editar",command=lambda: update(identificador=identificador, name=name, lastname=lastname, user=user, password=password, listbox=listbox), width=10, font=("Arial",12),bg="#b4c5e4").place(x=550,y=100)
    tk.Button(root,text="Eliminar",command=lambda: delete(identificador=identificador, name=name, lastname=lastname, user=user, password=password, listbox=listbox),  width=10, font=("Arial",12),bg="#ff6978").place(x=550,y=150)
    tk.Button(root,text="Salir",command=lambda: salir(root=root), width=10, font=("Arial",12),bg="#48c9b0").place(x=850,y=50)


    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña")
    listbox = ttk.Treeview(root,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=230)
    
    mostrar(listbox)
    listbox.bind("<Double-Button-1>",lambda event: obtener(listbox, identificador=identificador,name=name,lastname=lastname,user=user,password=password))

    root.mainloop()

def salir(root: tk.Tk):
    from login import ventana_login
    root.destroy()
    ventana_login()

def add(identificador, name, lastname, user, password, listbox):
    
    nameAdd = name.get()
    lastnameAdd = lastname.get()
    userAdd = user.get()
    passwordAdd = password.get()
    rolAdd = "empleado"

    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="libreria")
    micursos=mysqlC.cursor()
    try:

        micursos.execute(f"insert into usuarios(nombre,apellido,usuario,contraseña,rol) values('{nameAdd}','{lastnameAdd}','{userAdd}','{passwordAdd}','{rolAdd}')")
        mysqlC.commit()
        name.delete(0,END)
        lastname.delete(0,END)
        user.delete(0, END)
        password.delete(0,END)
        identificador.config(state="normal")
        identificador.delete(0, END)
        identificador.config(state="readonly")
        messagebox.showinfo("informacion","Usuario agregado")
        actualizar(listbox)
    except mysql.connector.Error as error:
        if error.errno == 1062:
            messagebox.showerror("Error",f"Error: El nombre de usuario '{userAdd}' ya existe.")
        else: 
            messagebox.showerror("Error de conexión", f"Error: {error}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        mysqlC.rollback()
        mysqlC.close()

def update(identificador, name, lastname, user, password, listbox):
    idUpd = identificador.get()
    nameUpd = name.get()
    lastnameUpd = lastname.get()
    userUpd = user.get()
    passwordUpd = password.get()

    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="libreria")
    micursos=mysqlC.cursor()
    try:

        micursos.execute(f"UPDATE usuarios set nombre='{nameUpd}',apellido='{lastnameUpd}',usuario='{userUpd}',contraseña='{passwordUpd}' where id={idUpd}")
        mysqlC.commit()
        name.delete(0,END)
        lastname.delete(0,END)
        user.delete(0, END)
        password.delete(0,END)
        identificador.config(state="normal")
        identificador.delete(0, END)
        identificador.config(state="readonly")
        messagebox.showinfo("informacion","Usuario editado")
        actualizar(listbox)
    except mysql.connector.Error as error:
        if error.errno == 1062:
            messagebox.showerror("Error",f"Error: El nombre de usuario '{userUpd}' ya existe.")
        else: 
            messagebox.showerror("Error de conexión", f"Error: {error}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        mysqlC.rollback()
        mysqlC.close()

def delete(identificador, name, lastname, user, password, listbox):
    id = identificador.get()
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="libreria")
    micursos=mysqlC.cursor()
    try:
        micursos.execute(f"DELETE FROM USUARIOS WHERE id={id}")
        mysqlC.commit()
        name.delete(0,END)
        lastname.delete(0,END)
        user.delete(0, END)
        password.delete(0,END)
        identificador.config(state="normal")
        identificador.delete(0, END)
        identificador.config(state="readonly")
        messagebox.showinfo("informacion","usuario eliminado")
        actualizar(listbox)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        mysqlC.rollback()
        mysqlC.close()

def actualizar(listbox):
    
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar(listbox)

def mostrar(listbox):
    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="libreria")
    micursor=mysqlC.cursor()
    

    micursor.execute("select id, nombre, apellido, usuario, contraseña from usuarios WHERE rol='empleado'")

    lista = micursor.fetchall()
    
    for i,(id,nombre,apellido,usuario,contraseña) in enumerate(lista,start=1):


        listbox.insert("","end",values=(id,nombre,apellido,usuario,contraseña))
        mysqlC.close()

def obtener(listbox, name, identificador, user, password, lastname):
    name.delete(0,END)
    lastname.delete(0,END)
    password.delete(0,END)
    identificador.config(state="normal")
    identificador.delete(0,END)
    user.delete(0, END)

    renglon = listbox.selection()[0]
    print(renglon)
    seleccion = listbox.set(renglon)
    print(seleccion)
    
    identificador.insert(0,seleccion["Id"])
    name.insert(0,seleccion["Nombre"])
    lastname.insert(0,seleccion["Apellido"])
    user.insert(0,seleccion["Usuario"])
    password.insert(0,seleccion["Contraseña"])
    identificador.config(state="readonly")

