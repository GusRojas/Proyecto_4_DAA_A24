from grafos4daa import *

# Crear grafo
n = 250  # Numero de nodos 
d = 2  
grafo = grafoBarabasiAlbert(n, d)
grafo.guardar_grafo2("grafo_barabasi250.gv")

# Kruskal directo
mst_kruskal_d, valor_mst_kd = grafo.KruskalD()
grafo.guardar_grafo_mst('mst_kruskal_d.gv', mst_kruskal_d)
print(f"Peso total del MST Kruskal Directo: {valor_mst_kd}")

# Kruskal indirecto
mst_kruskal_i, valor_mst_ki = grafo.KruskalI()
grafo.guardar_grafo_mst('mst_kruskal_i.gv', mst_kruskal_i)
print(f"Peso total del MST Kruskal inverso: {valor_mst_ki}")

# Prim
mst_prim, valor_mst_prim = grafo.Prim()
grafo.guardar_grafo_mst('mst_prim.gv', mst_prim)
print(f"Peso total del MST con Prim: {valor_mst_prim}")

print("Arboles de expanción mínima guardados")