# Cotizador de Control de Plagas — Zonas y Precios

Aplicación web para vendedores. Se ingresa la dirección del cliente, el mapa detecta la zona y muestra los precios por tratamiento. La calculadora arma la cotización y genera dos salidas: el mensaje para el cliente (WhatsApp) y la ficha interna `[FICHA-ASESOR]`.

Es un único HTML estático, sin backend ni build. Se puede servir desde GitHub Pages, Hostinger o cualquier hosting estático.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | La aplicación cotizadora |
| `ZONAS.md` | Localidad → zona (lo usa el bot) |
| `PRECIOS.md` | Precios por zona, servicio, rango y franja + insumos (lo usa el bot) |
| `herramientas/editor-zonas.html` | Editor/calibrador que regenera `ZONAS.md` y `PRECIOS.md` |
| `PENDIENTES.md` | Mejoras y tareas abiertas |

## Buscador de direcciones

Mientras se escribe la calle y la altura, aparece una lista de coincidencias con localidad y partido (Photon/OpenStreetMap, con Georef como respaldo). Se elige la correcta y el mapa la ubica. La localidad elegida se cruza con `ZONAS.md` y avisa si no coincide con la zona del mapa. **Para que el cruce funcione, `ZONAS.md` tiene que estar publicado junto a `index.html`.**

## Cómo funciona la zona

1. **CABA** = polígono de 48 vértices (Gral. Paz, Riachuelo, Río de la Plata) → 0%.
2. Fuera de CABA: distancia en línea recta desde el **Obelisco** (-34.6037, -58.3816).

| Zona | Distancia | Aumento |
|---|---|---|
| CABA (Muy Cercano) | Polígono | 0% |
| Cercano | hasta 20 km | +10% |
| Media Distancia | 20 a 30 km | +25% |
| Lejano | 30 a 40 km | +35% |
| Muy Lejano | 40 a 69 km | +50% |
| Fuera de cobertura | más de 69 km | derivar |

Calibrado el 25/09/2026 contra `ZONAS.md`: coinciden 238 de 241 localidades del GBA. Las tres restantes están en el borde de una zona.

## Precios

Coinciden con `PRECIOS.md` (verificado en las 450 líneas de precio).

- Servicio = base × 1,25 por cada rango de m² × aumento de zona × ajuste de franja.
- Franjas (solo sobre el servicio): 17–20 +20%, 20–22 +35%, 22–00:30 +50%, sábado 9–12:30 +20%. Domingo no hay servicio.
- Combo de dos servicios: el mayor va pleno y el menor al 40%.
- Los insumos se suman sin ajuste de franja.
- Todo es sin IVA. El IVA (21%) aparece solo como referencia en la ficha del asesor.
- Más de 5000 m² → derivar.

**Al cliente nunca se le muestran ni la zona ni los porcentajes.**

## Actualizar precios o zonas

1. Abrir `herramientas/editor-zonas.html` en el navegador donde se calibró. Las zonas quedan guardadas en ese navegador.
2. Ajustar y exportar `ZONAS.md` + `PRECIOS.md`.
3. Si cambian los precios base, los radios o el centro, actualizar también las constantes `SERVICIOS`, `INSUMO_PRECIOS`, `ZONAS` y `CABA_CENTER` en `index.html`.

## Desplegar

Subir `index.html` y `ZONAS.md` a la raíz del hosting. No tiene dependencias locales: Leaflet y los mapas se cargan desde internet, y las direcciones se geocodifican con Nominatim (OpenStreetMap).
