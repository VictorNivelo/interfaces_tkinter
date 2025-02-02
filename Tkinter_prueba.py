import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("500x600")

# 1. Etiquetas (Label)
etiqueta = tk.Label(ventana, text="Esto es una etiqueta")
etiqueta.grid(row=0, column=0)

# 2. Botones (Button)
boton = tk.Button(ventana, text="Clic aquí")
boton.grid(row=1, column=0)

# 3. Entrada de texto (Entry)
entrada = tk.Entry(ventana)
entrada.grid(row=2, column=0)

# 4. Área de texto (Text)
texto_area = tk.Text(ventana, height=5, width=30)
texto_area.grid(row=3, column=0)

# 5. Checkbutton
checkbox = tk.Checkbutton(ventana, text="Opción")
checkbox.grid(row=4, column=0)

# 6. Radiobutton
radio1 = tk.Radiobutton(ventana, text="Opción 1", value=1)
radio2 = tk.Radiobutton(ventana, text="Opción 2", value=2)
radio1.grid(row=5, column=0)
radio2.grid(row=5, column=1)

# 7. Listbox
listbox = tk.Listbox(ventana)
listbox.insert(1, "Elemento 1")
listbox.insert(2, "Elemento 2")
listbox.grid(row=6, column=0)

# 8. Combobox
combo = ttk.Combobox(ventana, values=["Opción 1", "Opción 2"])
combo.grid(row=7, column=0)

# 9. Scale
scale = tk.Scale(ventana, from_=0, to=100, orient="horizontal")
scale.grid(row=8, column=0)

# 10. Spinbox
spinbox = tk.Spinbox(ventana, from_=0, to=100)
spinbox.grid(row=9, column=0)

# Configuración del menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)
archivo_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)

ventana.mainloop()