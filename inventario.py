import tkinter as tk
from tkinter import messagebox
from producto import Producto
from excepciones import CantidadInvalidaException, PrecioInvalidoException, ProductoInvalidoException



producto = None

def registrar_producto():
    global producto  
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        producto = Producto(nombre, precio, cantidad)
        status.config(text="Producto agregado correctamente",fg="green")
        detalles_label.config(text="")
    except ProductoInvalidoException as e:
        status.config(text=("Error", str(e)),fg="red")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except PrecioInvalidoException as e:
        status.config(text=("Error", str(e)),fg="red")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except CantidadInvalidaException as e:
        status.config(text=("Error", str(e)),fg="red")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except ValueError:
        status.config(text=("Error", "Precio y cantidad deben ser números válidos."),fg="red")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")
    except Exception as e:
        status.config(text=("Error", f"Ha ocurrido un error: {str(e)}"),fg="red")
        detalles_label.config(text="PRODUCTO NO VÁLIDO")

def mostrar_detalles():
    if producto is not None:
        detalles_label.config(text=producto.mostrar_detalles_producto(producto.calcular_valor_total()))
    else:
        status.config("Error", "No se ha registrado ningún producto.")

ventana = tk.Tk()
ventana.title("TIENDA")
ventana.geometry("400x500")
ventana.configure(bg="#170907")


label_tienda = tk.Label(ventana, text="GESTIÓN DE PRODUCTOS",bg="black",fg="#d1721e", font=("Times New Roman", 16), relief="ridge",highlightbackground="#d1721e",highlightthickness=2)
label_tienda.pack(pady=5)
label_nombre = tk.Label(ventana, text="Nombre del producto:",bg="black",fg="#d1721e", font=("Times New Roman", 12), relief="flat",highlightbackground="#f1e3a9",highlightthickness=1)
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, bg="#f1e3a9")
entry_nombre.pack(pady=5)

label_precio = tk.Label(ventana, text="Precio del producto:",bg="black",fg="#d1721e", font=("Times New Roman", 12), relief="flat",highlightbackground="#f1e3a9",highlightthickness=1)
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana, bg="#f1e3a9")
entry_precio.pack(pady=5)

label_cantidad = tk.Label(ventana, text="Cantidad en inventario:",bg="black",fg="#d1721e", font=("Times New Roman", 12), relief="flat",highlightbackground="#f1e3a9",highlightthickness=1)
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana, bg="#f1e3a9")
entry_cantidad.pack(pady=5)

boton_registrar = tk.Button(ventana, text="Registrar producto", command=registrar_producto,fg="#f1e3a9",bg="green", font=("Courier New", 12, "bold"))
boton_registrar.pack(pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar producto", command=mostrar_detalles,fg="#f1e3a9",bg="#1d51c2", font=("Courier New", 12, "bold"))
boton_mostrar.pack(pady=5)

status = tk.Label(ventana, text="", fg="red", relief="sunken")
status.pack()
detalles_label = tk.Label(ventana, text="", fg="blue", relief="sunken")
detalles_label.pack()


ventana.mainloop()