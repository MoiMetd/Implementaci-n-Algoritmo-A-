import heapq


grafo = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Eforie': {'Hirsova': 86},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Urziceni': {'Hirsova': 98, 'Vaslui': 142, 'Iasi': 92},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92, 'Neamt': 87},
    'Iasi': {'Urziceni': 92, 'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87, 'Sinaia': 84},
    'Sinaia': {'Neamt': 84, 'Bucharest': 246}
}



def costo(gfo, c1, c2):
    return gfo[c1][c2]



heuristica = {
    'Arad': 366,'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,'Iasi': 226,
    'Lugoj': 244, 'Mehadia': 241,'Neamt': 234,'Oradea': 380,'Pitesti': 98,'Rimnicu Vilcea': 193,'Sibiu': 253,'Sinaia': 140,'Timisoara': 329,
    'Urziceni': 80,'Vaslui': 142,'Zerind': 374
}


def a_estrella(gfo, costo, heuristica, inicio, fin):
    abierto = []
    cerrado = set()
    heapq.heappush(abierto, (0, inicio))
    csa = {inicio: 0}
    camino = {inicio: None}

    while abierto:
        _, c_actual = heapq.heappop(abierto)
        if c_actual == fin:
            break
        cerrado.add(c_actual)

        for c_siguiente in gfo[c_actual]:
            if c_siguiente in cerrado:
                continue
            costo_nuevo = csa[c_actual] + costo(grafo, c_actual, c_siguiente)
            if c_siguiente not in csa or costo_nuevo < csa[c_siguiente]:
                csa[c_siguiente] = costo_nuevo
                prioridad = costo_nuevo + heuristica[c_siguiente]
                heapq.heappush(abierto, (prioridad, c_siguiente))
                camino[c_siguiente] = c_actual


    camino_optimo = []
    c_actual = fin
    while c_actual is not None:
        camino_optimo.append(c_actual)
        c_actual = camino.get(c_actual)
    camino_optimo.reverse()

    print("La mejor ruta para el mapa rodoviario es:", " -> ".join(camino_optimo))
    print("Y su costo total es:", csa[fin])

    return camino_optimo, csa[fin]


inicio = 'Arad'
fin = 'Bucharest'
a_estrella(grafo, costo, heuristica, inicio, fin)