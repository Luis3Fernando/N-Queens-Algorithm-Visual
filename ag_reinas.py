import random
import time
import threading

class AG_Reinas:
    def __init__(self, n, tam_poblacion=100, prob_mutacion=0.1, max_generaciones=1000):
        """Inicializa el problema con parámetros para el AG."""
        self.n = n
        self.tam_poblacion = tam_poblacion
        self.prob_mutacion = prob_mutacion
        self.max_generaciones = max_generaciones
        self.poblacion = []
        self.soluciones = []
        self.tiempo_ejecucion = 0

    def generar_poblacion_inicial(self):
        """Genera una población inicial de soluciones."""
        self.poblacion = [random.sample(range(self.n), self.n) for _ in range(self.tam_poblacion)]

    def aptitud(self, tablero):
        """Calcula la aptitud de un tablero (menos conflictos, mejor aptitud)."""
        conflictos = 0
        for col1 in range(self.n):
            for col2 in range(col1 + 1, self.n):
                if tablero[col1] == tablero[col2] or abs(tablero[col1] - tablero[col2]) == abs(col1 - col2):
                    conflictos += 1
        return -conflictos

    def seleccionar_padres(self):
        """Selecciona padres usando selección por torneo."""
        padres = []
        for _ in range(self.tam_poblacion // 2):
            torneo = random.sample(self.poblacion, 3)
            mejor = max(torneo, key=self.aptitud)
            padres.append(mejor)
        return padres

    def cruzar(self, padre1, padre2):
        """Realiza el crossover entre dos padres."""
        punto = random.randint(1, self.n - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2

    def mutar(self, tablero):
        """Muta un tablero cambiando una reina de lugar."""
        if random.random() < self.prob_mutacion:
            col = random.randint(0, self.n - 1)
            fila = random.randint(0, self.n - 1)
            tablero[col] = fila
        return tablero

    def evolucionar(self):
        """Evoluciona la población hasta encontrar una solución válida."""
        self.generar_poblacion_inicial()
        for generacion in range(self.max_generaciones):
            nueva_poblacion = []
            padres = self.seleccionar_padres()
            for i in range(0, len(padres), 2):
                padre1, padre2 = padres[i], padres[(i + 1) % len(padres)]
                hijo1, hijo2 = self.cruzar(padre1, padre2)
                nueva_poblacion.append(self.mutar(hijo1))
                nueva_poblacion.append(self.mutar(hijo2))
            
            self.poblacion = nueva_poblacion
            mejor = max(self.poblacion, key=self.aptitud)
            if self.aptitud(mejor) == 0:
                self.soluciones.append(mejor)
                break

    def calcular_tiempo(self):
        """Calcula el tiempo que toma encontrar una solución válida."""
        inicio = time.time()
        self.evolucionar()
        fin = time.time()
        self.tiempo_ejecucion = fin - inicio

    def calcular_tiempo_hilo(self):
        """Calcula el tiempo en un hilo separado."""
        hilo = threading.Thread(target=self.calcular_tiempo)
        hilo.start()
        hilo.join()

    def obtener_tiempo_ejecucion(self):
        """Retorna el tiempo que tomó encontrar la solución."""
        return self.tiempo_ejecucion

    def obtener_soluciones(self):
        """Retorna las soluciones encontradas por el AG."""
        return self.soluciones

    def solucion_optima(self):
        return self.soluciones[0] if self.soluciones else None
