# Gallery — Edición Español

**Gallery**: el visor de imágenes PNG/JPG para la HP Prime.

![Gallery](Images/cover.png)

> **Edición Español** — versión modificada y mejorada por **Miguel Ángel Rivera Ospina ("Belico")**, 2026,
> basada en el trabajo original de **Manuel Andrés Vélez**.
> Distribuida bajo licencia **GPL-3.0**, la misma del proyecto original.

## Créditos y licencia

Este proyecto es un **trabajo derivado** del Gallery original. Se respetan todos los términos de la licencia GPL-3.0:

| Rol | Autor |
|-----|-------|
| **Autor original** | Manuel Andrés Vélez — mandresve@hotmail.com |
| **Edición Español y mejoras** | Miguel Ángel Rivera Ospina ("Belico") — 2026 |
| **Licencia** | GPL-3.0 (se conserva la del original) |

**Aviso de modificación (GPL-3.0 §5a):** esta es una versión modificada del Gallery original.
El copyright del código base pertenece a su autor original, Manuel Andrés Vélez. Los cambios
introducidos en esta edición son de Miguel Ángel Rivera Ospina, 2026.

### Cambios en esta edición
- **Traducción completa de la interfaz al español** (menús, diálogos, mensajes y pantalla de bienvenida).
- **Mejora de rendimiento:** `Center_Fit` ahora calcula el escalado con una fórmula directa
  (`MIN(320/ancho, 240/alto)`) en lugar del antiguo bucle que reducía la imagen 1% por vuelta.
  Mismo resultado visual, pero instantáneo — especialmente notable en imágenes grandes.
- **Corrección de estabilidad:** el diálogo *"Ir a página"* ahora valida el rango del número
  ingresado. Antes, un número fuera de límites cerraba la app; ahora se ajusta al rango válido.

#### Mejoras pendientes (hoja de ruta)
- Filtrar la lista para mostrar solo imágenes (`.png`/`.jpg`) y evitar errores al abrir otros archivos.
- Reemplazar la recursión `Open_File`/`Read_Keyboard` por una máquina de estados (estabilidad con muchas imágenes).
- Convertir el muro de `IF` de `Read_Keyboard` en un `CASE`; unificar las 4 funciones de scroll duplicadas.
- Rehacer las imágenes del tutorial embebido en español.

## ¿Qué es Gallery?

Una aplicación en **HP-PPL** para ver imágenes PNG y JPG directamente en la calculadora
HP Prime (modelos G1 y G2), con soporte de zoom, desplazamiento (pan), inversión de colores
y navegación entre múltiples imágenes, tanto con el teclado como con la pantalla táctil.

## Instalación

1. **Verifica el firmware** de tu calculadora — asegúrate de tenerlo actualizado.
2. Descarga e instala el **HP Connectivity Kit** y el **HP Prime Virtual Emulator**.
3. Abre el **HP Connectivity Kit**. En el panel izquierdo, abre tu calculadora (o el emulador)
   y ubica la categoría **"Application Library"**.
4. Arrastra la carpeta **`Gallery.hpappdir`** y suéltala dentro de "Application Library".
5. ¡Listo! La app ya está instalada.

## Cargar imágenes

1. Copia tus imágenes (PNG/JPG) dentro de la carpeta **`Gallery.hpappdir`**.
2. **No borres el archivo `icon.png`** ni los archivos `*.hpapp...` — son esenciales para
   que la app funcione. Si falta `icon.png`, la app se declara dañada y no inicia.
3. Vuelve a arrastrar la carpeta `Gallery.hpappdir` a "Application Library" para transferirla.

**Especificaciones recomendadas:** 320×240 px, 8 bits de profundidad. La app soporta cualquier
tamaño, pero estas medidas dan la mejor fluidez. Comprimir las imágenes antes de subirlas
mejora el rendimiento y el espacio.

## Cómo se usa

| Acción | Control |
|--------|---------|
| Abrir el menú de la app | Botón **[View]** |
| Salir de la imagen / volver | Botón **[ON]** |
| Imagen anterior / siguiente | **D-Pad** izquierda / derecha |
| Invertir colores (modo oscuro) | Botón **[+/-]** |
| Pantalla en negro (blackout) | Botón **[DEL]** |
| Mover la imagen (teclado) | Teclas **[4] [8] [6] [2]** |
| Acercar / alejar (zoom) | Botones **[+]** / **[-]** |
| Restablecer zoom y posición | Tecla **[5]** |
| Ocultar la app | Botón **[HOME]** |

**Pantalla táctil:** arrastra con un dedo para mover la imagen; pellizca con dos dedos
para acercar o alejar.

## Opciones

Desde el menú **Opciones** puedes configurar: información de imagen en pantalla,
inversión de colores, ajuste a pantalla, orden inverso de la lista, velocidad de
desplazamiento y sensibilidad del zoom táctil.

## Modificar y compilar el código

El código fuente legible está en **`Gallery.hpp`** (lenguaje **HP-PPL**). El archivo que
realmente ejecuta la calculadora es el binario `Gallery.hpappdir/Gallery.hpappprgm`, que
**se genera automáticamente** desde el HP Connectivity Kit.

Para aplicar cambios:
1. En el HP Connectivity Kit, doble clic sobre la app Gallery en "Application Library".
2. Ve a la pestaña **"Program"**.
3. Pega el contenido de `Gallery.hpp` y **guarda** — la CK recompila el binario.
4. Prueba primero en el **emulador** antes de pasarlo a la calculadora física.

## Licencia

Este software se distribuye bajo la **Licencia Pública General de GNU v3.0 (GPL-3.0)**.
Puedes usarlo, estudiarlo, modificarlo y redistribuirlo libremente, siempre que conserves
esta misma licencia, mantengas los créditos del autor original e indiques los cambios
realizados. Consulta el archivo [LICENSE](LICENSE) para el texto completo.
