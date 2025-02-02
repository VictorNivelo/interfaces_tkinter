# ventana centrada en pyton usando tkinter

import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# dimensiones de la interfaz en altura y ancho en pixeles
ancho = 300
alto = 200

# color de fondo de la ventana
color_fondo = "#92e1d9"

# letra de la ventana
letra = "Helvetica"

# obtener las dimesnciones de la pantalla del dispoitivo
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# calcular la posición x,y para la ventana
posicion_ancho = (ancho_pantalla - ancho) // 2
posicion_alto = (alto_pantalla - alto) // 2

# establecer la geometría de la ventana
ventana.geometry(f"{ancho}x{alto}+{posicion_ancho}+{posicion_alto}")

# título de la ventana
ventana.title("Contador de Clics")

# configurar el color de fondo de la ventana
ventana.configure(bg=color_fondo)

# etiqueta en la ventana
etiqueta = tk.Label(
    ventana,
    text="Contador de Clics",
    font=(letra, 25),
    bg=color_fondo,
)

# empaquetar la etiqueta
etiqueta.pack(pady=5)

# contador declarado con el valor de 0
contador = 0


# función para imprimir en consola
def imprimir():
    # variable global contador
    global contador
    # incrementar el contador
    contador += 1
    # imprimir en consola el valor del contador
    print(f"Botón presionado {contador} veces")
    # actualizar el texto de la etiqueta del contador
    etiqueta_contador.config(text=f"{contador}", font=(letra, 20), bg=color_fondo)


# boton en la ventana con la función imprimir
boton = tk.Button(ventana, text="Presionar", command=imprimir, font=(letra, 12))

# empaquetar el boton
boton.pack(pady=5)

# etiqueta para mostrar el contador
etiqueta_contador = tk.Label(ventana, text=f"{contador}", font=(letra, 20), bg=color_fondo)

# empaquetar la etiqueta del contador
etiqueta_contador.pack(pady=5)

# mostrar la ventana
ventana.mainloop()
