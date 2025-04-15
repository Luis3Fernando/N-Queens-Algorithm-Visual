from logic import *

n = 12
soluciones_1, tiempo_1 = resolver_n_reinas_time(n)
soluciones_2, tiempo_2 = resolver_AG_reinas_time(n)

print(f"Algoritmo Matematico: Tiempo de solución en {tiempo_1:.4f} segundos.")
print(f"Algoritmo Genético: Tiempo de solución en {tiempo_2:.4f} segundos.")