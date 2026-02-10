"""
Enfoque 2: Zonas definidas como POLIGONOS (lista de vertices)
Sin dependencias externas. Usa ray-casting para point-in-polygon.
"""

# --- Definicion de zonas como poligonos (hardcoded) ---
# Cada zona es una lista de (lat, lng) que forman un poligono cerrado
ZONAS = [
    {
        "nombre": "Microcentro",
        "vertices": [
            (-34.5950, -58.3850),
            (-34.5950, -58.3700),
            (-34.6100, -58.3700),
            (-34.6100, -58.3850),
        ],
    },
    {
        "nombre": "Palermo Soho",
        "vertices": [
            (-34.5830, -58.4320),
            (-34.5830, -58.4180),
            (-34.5920, -58.4180),
            (-34.5920, -58.4320),
        ],
    },
    {
        "nombre": "La Boca (triangulo)",
        "vertices": [
            (-34.6300, -58.3700),
            (-34.6400, -58.3550),
            (-34.6400, -58.3700),
        ],
    },
]

# --- Ray-casting: punto dentro de poligono? ---
def punto_en_poligono(lat, lng, vertices):
    n = len(vertices)
    dentro = False
    j = n - 1
    for i in range(n):
        yi, xi = vertices[i]
        yj, xj = vertices[j]
        if ((yi > lat) != (yj > lat)) and (lng < (xj - xi) * (lat - yi) / (yj - yi) + xi):
            dentro = not dentro
        j = i
    return dentro

# --- Buscar en que zona(s) cae un punto ---
def buscar_zonas(lat, lng):
    resultados = []
    for zona in ZONAS:
        if punto_en_poligono(lat, lng, zona["vertices"]):
            resultados.append(zona["nombre"])
    return resultados

# --- Pruebas ---
PUNTOS_TEST = [
    {"nombre": "Teatro Colon",     "lat": -34.6011, "lng": -58.3833},
    {"nombre": "Plaza Italia",     "lat": -34.5806, "lng": -58.4212},
    {"nombre": "Caminito",         "lat": -34.6383, "lng": -58.3636},
    {"nombre": "Ezeiza (afuera)",  "lat": -34.8222, "lng": -58.5358},
    {"nombre": "Florida y Lavalle","lat": -34.6020, "lng": -58.3780},
]

if __name__ == "__main__":
    print("=== ENFOQUE POLIGONOS (vertices) ===\n")

    for punto in PUNTOS_TEST:
        zonas = buscar_zonas(punto["lat"], punto["lng"])
        if zonas:
            for z in zonas:
                print(f"  {punto['nombre']:20s} -> {z}")
        else:
            print(f"  {punto['nombre']:20s} -> FUERA de todas las zonas")
    print()
