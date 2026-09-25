# Pendientes

Actualizado: 25/09/2026

## 1. Buscador de direcciones con sugerencias (prioridad alta)

**Problema:** el buscador actual (Nominatim) toma el primer resultado y exige escribir la dirección exacta. Hay muchas calles con el mismo nombre en distintas localidades ("Maipú 1000" existe en CABA, Florida, Banfield, Ramos Mejía, Claypole, Merlo, Escobar…). Si toma la equivocada, la zona y el precio salen mal sin que nadie lo note.

**Solución propuesta:** que, mientras el vendedor escribe, aparezca una lista de opciones con la localidad y el partido, y que se elija una.

```
[ Maipu 1000                          ]
  ▸ Maipú 1000 — CABA
  ▸ Av. Maipú 1000 — Florida, Vicente López
  ▸ Maipú 1000 — Banfield, Lomas de Zamora
  ▸ Maipú 1000 — Ramos Mejía, La Matanza
```

Cómo implementarla (sin backend, sin costo):

| Pieza | Qué hace | Probado 25/09 |
|---|---|---|
| **Photon** (`photon.komoot.io/api`) | Sugerencias mientras se escribe. Gratis, basada en OpenStreetMap y pensada para autocompletar. Se sesga hacia el Obelisco (`lat`/`lon`) para que salgan primero las del AMBA | "maipu 1000" → CABA, Florida, Banfield, Ramos Mejía, Claypole |
| **Georef** (`apis.datos.gob.ar/georef/api/direcciones`) | API oficial del Estado. Normaliza calle y altura, y devuelve partido y coordenadas. Se usa como respaldo, filtrando `provincia=02,06` | "Maipu 1000" → 37 resultados con partido |

Detalles:
- Buscar recién con 3 letras y esperar unos 300 ms después de la última tecla, para no saturar el servicio.
- Mostrar hasta 6–8 opciones, filtrar las que quedan a más de 69 km y ordenar por distancia al Obelisco.
- Al elegir una opción: marcarla en el mapa, calcular la zona por círculo y, además, **cruzar la localidad contra ZONAS.md**. Si no coinciden, mostrar un aviso ("verificar dirección").
- Mantener Enter + Nominatim como alternativa si la lista no trae nada.
- No usar Nominatim para autocompletar: su política de uso lo prohíbe.
- Alternativa paga: Google Places Autocomplete es la más precisa, pero requiere API key, facturación y exponer la key en el HTML. Solo conviene si Photon o Georef no alcanzan.

## 2. Seguridad

- [ ] **Revocar el token de GitHub** que estaba escrito en la URL del remoto de este repo (GitHub → Settings → Developer settings → Personal access tokens). El remoto ya usa SSH, pero el token sigue activo hasta que se revoque.

## 3. Separar el proyecto

- [ ] Definir la estructura final: la app (este repo) por un lado y el bot/skill (`asistente-ventas-plagas-skill`) por el otro.
- [ ] El skill todavía publica su copia vieja de `index.html` en GitHub Pages (precios y círculos de febrero). Cuando los vendedores pasen a la URL nueva, borrarla o redirigirla.
- [ ] Hacer commit de los cambios del skill. Quedaron sin commitear porque estaban mezclados con trabajo previo (fichas/, CATALOGO.md y archivos borrados).
- [ ] Limpiar el formato roto de `INSUMOS.md` del skill (cada línea empieza con `#`).
- [ ] Decidir cómo sincronizar `ZONAS.md` y `PRECIOS.md` entre este repo y el skill. Hoy están copiados en los dos.

## 4. Deploy

- [ ] Subir `index.html` a Hostinger con el sistema propio.
- [ ] Opcional: activar GitHub Pages en este repo para tener una URL de prueba.

## 5. Datos de zonas (menores)

- [ ] "Lomas de Zamora Centro" no se pudo geocodificar al calibrar. Verificar a mano que caiga en Media Distancia.
- [ ] Haedo cae justo a 20,0 km (límite Cercano / Media Distancia). Confirmar la zona que corresponde.
- [ ] Las constantes de `index.html` (`SERVICIOS`, `INSUMO_PRECIOS`, `ZONAS`, `CABA_CENTER`) se mantienen a mano. A futuro, que el editor de zonas exporte también un `config.js` que lea la app, así no hay que tocar código al cambiar precios.
