import tkinter as tk
from prettytable import PrettyTable


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    fx0, fx1 = f(x0), f(x1)
    #if x0 == x1:
    #    error = 0
    #else:
    #   error = abs((x1 - x0) / x1) * 100
    error = 100
    table = PrettyTable(['i', 'x0', 'x1', 'x', 'f(x0)', 'f(x1)', 'f(x)', 'error (%)'])
    for i in range(max_iter):
        x = x1 - fx1*(x1-x0)/(fx1-fx0)
        fx = f(x)
        if abs(fx) < tol:
            error = abs((x-x1)/x)*100
            table.add_row([i+1, round(x0, 4), round(x1, 4), round(x, 4), round(fx0, 4), round(fx1, 4), round(fx, 4), round(error, 4)])
            return x, table
        error = abs((x-x1)/x)*100
        table.add_row([i+1, round(x0, 4), round(x1, 4), round(x, 4), round(fx0, 4), round(fx1, 4), round(fx, 4), round(error, 4)])
        x0, fx0 = x1, fx1
        x1, fx1 = x, fx
    raise Exception(f"No se pudo encontrar la raíz después de {max_iter} iteraciones.")


class SecanteGUI: #Clase que se encarga de manejar la creación y diseño de la interfaz.
    def __init__(self, master): #master representa la ventana principal de la GUI.
        self.master = master # Asigna al objeto master la instancia de self.master
        master.title("Método de la Secante") # Se establece el título de la ventana como "Método de la Secante"
        
        # Crear widgets
        self.f_label = tk.Label(master, text="Ingrese la función cuya raíz desea encontrar:")
        self.f_entry = tk.Entry(master)
        self.x0_label = tk.Label(master, text="Ingrese un valor para x0:")
        self.x0_entry = tk.Entry(master)
        self.x1_label = tk.Label(master, text="Ingrese un valor para x1:")
        self.x1_entry = tk.Entry(master)
        self.calc_button = tk.Button(master, text="Calcular", command=self.calcular)
        self.result_label = tk.Label(master, text="Resultado:")
        self.result_text = tk.Text(master, height=10, width=50)
        self.table_label = tk.Label(master, text="Tabla de iteraciones:")
        self.table_text = tk.Text(master, height=10, width=100)
        
        # Ubicar widgets en la ventana
        self.f_label.grid(row=0, column=0, sticky="W")
        self.f_entry.grid(row=1, column=0, columnspan=2, sticky="WE")
        self.x0_label.grid(row=2, column=0, sticky="W")
        self.x0_entry.grid(row=3, column=0, sticky="WE")
        self.x1_label.grid(row=2, column=1, sticky="W")
        self.x1_entry.grid(row=3, column=1, sticky="WE")
        self.calc_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=5, column=0, sticky="W")
        self.result_text.grid(row=6, column=0, columnspan=2, sticky="WE")
        self.table_label.grid(row=7, column=0, columnspan=2, sticky="W")
        self.table_text.grid(row=8, column=0, columnspan=2, sticky="WE")
        
    def calcular(self):
        # Obtener la función y los valores iniciales
        f_str = self.f_entry.get() # Obtiene el valor ingresado en el campo de entrada 'f_entry' y lo almacena en la variable 'f_str'
        x0 = float(self.x0_entry.get()) # Obtiene el valor ingresado en 'x0_entry' y lo convierte a un número de punto flotante para luego almacenar en x0.
        x1 = float(self.x1_entry.get()) # Se repite el proceso de x0, pero en x1.
        f = lambda x: eval(f_str) # Esta función se utilizará para calcular el método de la secante.
         # La función se utiliza una expresión lambda que toma un parámetro x y utiliza la función incorporada eval() para evaluar la expresión almacenada en f_str en ese valor de x.

        # Aplicar el método de la secante
        x, table = secante(f, x0, x1) #Aplica el metodo de la secante a la función y los valores iniciales. 
        
        # Mostrar el resultado y la tabla de iteraciones
        self.result_text.delete(1.0, tk.END) #Borra el contenido de result_text
        self.result_text.insert(tk.END, f"La raíz aproximada es: {round(x, 6)}") #Inserta en result_text el valor de la raiz de forma redondeada.
        self.table_text.delete(1.0, tk.END) #Borra el contenido de table_text.
        self.table_text.insert(tk.END, str(table)) #Inserta en table_text las iteraciones del metodo de la secante, almacenado en table.
        
# Crear la ventana principal
root = tk.Tk() # Crea una instancia de la clase Tk y la asigna a la variable root que representa la venta principal de la interfaz.

# Crear la interfaz gráfica
app = SecanteGUI(root) # Crea un objeto de la clase SecanteGUI y lo asigna a la variable app.

# Ejecutar la aplicación
root.mainloop()