# Sistema de Zonas y Precios

Herramienta para definir zonas geográficas (polígonos) con precios diferenciados por servicio.

## 🗺️ Editor de Zonas

**Archivo:** `mapa_poligonos.html`

### Cómo usar:

1. **Dibujar zonas**: Click en 🔷 (arriba derecha), luego click en el mapa para agregar vértices. Doble-click para cerrar.
2. **Editar forma**: Click en ✏️, arrastra los vértices del polígono
3. **Configurar precios**: En el sidebar, edita los 4 servicios (plagas, roedores, ulv, termo)
4. **Buscar dirección**: Ingresa una dirección para ver en qué zona cae
5. **Guardar**: Se guarda automáticamente en LocalStorage del browser

### Botones del sidebar:

- **📥 Exportar**: Genera JSON con todas las zonas (coordenadas + precios)
- **📤 Importar**: Carga zonas desde un JSON previamente exportado
- **⚡ Ver Función**: Muestra código listo para usar en tu backend

---

## 💾 Formato de datos (JSON)

Cuando exportas, obtienes algo así:

```json
[
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
  }
]
```

Cada zona tiene:
- `nombre`: Identificador legible
- `vertices`: Array de `[lat, lng]` que forman el polígono
- `precios`: Objeto con precio de cada servicio

---

## 🔧 Usar en tu código

### JavaScript

**Archivo:** `buscar_zona.js`

```javascript
const { buscarZona } = require('./buscar_zona.js');

// Buscar zona para una coordenada
const zona = buscarZona(-34.6011, -58.3833);

if (zona) {
    console.log(zona.nombre);      // "Zona Centro"
    console.log(zona.precios);     // { plagas: 40000, ... }
} else {
    console.log("Fuera de cobertura");
}
```

### Python

**Archivo:** `buscar_zona.py`

```python
from buscar_zona import buscar_zona

# Buscar zona para una coordenada
zona = buscar_zona(-34.6011, -58.3833)

if zona:
    print(zona['nombre'])      # "Zona Centro"
    print(zona['precios'])     # {'plagas': 40000, ...}
else:
    print("Fuera de cobertura")
```

---

## 📋 Workflow completo

1. **Diseñar zonas**: Abre `mapa_poligonos.html`, dibuja tus zonas, configura precios
2. **Exportar datos**: Click en "📥 Exportar", copia el JSON
3. **Pegar en código**: Abre `buscar_zona.js` o `buscar_zona.py`, reemplaza la variable `ZONAS` con tu JSON
4. **Integrar en tu app**: Usa la función `buscarZona(lat, lng)` para consultar zona y precios

---

## 🧮 Algoritmo

Usa **ray-casting** para determinar si un punto está dentro de un polígono:
- Traza una línea desde el punto hacia el infinito
- Cuenta cuántas veces cruza los bordes del polígono
- Si cruza un número impar de veces → está adentro
- Si cruza un número par de veces → está afuera

Complejidad: O(n) donde n = número de vértices del polígono.

---

## 🌍 Geolocalización

Actualmente usa **Nominatim** (OpenStreetMap) para convertir direcciones a coordenadas.

Alternativas para producción:
- **Google Geocoding API**: Mejor precisión en Argentina
- **georef.ar**: API del gobierno argentino, gratis, solo Argentina
- **Mapbox**: Buen balance calidad/precio

Para cambiar el servicio, modifica la línea del `fetch()` en el HTML.
