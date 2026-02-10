/**
 * Función standalone para buscar zona por coordenadas
 *
 * Uso:
 * 1. Exporta tus zonas desde el mapa (botón "Exportar")
 * 2. Pega el JSON en la constante ZONAS
 * 3. Llama a buscarZona(lat, lng)
 */

// === PEGA TUS ZONAS EXPORTADAS AQUI ===
const ZONAS = [
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
];

/**
 * Algoritmo ray-casting para determinar si un punto está dentro de un polígono
 */
function puntoEnPoligono(lat, lng, vertices) {
    let dentro = false;
    let j = vertices.length - 1;

    for (let i = 0; i < vertices.length; i++) {
        const [yi, xi] = vertices[i];
        const [yj, xj] = vertices[j];

        if ((yi > lat) !== (yj > lat) &&
            lng < (xj - xi) * (lat - yi) / (yj - yi) + xi) {
            dentro = !dentro;
        }
        j = i;
    }

    return dentro;
}

/**
 * Busca en qué zona cae una coordenada
 * @param {number} lat - Latitud
 * @param {number} lng - Longitud
 * @returns {Object|null} Zona encontrada con { nombre, vertices, precios } o null
 */
function buscarZona(lat, lng) {
    for (const zona of ZONAS) {
        if (puntoEnPoligono(lat, lng, zona.vertices)) {
            return zona;
        }
    }
    return null; // No encontrada
}

// === EJEMPLO DE USO ===
if (require.main === module) {
    // Pruebas
    const pruebas = [
        { nombre: "Teatro Colón", lat: -34.6011, lng: -58.3833 },
        { nombre: "Palermo", lat: -34.5806, lng: -58.4212 },
        { nombre: "Fuera", lat: -34.8222, lng: -58.5358 }
    ];

    console.log("=== Prueba de búsqueda de zonas ===\n");

    for (const punto of pruebas) {
        const zona = buscarZona(punto.lat, punto.lng);

        if (zona) {
            console.log(`${punto.nombre}:`);
            console.log(`  Zona: ${zona.nombre}`);
            console.log(`  Precios:`, zona.precios);
        } else {
            console.log(`${punto.nombre}: FUERA de todas las zonas`);
        }
        console.log();
    }
}

// Export para usar en otros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { buscarZona, puntoEnPoligono, ZONAS };
}
