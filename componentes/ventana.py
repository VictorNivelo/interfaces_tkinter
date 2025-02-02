# ventana centrada en pyton usando tkinter

import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# dimensiones de la interfaz en altura y ancho en pixeles
ancho = 350
alto = 350

# obtener las dimesnciones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# calcular la posición x,y para la ventana
posicion_ancho = (ancho_pantalla - ancho) // 2
posicion_alto = (alto_pantalla - alto) // 2

# establecer la geometría de la ventana
ventana.geometry(f"{ancho}x{alto}+{posicion_ancho}+{posicion_alto}")

# título de la ventana
ventana.title("Ventana de prueba")

# mostrar la ventana
ventana.mainloop()
