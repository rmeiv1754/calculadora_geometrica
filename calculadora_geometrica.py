# Dar permisos varios: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# Activar el entorno virtual: Ir a la carpeta SCRIPT y ejecutar el file .\activate
# devolverse con cd.. y Ejecutar código: py calculadora_geometrica.py

# Hecho en VSCODE

import tkinter as tk
from tkinter import messagebox
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
        "imagen": "img\\cube.png",
        "nombre": "Cubo"
    },
    {
        "imagen": "img\\sphere.png",
        "nombre": "Esfera"
    },
    {
        "imagen": "img\\cylinder.png",
        "nombre": "Cilindro"
    },
    {
        "imagen": "img\\cone.png",
        "nombre": "Cono"
    },
    {
        "imagen": "img\\pyramid.png",
        "nombre": "Pirámide"
    },
    {
        "imagen": "img\\parallelepiped.png",
        "nombre": "Paralelepípedo"
    },
    {
        "imagen": "img\\ellipsoid.png",
        "nombre": "Elipsoide"
    },
    {
        "imagen": "img\\octahedron.png",
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
    elif figura == "Cilindro":
        calcular_area_cilindro()
    elif figura == "Cono":
        calcular_area_cono()
    elif figura == "Pirámide":
        calcular_area_piramide()
    elif figura == "Paralelepípedo":
        calcular_area_paralelepipedo()
    elif figura == "Elipsoide":
        calcular_area_elipsoide()
    elif figura == "Octaedro":
        calcular_area_octaedro()

def calcular_volumen(figura):
    if figura == "Cubo":
        calcular_volumen_cubo()
    elif figura == "Esfera":
        calcular_volumen_esfera()
    elif figura == "Cilindro":
        calcular_volumen_cilindro()
    elif figura == "Cono":
        calcular_volumen_cono()
    elif figura == "Pirámide":
        calcular_volumen_piramide()
    elif figura == "Paralelepípedo":
        calcular_volumen_paralelepipedo()
    elif figura == "Elipsoide":
        calcular_volumen_elipsoide()
    elif figura == "Octaedro":
        calcular_volumen_octaedro()

#funciones para calcular el area de las figuras
#figuras maria: cubo-volumen, esfera, cilindro, cono
def calcular_area_cubo():

    #creamos el modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Área - Cubo")
    ventana_modal.geometry("600x310")

    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    #dividimos en 2 la ventana_modal: 1 frame entrada 2 frame resultados
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    
    ventana_modal_input = tk.Label(frame_entrada, text="Lado del cubo: ", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_input.grid(row=1, column=0, padx=10)

    lado_ingresar = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    lado_ingresar.grid(row=1, column=1, padx=10)

    #menu desplegable
    opcion_var = tk.StringVar()
    opcion_var.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones = tk.OptionMenu(frame_entrada, opcion_var, *lista_magnitud)
    opciones.grid(row=1, column=2, padx=10)
    
    #se muestra la opcion seleccionada
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Destruye todos los widgets dentro de frame_mostrar_re
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()
    
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFFFFF")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")
    

    def calcular_y_mostrar_area():
        # Obtener el valor ingresado en lado_ingresar
        lado = float(lado_ingresar.get())
        magnitud_seleccionada = opcion_var.get()

        # Definir las relaciones de conversión
        conversiones = {
        "centímetros": 0.01,  # 1 metro = 100 centímetros
        "pulgadas": 0.0254,   # 1 metro = 39.37 pulgadas
        "metros": 1.0         # No se necesita conversión
         }

        lado_en_metros = lado * conversiones[magnitud_seleccionada]

        # Calcular el área del cubo
        area = 6 * lado_en_metros ** 2

        # Borra resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Área del cubo: {area} m2", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()


    calcular_button = tk.Button(frame_entrada, text="Calcular Área", command=calcular_y_mostrar_area)
    calcular_button.grid(row=2, column=0, columnspan=5, pady=10)

    #estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones.config()

def calcular_volumen_cubo():
    #creamos el modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Cubo")
    

#figuras yotas pelotas: pirámide, paralelepipedo, elipsoide, octaedro

#PIRAMIDE
def calcular_area_piramide():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Área - Pirámide")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud de la base
    ventana_modal_longitud_base = tk.Label(frame_entrada, text="Longitud de la base:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud_base.grid(row=1, column=0, padx=10)
    
    entrada_longitud_base = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud_base.grid(row=1, column=1, padx=10)
    
    magnitud_longitud_base = tk.StringVar()
    magnitud_longitud_base.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud_base = tk.OptionMenu(frame_entrada, magnitud_longitud_base, *lista_magnitud)
    opciones_magnitud_longitud_base.grid(row=1, column=2, padx=10)
    
    # Entrada para la altura de la pirámide
    ventana_modal_altura = tk.Label(frame_entrada, text="Altura de la pirámide:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_altura.grid(row=2, column=0, padx=10)
    
    entrada_altura = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_altura.grid(row=2, column=1, padx=10)
    
    magnitud_altura = tk.StringVar()
    magnitud_altura.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_altura = tk.OptionMenu(frame_entrada, magnitud_altura, *lista_magnitud)
    opciones_magnitud_altura.grid(row=2, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el área de la pirámide
    def calcular_y_mostrar_area():
        # Obtener los valores ingresados
        longitud_base = float(entrada_longitud_base.get())
        magnitud_seleccionada_base = magnitud_longitud_base.get()

        altura = float(entrada_altura.get())
        magnitud_seleccionada_altura = magnitud_altura.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir las medidas a metros
        longitud_base_en_metros = longitud_base * conversiones[magnitud_seleccionada_base]
        altura_en_metros = altura * conversiones[magnitud_seleccionada_altura]

        # Calcular el área de la pirámide
        area = (longitud_base_en_metros ** 2 + 2 * longitud_base_en_metros * altura_en_metros)

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Área de la pirámide: {area} m2", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Área", command=calcular_y_mostrar_area)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_altura.config()
    opciones_magnitud_longitud_base.config()

def calcular_volumen_piramide():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Pirámide")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud de la base
    ventana_modal_longitud_base = tk.Label(frame_entrada, text="Longitud de la base:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud_base.grid(row=1, column=0, padx=10)
    
    entrada_longitud_base = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud_base.grid(row=1, column=1, padx=10)
    
    magnitud_longitud_base = tk.StringVar()
    magnitud_longitud_base.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud_base = tk.OptionMenu(frame_entrada, magnitud_longitud_base, *lista_magnitud)
    opciones_magnitud_longitud_base.grid(row=1, column=2, padx=10)
    
    # Entrada para la altura de la pirámide
    ventana_modal_altura = tk.Label(frame_entrada, text="Altura de la pirámide:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_altura.grid(row=2, column=0, padx=10)
    
    entrada_altura = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_altura.grid(row=2, column=1, padx=10)
    
    magnitud_altura = tk.StringVar()
    magnitud_altura.set("metros")
    opciones_magnitud_altura = tk.OptionMenu(frame_entrada, magnitud_altura, *lista_magnitud)
    opciones_magnitud_altura.grid(row=2, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el volumen de la pirámide
    def calcular_y_mostrar_volumen():
        # Obtener los valores ingresados
        longitud_base = float(entrada_longitud_base.get())
        magnitud_seleccionada_base = magnitud_longitud_base.get()

        altura = float(entrada_altura.get())
        magnitud_seleccionada_altura = magnitud_altura.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir las medidas a metros
        longitud_base_en_metros = longitud_base * conversiones[magnitud_seleccionada_base]
        altura_en_metros = altura * conversiones[magnitud_seleccionada_altura]

        # Calcular el volumen de la pirámide
        volumen = (1/3) * (longitud_base_en_metros ** 2) * altura_en_metros

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Volumen de la pirámide: {volumen} m3", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Volumen", command=calcular_y_mostrar_volumen)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_altura.config()
    opciones_magnitud_longitud_base.config()

#PARALELEPIPEDO
def calcular_area_paralelepipedo():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Área - Paralelepípedo")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud
    ventana_modal_longitud = tk.Label(frame_entrada, text="Longitud:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud.grid(row=1, column=0, padx=10)
    
    entrada_longitud = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud.grid(row=1, column=1, padx=10)
    
    magnitud_longitud = tk.StringVar()
    magnitud_longitud.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud = tk.OptionMenu(frame_entrada, magnitud_longitud, *lista_magnitud)
    opciones_magnitud_longitud.grid(row=1, column=2, padx=10)
    
    # Entrada para el ancho
    ventana_modal_ancho = tk.Label(frame_entrada, text="Ancho:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_ancho.grid(row=2, column=0, padx=10)
    
    entrada_ancho = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_ancho.grid(row=2, column=1, padx=10)
    
    magnitud_ancho = tk.StringVar()
    magnitud_ancho.set("metros")
    opciones_magnitud_ancho = tk.OptionMenu(frame_entrada, magnitud_ancho, *lista_magnitud)
    opciones_magnitud_ancho.grid(row=2, column=2, padx=10)

    # Entrada para la altura
    ventana_modal_altura = tk.Label(frame_entrada, text="Altura:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_altura.grid(row=3, column=0, padx=10)
    
    entrada_altura = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_altura.grid(row=3, column=1, padx=10)
    
    magnitud_altura = tk.StringVar()
    magnitud_altura.set("metros")
    opciones_magnitud_altura = tk.OptionMenu(frame_entrada, magnitud_altura, *lista_magnitud)
    opciones_magnitud_altura.grid(row=3, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el área del paralelepípedo
    def calcular_y_mostrar_area():
        # Obtener los valores ingresados
        longitud = float(entrada_longitud.get())
        magnitud_seleccionada_longitud = magnitud_longitud.get()

        ancho = float(entrada_ancho.get())
        magnitud_seleccionada_ancho = magnitud_ancho.get()

        altura = float(entrada_altura.get())
        magnitud_seleccionada_altura = magnitud_altura.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir las medidas a metros
        longitud_en_metros = longitud * conversiones[magnitud_seleccionada_longitud]
        ancho_en_metros = ancho * conversiones[magnitud_seleccionada_ancho]
        altura_en_metros = altura * conversiones[magnitud_seleccionada_altura]

        # Calcular el área del paralelepípedo
        area = 2 * (longitud_en_metros * ancho_en_metros + ancho_en_metros * altura_en_metros + altura_en_metros * longitud_en_metros)

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Área del paralelepípedo: {area} m2", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Área", command=calcular_y_mostrar_area)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_altura.config()
    opciones_magnitud_longitud.config()

def calcular_volumen_paralelepipedo():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Paralelepípedo")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud
    ventana_modal_longitud = tk.Label(frame_entrada, text="Longitud:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud.grid(row=1, column=0, padx=10)
    
    entrada_longitud = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud.grid(row=1, column=1, padx=10)
    
    magnitud_longitud = tk.StringVar()
    magnitud_longitud.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud = tk.OptionMenu(frame_entrada, magnitud_longitud, *lista_magnitud)
    opciones_magnitud_longitud.grid(row=1, column=2, padx=10)
    
    # Entrada para el ancho
    ventana_modal_ancho = tk.Label(frame_entrada, text="Ancho:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_ancho.grid(row=2, column=0, padx=10)
    
    entrada_ancho = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_ancho.grid(row=2, column=1, padx=10)
    
    magnitud_ancho = tk.StringVar()
    magnitud_ancho.set("metros")
    opciones_magnitud_ancho = tk.OptionMenu(frame_entrada, magnitud_ancho, *lista_magnitud)
    opciones_magnitud_ancho.grid(row=2, column=2, padx=10)

    # Entrada para la altura
    ventana_modal_altura = tk.Label(frame_entrada, text="Altura:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_altura.grid(row=3, column=0, padx=10)
    
    entrada_altura = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_altura.grid(row=3, column=1, padx=10)
    
    magnitud_altura = tk.StringVar()
    magnitud_altura.set("metros")
    opciones_magnitud_altura = tk.OptionMenu(frame_entrada, magnitud_altura, *lista_magnitud)
    opciones_magnitud_altura.grid(row=3, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el volumen del paralelepípedo
    def calcular_y_mostrar_volumen():
        # Obtener los valores ingresados
        longitud = float(entrada_longitud.get())
        magnitud_seleccionada_longitud = magnitud_longitud.get()

        ancho = float(entrada_ancho.get())
        magnitud_seleccionada_ancho = magnitud_ancho.get()

        altura = float(entrada_altura.get())
        magnitud_seleccionada_altura = magnitud_altura.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.000001,  # 1 metro cúbico = 1,000,000 cm3
            "pulgadas": 0.0000163871,  # 1 metro cúbico = 61,023.7 pulgadas3
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir las medidas a metros cúbicos
        longitud_en_metros = longitud * conversiones[magnitud_seleccionada_longitud]
        ancho_en_metros = ancho * conversiones[magnitud_seleccionada_ancho]
        altura_en_metros = altura * conversiones[magnitud_seleccionada_altura]

        # Calcular el volumen del paralelepípedo
        volumen = longitud_en_metros * ancho_en_metros * altura_en_metros

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Volumen del paralelepípedo: {volumen} m3", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Volumen", command=calcular_y_mostrar_volumen)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_altura.config()
    opciones_magnitud_longitud.config()

#ELIPSOIDE
def calcular_area_elipsoide():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Área - Elipsoide")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para el radio mayor
    ventana_modal_radio_mayor = tk.Label(frame_entrada, text="Radio Mayor:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_radio_mayor.grid(row=1, column=0, padx=10)
    
    entrada_radio_mayor = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_radio_mayor.grid(row=1, column=1, padx=10)
    
    magnitud_radio_mayor = tk.StringVar()
    magnitud_radio_mayor.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_radio_mayor = tk.OptionMenu(frame_entrada, magnitud_radio_mayor, *lista_magnitud)
    opciones_magnitud_radio_mayor.grid(row=1, column=2, padx=10)
    
    # Entrada para el radio menor
    ventana_modal_radio_menor = tk.Label(frame_entrada, text="Radio Menor:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_radio_menor.grid(row=2, column=0, padx=10)
    
    entrada_radio_menor = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_radio_menor.grid(row=2, column=1, padx=10)
    
    magnitud_radio_menor = tk.StringVar()
    magnitud_radio_menor.set("metros")
    opciones_magnitud_radio_menor = tk.OptionMenu(frame_entrada, magnitud_radio_menor, *lista_magnitud)
    opciones_magnitud_radio_menor.grid(row=2, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el área del elipsoide
    def calcular_y_mostrar_area():
        # Obtener los valores ingresados
        radio_mayor = float(entrada_radio_mayor.get())
        magnitud_seleccionada_radio_mayor = magnitud_radio_mayor.get()

        radio_menor = float(entrada_radio_menor.get())
        magnitud_seleccionada_radio_menor = magnitud_radio_menor.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.0001,  # 1 metro = 10,000 centímetros
            "pulgadas": 0.00064516,  # 1 metro = 1,550 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir los radios a metros
        radio_mayor_en_metros = radio_mayor * conversiones[magnitud_seleccionada_radio_mayor]
        radio_menor_en_metros = radio_menor * conversiones[magnitud_seleccionada_radio_menor]

        # Calcular el área del elipsoide
        area = math.pi * radio_mayor_en_metros * radio_menor_en_metros

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Área del elipsoide: {area} m²", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Área", command=calcular_y_mostrar_area)
    calcular_button.grid(row=3, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_radio_mayor.config()
    opciones_magnitud_radio_menor.config()

def calcular_volumen_elipsoide():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Elipsoide")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para el radio mayor
    ventana_modal_radio_mayor = tk.Label(frame_entrada, text="Radio Mayor:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_radio_mayor.grid(row=1, column=0, padx=10)
    
    entrada_radio_mayor = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_radio_mayor.grid(row=1, column=1, padx=10)
    
    magnitud_radio_mayor = tk.StringVar()
    magnitud_radio_mayor.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_radio_mayor = tk.OptionMenu(frame_entrada, magnitud_radio_mayor, *lista_magnitud)
    opciones_magnitud_radio_mayor.grid(row=1, column=2, padx=10)
    
    # Entrada para el radio menor
    ventana_modal_radio_menor = tk.Label(frame_entrada, text="Radio Menor:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_radio_menor.grid(row=2, column=0, padx=10)
    
    entrada_radio_menor = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_radio_menor.grid(row=2, column=1, padx=10)
    
    magnitud_radio_menor = tk.StringVar()
    magnitud_radio_menor.set("metros")
    opciones_magnitud_radio_menor = tk.OptionMenu(frame_entrada, magnitud_radio_menor, *lista_magnitud)
    opciones_magnitud_radio_menor.grid(row=2, column=2, padx=10)

    # Entrada para el radio intermedio
    ventana_modal_radio_intermedio = tk.Label(frame_entrada, text="Radio Intermedio:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_radio_intermedio.grid(row=3, column=0, padx=10)
    
    entrada_radio_intermedio = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_radio_intermedio.grid(row=3, column=1, padx=10)
    
    magnitud_radio_intermedio = tk.StringVar()
    magnitud_radio_intermedio.set("metros")
    opciones_magnitud_radio_intermedio = tk.OptionMenu(frame_entrada, magnitud_radio_intermedio, *lista_magnitud)
    opciones_magnitud_radio_intermedio.grid(row=3, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el volumen del elipsoide
    def calcular_y_mostrar_volumen():
        # Obtener los valores ingresados
        radio_mayor = float(entrada_radio_mayor.get())
        magnitud_seleccionada_radio_mayor = magnitud_radio_mayor.get()

        radio_menor = float(entrada_radio_menor.get())
        magnitud_seleccionada_radio_menor = magnitud_radio_menor.get()

        radio_intermedio = float(entrada_radio_intermedio.get())
        magnitud_seleccionada_radio_intermedio = magnitud_radio_intermedio.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir los radios a metros
        radio_mayor_en_metros = radio_mayor * conversiones[magnitud_seleccionada_radio_mayor]
        radio_menor_en_metros = radio_menor * conversiones[magnitud_seleccionada_radio_menor]
        radio_intermedio_en_metros = radio_intermedio * conversiones[magnitud_seleccionada_radio_intermedio]

        # Calcular el volumen del elipsoide
        volumen = (4/3) * math.pi * radio_mayor_en_metros * radio_menor_en_metros * radio_intermedio_en_metros

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Volumen del elipsoide: {volumen} m³", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Volumen", command=calcular_y_mostrar_volumen)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_radio_mayor.config()
    opciones_magnitud_radio_menor.config()
    opciones_magnitud_radio_intermedio.config()


#OCTAEDRO
def calcular_area_octaedro():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Área - Octaedro")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud de un lado del octaedro
    ventana_modal_longitud_lado = tk.Label(frame_entrada, text="Longitud de un lado:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud_lado.grid(row=1, column=0, padx=10)
    
    entrada_longitud_lado = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud_lado.grid(row=1, column=1, padx=10)
    
    magnitud_longitud_lado = tk.StringVar()
    magnitud_longitud_lado.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud_lado = tk.OptionMenu(frame_entrada, magnitud_longitud_lado, *lista_magnitud)
    opciones_magnitud_longitud_lado.grid(row=1, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el área del octaedro
    def calcular_y_mostrar_area():
        # Obtener los valores ingresados
        longitud_lado = float(entrada_longitud_lado.get())
        magnitud_seleccionada_lado = magnitud_longitud_lado.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir la longitud de un lado a metros
        longitud_lado_en_metros = longitud_lado * conversiones[magnitud_seleccionada_lado]

        # Calcular el área del octaedro
        area = 2 * (math.sqrt(3) * longitud_lado_en_metros**2)

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Área del octaedro: {area} m²", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Área", command=calcular_y_mostrar_area)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_longitud_lado.config()

def calcular_volumen_octaedro():
    # Crear la ventana modal
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.title("Cálculo de Volumen - Octaedro")
    ventana_modal.geometry("600x310")

    # Crear el frame de entrada
    frame_entrada = tk.Frame(ventana_modal, bg="#FFFFFF")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10)

    # Título
    ventana_modal_titulo = tk.Label(frame_entrada, text="Ingresa los datos", font=fuente_titulo_montserrat, justify="center", bg="#FFFFFF")
    ventana_modal_titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Entrada para la longitud de un lado del octaedro
    ventana_modal_longitud_lado = tk.Label(frame_entrada, text="Longitud de un lado:", font=fuente_montserrat, bg="#FFD7D7")
    ventana_modal_longitud_lado.grid(row=1, column=0, padx=10)
    
    entrada_longitud_lado = tk.Entry(frame_entrada, width=30, bg="#FFFFFF")
    entrada_longitud_lado.grid(row=1, column=1, padx=10)
    
    magnitud_longitud_lado = tk.StringVar()
    magnitud_longitud_lado.set("metros")
    lista_magnitud = ["centímetros", "pulgadas", "metros"]
    opciones_magnitud_longitud_lado = tk.OptionMenu(frame_entrada, magnitud_longitud_lado, *lista_magnitud)
    opciones_magnitud_longitud_lado.grid(row=1, column=2, padx=10)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana_modal)
    frame_resultados.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_resultado = tk.Label(frame_resultados, text="Resultado", font=fuente_titulo_montserrat, bg="#FFFFFF")
    etiqueta_resultado.grid(row=0, column=0)

    frame_mostrar_re = tk.Frame(ventana_modal, bg="#D9D9D9")
    frame_mostrar_re.grid(row=2, column=0, padx=10, pady=10, columnspan=5, rowspan=5)

    # Función para borrar resultados antiguos
    def borrar_resultados_antiguos():
        for widget in frame_mostrar_re.winfo_children():
            widget.destroy()

    # Función para mostrar un cuadro de diálogo
    def mostrar_cuadro_dialogo():
        # Crear un cuadro de diálogo personalizado para preguntar al usuario
        cuadro_dialogo = tk.Toplevel(ventana_modal)
        cuadro_dialogo.title("Realizar otro cálculo")

        etiqueta_pregunta = tk.Label(cuadro_dialogo, text="¿Desea realizar otro cálculo?", font=fuente_montserrat, bg="#FFD7D7")
        etiqueta_pregunta.grid(row=0, column=0, padx=10, pady=10)

        boton_si = tk.Button(cuadro_dialogo, text="Sí", command=cuadro_dialogo.destroy, bg="#FFD7D7")
        boton_si.grid(row=1, column=0, padx=40, pady=10)

        boton_no = tk.Button(cuadro_dialogo, text="No", command=ventana_modal.destroy)
        boton_no.grid(row=1, column=1, padx=10, pady=10)

        # Estilos
        cuadro_dialogo.configure(bg="#FFFFFF")

    # Función para calcular y mostrar el volumen del octaedro
    def calcular_y_mostrar_volumen():
        # Obtener los valores ingresados
        longitud_lado = float(entrada_longitud_lado.get())
        magnitud_seleccionada_lado = magnitud_longitud_lado.get()

        # Definir las relaciones de conversión
        conversiones = {
            "centímetros": 0.01,  # 1 metro = 100 centímetros
            "pulgadas": 0.0254,  # 1 metro = 39.37 pulgadas
            "metros": 1.0  # No se necesita conversión
        }

        # Convertir la longitud de un lado a metros
        longitud_lado_en_metros = longitud_lado * conversiones[magnitud_seleccionada_lado]

        # Calcular el volumen del octaedro
        volumen = (1/3) * (math.sqrt(2) * longitud_lado_en_metros**3)

        # Borrar resultados antiguos antes de mostrar uno nuevo
        borrar_resultados_antiguos()

        # Mostrar el resultado en un Label dentro de frame_mostrar_re
        resultado_label = tk.Label(frame_mostrar_re, text=f"Volumen del octaedro: {volumen} m³", font=fuente_montserrat, bg="#D9D9D9")
        resultado_label.grid(row=0, column=0)

        mostrar_cuadro_dialogo()

    calcular_button = tk.Button(frame_entrada, text="Calcular Volumen", command=calcular_y_mostrar_volumen)
    calcular_button.grid(row=4, column=0, columnspan=5, pady=10)

    # Estilos
    ventana_modal.configure(bg="#FFFFFF")
    opciones_magnitud_longitud_lado.config()


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
    etiqueta_imagen.grid(row=fila, column=columna, padx=10, pady=15)
    etiqueta_nombre.grid(row=fila * 2 + 1, column=columna, padx=10, pady=10)
    boton_area.grid(row=fila * 2 + 2, column=columna, padx=3, pady=3)
    boton_volumen.grid(row=fila * 2 + 3, column=columna, padx=3, pady=3)

    #estilos
    etiqueta_nombre.configure(bg="#FFFFFF", padx=4, pady=1)
    boton_area.configure(bg="#D9D9D9", padx=22, pady=1)
    boton_volumen.configure(bg="#D9D9D9", padx=10, pady=1)


ventana.mainloop()