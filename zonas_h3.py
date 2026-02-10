"""
Enfoque 3: Zonas definidas como CELDAS H3 (hexagonos de Uber)
Requiere: pip install h3
"""
try:
    import h3
except ImportError:
    print("Necesitas instalar h3: pip install h3")
    exit(1)

# --- Definir zonas como conjuntos de celdas H3 ---
# Resolucion 7 = hexagonos de ~5km2, resolucion 9 = ~0.1km2
RESOLUCION = 8  # ~0.7 km2 por celda

# Generamos zonas a partir de un centro + anillo de celdas
def crear_zona_desde_centro(lat, lng, anillos=2):
    """Crea una zona con la celda central + N anillos alrededor."""
    celda_central = h3.latlng_to_cell(lat, lng, RESOLUCION)
    celdas = h3.grid_disk(celda_central, anillos)
    return celdas

ZONAS = {
    "Obelisco": crear_zona_desde_centro(-34.6037, -58.3816, anillos=2),
    "Palermo":  crear_zona_desde_centro(-34.5735, -58.4217, anillos=3),
    "La Boca":  crear_zona_desde_centro(-34.6345, -58.3633, anillos=1),
}

# --- Buscar en que zona(s) cae un punto ---
def buscar_zonas(lat, lng):
    celda = h3.latlng_to_cell(lat, lng, RESOLUCION)
    resultados = []
    for nombre, celdas in ZONAS.items():
        if celda in celdas:
            resultados.append(nombre)
    return resultados, celda

# --- Pruebas ---
PUNTOS_TEST = [
    {"nombre": "Teatro Colon",     "lat": -34.6011, "lng": -58.3833},
    {"nombre": "Plaza Italia",     "lat": -34.5806, "lng": -58.4212},
    {"nombre": "Caminito",         "lat": -34.6383, "lng": -58.3636},
    {"nombre": "Ezeiza (afuera)",  "lat": -34.8222, "lng": -58.5358},
]

if __name__ == "__main__":
    print("=== ENFOQUE H3 (hexagonos) ===\n")

    print(f"  Resolucion: {RESOLUCION}")
    for nombre, celdas in ZONAS.items():
        print(f"  Zona '{nombre}': {len(celdas)} celdas")
    print()

    for punto in PUNTOS_TEST:
        zonas, celda = buscar_zonas(punto["lat"], punto["lng"])
        if zonas:
            for z in zonas:
                print(f"  {punto['nombre']:20s} -> {z} (celda: {celda})")
        else:
            print(f"  {punto['nombre']:20s} -> FUERA (celda: {celda})")
    print()
