"""
Zonas definidas como CIRCULOS.
Toda direccion cae en el circulo mas cercano (nadie queda afuera).
"""
import math

# --- Definicion de circulos (hardcoded) ---
CIRCULOS = [
    {"nombre": "Obelisco",  "lat": -34.6037, "lng": -58.3816},
    {"nombre": "Palermo",   "lat": -34.5735, "lng": -58.4217},
    {"nombre": "La Boca",   "lat": -34.6345, "lng": -58.3633},
]

# --- Haversine: distancia entre dos puntos en km ---
def distancia_km(lat1, lng1, lat2, lng2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlng / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# --- Buscar el circulo mas cercano ---
def circulo_mas_cercano(lat, lng):
    mejor = None
    mejor_dist = float("inf")
    for circulo in CIRCULOS:
        dist = distancia_km(lat, lng, circulo["lat"], circulo["lng"])
        if dist < mejor_dist:
            mejor_dist = dist
            mejor = circulo
    return mejor["nombre"], round(mejor_dist, 3)

# --- Pruebas ---
PUNTOS_TEST = [
    {"nombre": "Teatro Colon",       "lat": -34.6011, "lng": -58.3833},
    {"nombre": "Plaza Italia",       "lat": -34.5806, "lng": -58.4212},
    {"nombre": "Caminito",           "lat": -34.6383, "lng": -58.3636},
    {"nombre": "Ezeiza",             "lat": -34.8222, "lng": -58.5358},
    {"nombre": "Aeroparque",         "lat": -34.5592, "lng": -58.4156},
    {"nombre": "Retiro",             "lat": -34.5925, "lng": -58.3747},
    {"nombre": "Constitucion",       "lat": -34.6275, "lng": -58.3817},
    {"nombre": "Liniers",            "lat": -34.6425, "lng": -58.5283},
    {"nombre": "San Isidro",         "lat": -34.4708, "lng": -58.5292},
    {"nombre": "Lanus",              "lat": -34.7000, "lng": -58.3900},
]

if __name__ == "__main__":
    print("=== CIRCULO MAS CERCANO (nadie queda afuera) ===\n")
    print(f"  Circulos definidos: {[c['nombre'] for c in CIRCULOS]}\n")

    for punto in PUNTOS_TEST:
        zona, dist = circulo_mas_cercano(punto["lat"], punto["lng"])
        print(f"  {punto['nombre']:20s} -> {zona:10s} ({dist} km)")
