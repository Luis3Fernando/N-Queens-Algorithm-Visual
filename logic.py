from reinas import Reinas
from ag_reinas import AG_Reinas
import time

def resolver_n_reinas(n):
    problema = Reinas(n)
    problema.resolver()
    return problema.obtener_soluciones()

def resolver_AG_reinas(n):
    problema = AG_Reinas(n)
    problema.evolucionar()
    return problema.obtener_soluciones()  

def resolver_n_reinas_time(n):
    inicio = time.time()
    problema = Reinas(n)
    problema.resolver()
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return problema.obtener_soluciones(), tiempo_ejecucion

def resolver_AG_reinas_time(n):
    inicio = time.time()
    problema = AG_Reinas(n)
    problema.evolucionar()
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return problema.obtener_soluciones(), tiempo_ejecucion
