# Pendientes

Actualizado: 25/09/2026

## 1. Buscador de direcciones con sugerencias — HECHO (25/09/2026)

Implementado en `index.html`:
- Mientras se escribe (3+ letras, espera 300 ms) aparece una lista de direcciones con localidad, partido y km. Se elige con el mouse o con las flechas + Enter.
- Fuente: Photon, sesgado al Obelisco y filtrado a 75 km. Si Photon no trae nada, usa Georef. Sin lista, Enter busca con Nominatim como antes.
- Al elegir, cruza la localidad con `ZONAS.md`: muestra ✓ si coincide o ⚠ si difiere, si el partido tiene varias zonas o si la localidad no figura.
- El cruce necesita que `ZONAS.md` esté en el mismo servidor que `index.html`. Abriendo el HTML como archivo local, el cruce no aparece.

Seguimiento:
- [ ] Probar con los vendedores direcciones reales difíciles (countries, barrios cerrados, calles sin altura).
- [ ] Photon es un servicio público gratuito, sin garantía de disponibilidad. Si se cae seguido, evaluar alojar Photon propio o pasar a Google Places.

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
