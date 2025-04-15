import tkinter as tk
import time
from tkinter import messagebox
from logic import resolver_n_reinas, resolver_AG_reinas

class NReinasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Problema de las N Reinas")
        
        self.N = 4
        self.soluciones = [] 
        self.solucion_actual = 0 
        
        self.label_input = tk.Label(root, text="Número de reinas (N):")
        self.label_input.grid(row=0, column=0, padx=10, pady=5)
        
        self.input_n = tk.Entry(root, width=5)
        self.input_n.grid(row=0, column=1, padx=10, pady=5)
        self.input_n.insert(0, str(self.N))
        
        self.btn_actualizar = tk.Button(root, text="Actualizar Tablero", command=self.actualizar_tablero)
        self.btn_actualizar.grid(row=0, column=2, padx=10, pady=5)
        
        self.btn_encontrar = tk.Button(root, text="Encontrar Soluciones", command=self.encontrar_soluciones)
        self.btn_encontrar.grid(row=0, column=3, padx=10, pady=5)
        
        self.label_soluciones = tk.Label(root, text=f"Soluciones: 0")
        self.label_soluciones.grid(row=0, column=4, padx=10, pady=5)
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        
        self.btn_siguiente = tk.Button(root, text="Siguiente", command=self.mostrar_siguiente_solucion)
        self.btn_siguiente.grid(row=2, column=0, columnspan=5, pady=10)
        
        self.label_solution_optim = tk.Label(root, text=f"Solucion optima: ")
        self.label_solution_optim.grid(row=3, column=0, columnspan=5, pady=10)
        
        self.dibujar_tablero()
    
    def dibujar_tablero(self):
        """Dibuja el tablero de tamaño N x N."""
        self.canvas.delete("all")
        tamano = 400 // self.N
        
        for i in range(self.N):
            for j in range(self.N):
                x1, y1 = j * tamano, i * tamano
                x2, y2 = x1 + tamano, y1 + tamano
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    
    def dibujar_solucion(self, solucion):
        """Dibuja una solución en el tablero."""
        tamano = 400 // self.N
        
        for col, fila in enumerate(solucion):
            x1, y1 = col * tamano, fila * tamano
            x2, y2 = x1 + tamano, y1 + tamano
            self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
    
    def actualizar_tablero(self):
        """Actualiza el tablero según el número ingresado."""
        try:
            self.N = int(self.input_n.get())
            if self.N <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido mayor a 0.")
            return
        
        self.dibujar_tablero()
    
    def encontrar_soluciones(self):
        """Encuentra las soluciones y actualiza la interfaz."""
        try:
            self.N = int(self.input_n.get())
            if self.N <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido mayor a 0.")
            return

        self.soluciones = resolver_n_reinas(self.N) 
        self.solucion_actual = 0
        num_soluciones = len(self.soluciones)
        self.label_soluciones.config(text=f"Soluciones: {num_soluciones}")
        
        if num_soluciones > 0:
            self.dibujar_solucion(self.soluciones[self.solucion_actual])
            self.label_solution_optim.config(text=f"Solución optima: {self.soluciones[0]}")
        else:
            messagebox.showinfo("Información", "No se encontraron soluciones para este tamaño de tablero.")
    
    def mostrar_siguiente_solucion(self):
        """Muestra la siguiente solución en el carrusel."""
        if not self.soluciones:
            messagebox.showinfo("Información", "No hay soluciones para mostrar.")
            return
        
        self.solucion_actual = (self.solucion_actual + 1) % len(self.soluciones)
        
        self.dibujar_tablero()
        self.dibujar_solucion(self.soluciones[self.solucion_actual])
