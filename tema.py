import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# dimensiones de la interfaz en altura y ancho en pixeles
ancho = 350
alto = 350

# obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# calcular la posición x,y para la ventana
posicion_ancho = (ancho_pantalla - ancho) // 2
posicion_alto = (alto_pantalla - alto) // 2

# establecer la geometría de la ventana
ventana.geometry(f"{ancho}x{alto}+{posicion_ancho}+{posicion_alto}")

# Variable para controlar el modo actual
modo_oscuro = False


# Función para cambiar el tema
def cambiar_tema():
    global modo_oscuro
    if modo_oscuro:
        ventana.configure(bg="white")
        boton_tema.configure(text="Modo Oscuro", bg="white", fg="black")
        modo_oscuro = False
    else:
        ventana.configure(bg="#373737")
        boton_tema.configure(text="Modo Claro", bg="#1f1e1e", fg="white")
        modo_oscuro = True


# Crear botón para cambiar tema
boton_tema = tk.Button(ventana, text="Modo Oscuro", command=cambiar_tema)
boton_tema.pack(pady=20)

# título de la ventana
ventana.title("Ventana de prueba")

# mostrar la ventana
ventana.mainloop()
