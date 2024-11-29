import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *

def mostrar():
    mysqlConn=mysql.connector.connect(host="localhost", user="root", password="", database="libreria")
    cursor=mysqlConn.cursor()
    cursor.execute("select * from libros")

    libros=cursor.fetchall()
    for i in listbox.get_children():
        listbox.delete(i)
    for i,(id, titulo, autor, editorial, año_publicacion, precio) in enumerate(libros, start=1):
        listbox.insert("","end",values=(id, titulo, autor, editorial, año_publicacion, precio))
        mysqlConn.close()

def crear():
    titulo=entry_titulo.get()
    autor=entry_autor.get()
    editorial=entry_editorial.get()
    año_publicacion=entry_año.get()
    precio=entry_precio.get()

    mysqlConn=mysql.connector.connect(host="localhost", user="root", password="", database="libreria")
    cursor=mysqlConn.cursor()

    try:
        cursor.execute(f"insert into libros(titulo, autor, editorial, año_publicacion, precio) values('{titulo}', '{autor}', '{editorial}', '{año_publicacion}', {precio})")
        mysqlConn.commit()
        entry_titulo.delete(0, END)
        entry_autor.delete(0, END)
        entry_editorial.delete(0, END)
        entry_año.delete(0, END)
        entry_precio.delete(0, END)
        
        messagebox.showinfo("Informacion", "Libro agregado correctamente")
        actualizar()
    except Exception as e:
        print(e)
        mysqlConn.rollback()
        mysqlConn.close()

def obtenerR(event):
    entry_titulo.delete(0, END)
    entry_autor.delete(0, END)
    entry_editorial.delete(0, END)
    entry_año.delete(0, END)
    entry_precio.delete(0, END)
    entry_id.delete(0, END)
    

    renglon=listbox.selection()[0]
    print(renglon)
    seleccion=listbox.set(renglon)
    print(seleccion)
    entry_titulo.insert(0, seleccion["Titulo"])
    entry_autor.insert(0, seleccion["Autor"])
    entry_editorial.insert(0, seleccion["Editorial"])
    entry_año.insert(0, seleccion["Año_publicacion"])
    entry_precio.insert(0, seleccion["Precio"])
    entry_id.insert(0, seleccion["Id"])

def actualizar():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar()

def editar():
    titulo=entry_titulo.get()
    autor=entry_autor.get()
    editorial=entry_editorial.get()
    año_publicacion=entry_año.get()
    precio=entry_precio.get()
    id=entry_id.get()
    print(año_publicacion)
    mysqlConn=mysql.connector.connect(host="localhost", user="root", password="", database="libreria")
    cursor=mysqlConn.cursor()

    try:
        cursor.execute(f"update libros set titulo='{titulo}', autor='{autor}', editorial='{editorial}', año_publicacion='{año_publicacion}', precio={precio} where id={id}")
        mysqlConn.commit()
        entry_titulo.delete(0, END)
        entry_autor.delete(0, END)
        entry_editorial.delete(0, END)
        entry_año.delete(0, END)
        entry_precio.delete(0, END)
        entry_id.delete(0, END)
        messagebox.showinfo("Actualización", "Se actualizaron los datos correctamente")
        actualizar()
    except Exception as e:
        print(e)
        mysqlConn.rollback()
        mysqlConn.close()

def eliminar():
    id=entry_id.get()

    mysqlConn=mysql.connector.connect(host="localhost", user="root", password="", database="libreria")
    cursor=mysqlConn.cursor()

    try:
        cursor.execute(f"delete from libros where id={id}")
        mysqlConn.commit()
        entry_titulo.delete(0, END)
        entry_autor.delete(0, END)
        entry_editorial.delete(0, END)
        entry_año.delete(0, END)
        entry_precio.delete(0, END)
        entry_id.delete(0, END)
        messagebox.showinfo("Informacion", "Libro eliminado correctamente")
        actualizar()
    except Exception as e:
        print(e)
        mysqlConn.rollback()
        mysqlConn.close()

def filtrar():
    autor_filtro=entry_filtro.get()

    mysqlConn=mysql.connector.connect(host="localhost", user="root", password="", database="libreria")
    cursor=mysqlConn.cursor()

    cursor.execute(f"select * from libros where autor='{autor_filtro}'")
    lista_filtrada=cursor.fetchall()

    for i in listbox.get_children():
        listbox.delete(i)

    for i,(id,titulo,autor,editorial,año_publicacion,precio) in enumerate(lista_filtrada, start=1):
        listbox.insert("","end",values=(id, titulo, autor, editorial, año_publicacion, precio))
        mysqlConn.close()

def salir(ventana: Tk):
    from login import ventana_login
    ventana.destroy()
    ventana_login()

def ventana_empleado():
    global entry_titulo
    global entry_autor
    global entry_editorial
    global entry_año
    global entry_precio
    global entry_id
    global entry_filtro
    global listbox

    ventana=tk.Tk()
    ventana.title("Menu empleado")
    ventana.geometry("1500x600")

    tk.Label(ventana, text="ADMINISTRAR LIBROS", font=("Arial", 18)).place(x=500, y=5)

    label_titulo=tk.Label(ventana, text="Titulo")
    label_titulo.place(x=20, y=30)
    
    label_autor=tk.Label(ventana, text="Autor")
    label_autor.place(x=20, y=90)

    label_editorial=tk.Label(ventana, text="Editorial")
    label_editorial.place(x=20, y=150)

    label_año=tk.Label(ventana, text="Fecha de publicacion")
    label_año.place(x=20, y=210)

    label_precio=tk.Label(ventana, text="Precio")
    label_precio.place(x=20, y=270)

    label_id=tk.Label(ventana, text="ID")
    label_id.place(x=500, y=150)
    
    label_filtro=tk.Label(ventana, text="Filtrar por autor")
    label_filtro.place(x=1000, y=150)

    entry_filtro=tk.Entry(ventana, width=30)
    entry_filtro.place(x=1000, y=180)

    entry_id=tk.Entry(ventana, width=20)
    entry_id.place(x=500, y=180)

    entry_titulo=tk.Entry(ventana, width=30)
    entry_titulo.place(x=20, y=60)

    entry_autor=tk.Entry(ventana, width=30)
    entry_autor.place(x=20, y=120)

    entry_editorial=tk.Entry(ventana, width=30)
    entry_editorial.place(x=20, y=180)

    entry_año=tk.Entry(ventana, width=20)
    entry_año.place(x=20, y=240)

    entry_precio=tk.Entry(ventana, width=20)
    entry_precio.place(x=20, y=300)

    tk.Button(ventana, text="Crear", command=crear, height=3, width=10).place(x=250, y=100)
    tk.Button(ventana, text="Editar", command=editar, height=3, width=10).place(x=500, y=250)
    tk.Button(ventana, text="Eliminar", command=eliminar, height=3, width=10).place(x=600, y=250)
    tk.Button(ventana, text="Filtrar", command=filtrar, height=3, width=10).place(x=1000, y=250)
    tk.Button(ventana, text="Cancelar", command=mostrar, height=3, width=10).place(x=1100, y=250)
    tk.Button(ventana, text="Salir", command=lambda: salir(ventana=ventana), height=3, width=10).place(x=1300, y=450)

    columnas=("Id", "Titulo", "Autor", "Editorial", "Año_publicacion", "Precio")
    listbox=ttk.Treeview(ventana, columns=columnas, show="headings")

    for columna in columnas:
        listbox.heading(columna, text=columna)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=400)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)

    ventana.mainloop()
