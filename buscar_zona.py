"""
Función standalone para buscar zona por coordenadas

Uso:
1. Exporta tus zonas desde el mapa (botón "Exportar")
2. Pega el JSON en la variable ZONAS
3. Llama a buscar_zona(lat, lng)
"""

# === PEGA TUS ZONAS EXPORTADAS AQUI ===
ZONAS = [
    {
        "nombre": "Zona Centro",
        "vertices": [
            [-34.60, -58.45],
            [-34.60, -58.40],
            [-34.65, -58.40],
            [-34.65, -58.45]
        ],
        "precios": {
            "plagas": 40000,
            "roedores": 50000,
            "ulv": 60000,
            "termo": 120000
        }
    },
    {
        "nombre": "Zona Norte",
        "vertices": [
            [-34.55, -58.45],
            [-34.55, -58.40],
            [-34.60, -58.40],
            [-34.60, -58.45]
        ],
        "precios": {
            "plagas": 50000,
            "roedores": 62500,
            "ulv": 75000,
            "termo": 150000
        }
    }
]


def punto_en_poligono(lat: float, lng: float, vertices: list) -> bool:
    """
    Algoritmo ray-casting para determinar si un punto está dentro de un polígono
    """
    dentro = False
    j = len(vertices) - 1

    for i in range(len(vertices)):
        yi, xi = vertices[i]
        yj, xj = vertices[j]

        if ((yi > lat) != (yj > lat)) and \
           (lng < (xj - xi) * (lat - yi) / (yj - yi) + xi):
            dentro = not dentro

        j = i

    return dentro


def buscar_zona(lat: float, lng: float) -> dict | None:
    """
    Busca en qué zona cae una coordenada

    Args:
        lat: Latitud
        lng: Longitud

    Returns:
        Diccionario con { nombre, vertices, precios } o None si no se encuentra
    """
    for zona in ZONAS:
        if punto_en_poligono(lat, lng, zona["vertices"]):
            return zona

    return None  # No encontrada


# === EJEMPLO DE USO ===
if __name__ == "__main__":
    pruebas = [
        {"nombre": "Teatro Colón", "lat": -34.6011, "lng": -58.3833},
        {"nombre": "Palermo", "lat": -34.5806, "lng": -58.4212},
        {"nombre": "Fuera", "lat": -34.8222, "lng": -58.5358}
    ]

    print("=== Prueba de búsqueda de zonas ===\n")

    for punto in pruebas:
        zona = buscar_zona(punto["lat"], punto["lng"])

        if zona:
            print(f"{punto['nombre']}:")
            print(f"  Zona: {zona['nombre']}")
            print(f"  Precios: {zona['precios']}")
        else:
            print(f"{punto['nombre']}: FUERA de todas las zonas")
        print()
