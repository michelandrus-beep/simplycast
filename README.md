<div align="center">

# Simply Cast (Versión en Español)

**Mezclador de vídeo para Windows. Emisión en vivo, grabación y streaming — gratis, sin claves ni suscripciones.**

[![Descargar](https://img.shields.io/github/v/release/michelandrus-beep/simplycast?label=descargar&style=for-the-badge&color=6c4fe0)](https://github.com/michelandrus-beep/simplycast/releases/latest)
![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078d4?style=for-the-badge&logo=windows11&logoColor=white)
![Android](https://img.shields.io/badge/control-Android-34d399?style=for-the-badge&logo=android&logoColor=white)

<img src="site/screenshot.png" alt="Simply Cast" width="900">

</div>

---

## 🇪🇸 Traducción al Español (Parcheador de Interfaz y Niveles de Audio)

Dado que SimplyCast no incluye archivos externos de traducción, este repositorio incluye un **script de parcheado automático en Python** (`patch_simplycast.py`) que traduce de forma segura la interfaz de usuario, los controles de emisión/grabación y todo el sistema de **mezclador y niveles de audio** a español sin corromper la integridad del ejecutable.

### Cómo aplicar la traducción en tu PC:

1. **Opción Rápida (1 Clic en Windows):**
   * Descarga o clona este repositorio.
   * Haz doble clic en **`parchear_a_espanol.bat`**.

2. **Opción por Línea de Comandos (PowerShell / CMD):**
   ```bash
   python patch_simplycast.py "C:\Users\baque\AppData\Local\Programs\SimplyCast\SimplyCast.exe"
   ```

*Nota:* El script crea automáticamente una copia de respaldo `SimplyCast.exe.original.bak` antes de realizar cualquier cambio. Si en algún momento deseas volver al ruso original, ejecuta:
```bash
python patch_simplycast.py --restore
```

---

## Características de Simply Cast

| | |
|---|---|
| 🎬 **Previo y Vivo** | Corte y transición automática, barra T (T-bar), 16 transiciones, overlays, salida a negro |
| 🎥 **Fuentes de entrada** | Cámaras, pantalla, vídeo, imágenes, NDI, páginas web, títulos, PDF y presentaciones de PowerPoint |
| 🖥 **PowerPoint** | Presentación en vivo con animaciones; reproducción fluida de vídeos de diapositivas incluso con GPU integrada, envío de audio al mixer |
| 📡 **Streaming y grabación** | Grabación a archivo, RTMP(S), SRT multidestino con codificación acelerada por hardware (NVIDIA / AMD) |
| 🔊 **Mezclador de audio** | Buses (A–G, Master), solo, AFV, vúmetros y niveles de volumen en LUFS |
| 🛡 **Estabilidad** | La caída de una cámara no interrumpe el vivo, reconexión automática de stream y recuperación de proyectos |
| 📱 **Control remoto Android** | Monitores en tiempo real, cambio y reordenación de entradas, y uso del teléfono como cámara inalámbrica |

---

## Inicio Rápido

1. Instala e inicia Simply Cast.
2. Aplica la traducción con `parchear_a_espanol.bat`.
3. Añade fuentes: cámara, captura de pantalla o archivo de vídeo.
4. Selecciona la entrada en previo y envíala a emisión (`Espacio`).
5. Haz clic en **«Transmitir»** o **«Grabar»**.

---

## Licencias

Simply Cast utiliza Qt y FFmpeg bajo licencia LGPL; los textos de las licencias se encuentran en la carpeta `licenses` del programa. NDI® es una marca registrada de Vizrt NDI AB.

Fork mantenido y traducido para la comunidad hispanohablante.