import threading
import time

class Reinas:
    def __init__(self, n):
        """Inicializa el problema con el tamaño del tablero."""
        self.n = n
        self.soluciones = []
        self.tiempo_ejecucion = 0

    def es_valido(self, tablero, fila, col):
        """Verifica si es seguro colocar una reina en la posición (fila, col)."""
        for i in range(col):
            if tablero[i] == fila or \
               abs(tablero[i] - fila) == abs(i - col):
                return False
        return True

    def backtrack(self, tablero, col):
        """Resuelve el problema de forma recursiva usando backtracking."""
        if col == self.n:
            self.soluciones.append(tablero[:])
            return
        
        for fila in range(self.n):
            if self.es_valido(tablero, fila, col):
                tablero[col] = fila
                self.backtrack(tablero, col + 1)

    def resolver(self):
        """Encuentra todas las soluciones posibles."""
        tablero = [-1] * self.n
        self.backtrack(tablero, 0)

    def obtener_soluciones(self):
        """Retorna la lista de soluciones."""
        return self.soluciones

    def solucion_optima(self):
        """Retorna la primera solución encontrada."""
        return self.soluciones[0] if self.soluciones else None

    def ejecutar_resolver_con_tiempo(self):
        """Ejecuta el método resolver y mide el tiempo de ejecución."""
        inicio = time.time()
        self.resolver()
        fin = time.time()
        self.tiempo_ejecucion = fin - inicio

    def calcular_tiempo(self):
        """Ejecuta el cálculo de soluciones en un hilo y mide el tiempo."""
        hilo = threading.Thread(target=self.ejecutar_resolver_con_tiempo)
        hilo.start()
        hilo.join()

    def obtener_tiempo_ejecucion(self):
        """Retorna el tiempo que tomó encontrar las soluciones."""
        return self.tiempo_ejecucion