import tkinter as tk
import math
import PIL
from PIL import ImageTk, Image

#estructura ventana GUI
ventana = tk.Tk()
ventana.geometry("900x800")
ventana.title("Cálculadora geométrica")
ventana.configure(bg="#FFFFFF")

#para centrar las figuras
ventana.grid_columnconfigure((0, 1, 2, 3), weight=1)

#estilo de fuente
fuente_titulo_montserrat = ("Montserrat", 16)
fuente_montserrat = ("Montserrat", 12)
fuente_boton_montserrat = ("Montserrat", 8)

#titulo de la calculadora
calculadora_titulo = tk.Label(ventana, text="Calculadora geométrica", bg="#FFD7D7", font=fuente_titulo_montserrat,
padx=280,
pady=10)

calculadora_titulo.grid(row=0, column=0, columnspan=4)

espacio_vacio = tk.Label(ventana, text=" ", bg="#FFFFFF")
espacio_vacio.grid(row=1, column=0, columnspan=4)

#contenedor figuras
contenedor_figuras = tk.Frame(ventana, bg="#FFD7D7", padx=30, pady=20)
contenedor_figuras.grid(row=2, column=0, columnspan=4)

#creamos array de imagenes y nombres de cada figura
nombres_figuras = [
    {
        "imagen": "img\cube.png",
        "nombre": "Cubo"
    },
    {
        "imagen": "img\sphere.png",
        "nombre": "Esfera"
    },
    {
        "imagen": "img\cylinder.png",
        "nombre": "Cilindro"
    },
    {
        "imagen": "img\cone.png",
        "nombre": "Cono"
    },
    {
        "imagen": "img\pyramid.png",
        "nombre": "Pirámide"
    },
    {
        "imagen": "img\parallelepiped.png",
        "nombre": "Paralelepípedo"
    },
    {
        "imagen": "img\ellipsoid.png",
        "nombre": "Elipsoide"
    },
    {
        "imagen": "img\octahedron.png",
        "nombre": "Octaedro"
    },
]

#array vacio para guardar las figuras que se recorran
matriz_figuras = []

#condicionales para verificar el paso del parametro con y llamar 
# a la funcion correspondiente a cada figura

def calcular_area(figura):
    if figura == "Cubo":
        calcular_area_cubo()
    elif figura == "Esfera":
        calcular_area_esfera()

def calcular_volumen(figura):
    if figura == "Cubo":
        calcular_volumen_cubo()
    elif figura == "Esfera":
        calcular_volumen_esfera()


#funciones para calcular el area de las figuras
def calcular_area_cubo():

    #creamos el modal
    ventana_modal_area_cubo = tk.Toplevel(ventana)
    ventana_modal_area_cubo.title("Cálculo de Área - Cubo")
    ventana_modal_area_cubo.geometry("600x400")

def calcular_volumen_cubo():

    #creamos el modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Cubo")

#ciclos para mostrar las cards de las figuras

for elemento in nombres_figuras:
    ruta_figura = elemento["imagen"]
    nombre = elemento["nombre"]

    #uso de libreria PLI para usar imagenes en la GUI
    imagen = Image.open(ruta_figura)
    imagen = imagen.resize((100, 100))
    imagen = ImageTk.PhotoImage(imagen)

    #contenedor para cada imagen
    tarjeta = tk.Frame(contenedor_figuras, bg="#FFFFFF", padx=20, pady=8)
    tarjeta.grid(row=len(matriz_figuras) // 4, column=len(matriz_figuras) % 4, padx=10, pady=20)

    etiqueta_imagen = tk.Label(tarjeta, image=imagen)
    etiqueta_imagen.image = imagen

    etiqueta_nombre = tk.Label(tarjeta, text=nombre, font=fuente_montserrat)

    #botones de area y volumen
    boton_area = tk.Button(tarjeta, text="Área", font=fuente_boton_montserrat, command=lambda n=nombre: calcular_area(n))
    boton_volumen = tk.Button(tarjeta, text="Volumen", font=fuente_boton_montserrat, command=lambda n=nombre: calcular_volumen(n))

    #se agregan al array vacio
    matriz_figuras.append((etiqueta_imagen, etiqueta_nombre, boton_area, boton_volumen))
    

#se usa ciclo for para ordenarlas de acuerdo a los estilos 2 filas 4 columnas
for i, (etiqueta_imagen, etiqueta_nombre, boton_area, boton_volumen) in enumerate(matriz_figuras):
    fila = (i // 4) + 1 #division entera, resultado el cosciente, se hace asi para que comience despues del titulo
    columna = i % 4 #modulo de division, resultado el residuo
    etiqueta_imagen.grid(row=fila * 2, column=columna, padx=10, pady=15)
    etiqueta_nombre.grid(row=fila * 2 + 1, column=columna, padx=10, pady=10)
    boton_area.grid(row=fila * 2 + 2, column=columna, padx=3, pady=3)
    boton_volumen.grid(row=fila * 2 + 3, column=columna, padx=3, pady=3)

    #estilos
    etiqueta_nombre.configure(bg="#FFFFFF", padx=4, pady=1)
    boton_area.configure(bg="#D9D9D9", padx=22, pady=1)
    boton_volumen.configure(bg="#D9D9D9", padx=10, pady=1)


ventana.mainloop()