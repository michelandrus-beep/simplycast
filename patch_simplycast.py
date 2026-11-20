#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimplyCast - Parcheador de Idioma a Español
Traduce la interfaz, controles de emisión, grabación y niveles de audio del ejecutable SimplyCast.exe.
"""

import sys
import os
import shutil
import argparse

TRANSLATIONS_U16 = [
    # Audio / Mixer / Niveles
    ('Микшер', 'Mixer'),
    ('Мастер', 'Master'),
    ('Шина', 'Bus'),
    ('Шины', 'Buses'),
    ('Громкость', 'Volumen'),
    ('Звук', 'Audio'),
    ('Только звук', 'Solo audio'),
    ('уровни', 'niveles'),
    ('Уровень', 'Nivel'),
    ('Звук клиппит', 'Audio satura'),
    ('Звук слишком тихий или клиппит', 'Audio muy bajo o saturado'),
    ('уменьшите громкость', 'reduzca el volumen'),
    ('Нет входов со звуком', 'Sin entradas audio'),
    ('Открыть микшер', 'Abrir mixer'),
    ('маршруты звука', 'rutas de audio'),
    ('задержка звука', 'retardo audio'),

    # Emisión / Grabación / Vivo
    ('Выйти в эфир', 'Transmitir'),
    ('В ЭФИРЕ', 'EN VIVO'),
    ('Завершить эфир', 'Terminar vivo'),
    ('Настройки эфира…', 'Ajustes vivo…'),
    ('В эфир', 'En vivo'),
    ('Эфир', 'Vivo'),
    ('Превью', 'Previo'),
    ('Запись', 'Grabar'),
    ('Начать запись', 'Iniciar grab.'),
    ('Остановить', 'Detener'),
    ('Пауза', 'Pausa'),

    # Fuentes / Entradas
    ('Входы', 'Entr.'),
    ('+ Вход', '+ Ent.'),
    ('Камера', 'Cámara'),
    ('Экран', 'Pant.'),
    ('Окно', 'Vent.'),
    ('Видео', 'Vídeo'),
    ('Картинка', 'Imagen'),
    ('Браузер', 'Naveg.'),
    ('Цвет', 'Color'),
    ('Без камеры', 'Sin cámara'),
    ('Без микрофона', 'Sin micro'),

    # Menú / Proyectos / Ajustes
    ('Новый проект', 'Nuevo proy.'),
    ('Открыть…', 'Abrir…'),
    ('Последние проекты', 'Proy. recientes'),
    ('Сохранить', 'Guardar'),
    ('Сохранить как…', 'Guardar como…'),
    ('Настройки', 'Ajustes'),
    ('Все настройки программы', 'Todos los ajustes prog.'),
    ('Помощь', 'Ayuda'),
    ('Выход', 'Salir'),
    ('Мониторы', 'Pantalla'),
    ('Виртуальная камера', 'Cámara virtual'),
    ('Установить камеру в Windows…', 'Instalar cámara en Windows…'),
    ('NDI-выход', 'Sal. NDI'),

    # Diseños y Pantallas
    ('Раскладка «Много входов»', 'Diseño «Muchos inputs»'),
    ('Раскладка «Два экрана»', 'Diseño «Dos pantallas»'),
    ('Мои раскладки', 'Mis diseños'),
    ('Удалить раскладку', 'Eliminar diseño'),
    ('Рисовать поверх эфира', 'Dibujar sobre vivo'),
    ('Оверлеи: что показано поверх эфира', 'Overlays: qué se ve sobre el vivo'),
    ('Импорт сцены из OBS…', 'Importar desde OBS…'),
    ('Импорт проекта vMix…', 'Importar desde vMix'),
    ('Всё готово к эфиру', 'Listo para el vivo'),
    ('Всё равно начать', 'Comenzar igual'),
    ('Выполнить сейчас', 'Ejecutar ahora'),
    ('Вкл', 'On'),
    ('Вперёд', 'Avance')
]

TRANSLATIONS_U8 = [
    ('Микшер', 'Mixer '),
    ('Входы', 'Entr.'),
    ('Вход', 'Ent.'),
    ('Запись', 'Grabar'),
    ('Мастер', 'Master'),
    ('Громкость', 'Volumen  '),
    ('уровни', 'niveles'),
    ('Уровень', 'Nivel  '),
    ('Без камеры', 'Sin cámara'),
    ('Без микрофона', 'Sin micro    '),
    ('Вкл', 'On '),
    ('Вперёд', 'Avance'),
    ('Всё готово к эфиру', 'Listo para el vivo'),
    ('Всё равно начать', 'Comenzar igual  '),
    ('Выполнить сейчас', 'Ejecutar ahora  '),
    ('Звук слишком тихий или клиппит', 'Audio muy bajo o saturado     '),
    ('Master выше −1 дБ или ниже −40 дБ дольше, с', 'Master > −1 dB o < −40 dB por más tiempo, s')
]

def fit(ru_text, es_text, encoding):
    """Ajusta la longitud exacta en bytes de la cadena en español a la original en ruso."""
    target_len = len(ru_text.encode(encoding))
    es_bytes = es_text.encode(encoding)
    if len(es_bytes) > target_len:
        char_unit = len(' '.encode(encoding))
        max_chars = target_len // char_unit
        es_bytes = es_text[:max_chars].encode(encoding)
    space = ' '.encode(encoding)
    diff = target_len - len(es_bytes)
    return es_bytes + space * (diff // len(space))

def find_target_exe(custom_path=None):
    """Encuentra la ruta a SimplyCast.exe."""
    if custom_path and os.path.isfile(custom_path):
        return custom_path

    # Rutas comunes en Windows
    candidates = []
    local_app_data = os.environ.get('LOCALAPPDATA', '')
    if local_app_data:
        candidates.append(os.path.join(local_app_data, 'Programs', 'SimplyCast', 'SimplyCast.exe'))
    
    userprofile = os.environ.get('USERPROFILE', '')
    if userprofile:
        candidates.append(os.path.join(userprofile, 'AppData', 'Local', 'Programs', 'SimplyCast', 'SimplyCast.exe'))

    candidates.append(r'C:\Users\baque\AppData\Local\Programs\SimplyCast\SimplyCast.exe')
    candidates.append('SimplyCast.exe')

    for c in candidates:
        if os.path.isfile(c):
            return c
    return None

def patch(target_path):
    print(f"[*] Archivo objetivo: {target_path}")

    bak_path = target_path + ".original.bak"
    if not os.path.exists(bak_path):
        print(f"[*] Creando copia de seguridad: {bak_path}")
        shutil.copy2(target_path, bak_path)
    else:
        print(f"[+] Copia de seguridad existente encontrada: {bak_path}")

    with open(target_path, 'rb') as f:
        data = f.read()

    patched = data
    count_u16 = 0
    for ru, es in TRANSLATIONS_U16:
        ru_b = ru.encode('utf-16le')
        es_b = fit(ru, es, 'utf-16le')
        c = patched.count(ru_b)
        if c > 0:
            patched = patched.replace(ru_b, es_b)
            count_u16 += c
            print(f"  [UTF-16] '{ru}' -> '{es.strip()}' ({c} ocurrencias)")

    count_u8 = 0
    for ru, es in TRANSLATIONS_U8:
        ru_b = ru.encode('utf-8')
        es_b = fit(ru, es, 'utf-8')
        c = patched.count(ru_b)
        if c > 0:
            patched = patched.replace(ru_b, es_b)
            count_u8 += c
            print(f"  [UTF-8]  '{ru}' -> '{es.strip()}' ({c} ocurrencias)")

    if len(patched) != len(data):
        print("[!] ERROR: La integridad del tamaño del binario no coincide. Cancelando escritura.")
        sys.exit(1)

    with open(target_path, 'wb') as f:
        f.write(patched)

    print("-" * 60)
    print(f"[✓] ¡Traducción completada con éxito!")
    print(f"[✓] Se tradujeron {count_u16 + count_u8} textos clave de la interfaz y controles de audio.")
    print(f"[✓] Puedes abrir SimplyCast ahora.")

def restore(target_path):
    bak_path = target_path + ".original.bak"
    if os.path.exists(bak_path):
        print(f"[*] Restaurando copia original desde: {bak_path}")
        shutil.copy2(bak_path, target_path)
        print("[✓] Restauración completada.")
    else:
        print(f"[!] No se encontró copia de seguridad en: {bak_path}")

def main():
    parser = argparse.ArgumentParser(description="Parcheador de idioma a Español para SimplyCast")
    parser.add_argument("path", nargs="?", help="Ruta hacia SimplyCast.exe (opcional)")
    parser.add_argument("--restore", action="store_true", help="Restaurar el ejecutable original desde la copia .bak")
    args = parser.parse_args()

    exe_path = find_target_exe(args.path)
    if not exe_path:
        print("[!] No se encontró SimplyCast.exe automáticamente.")
        print("Por favor especifica la ruta completa, por ejemplo:")
        print(r'python patch_simplycast.py "C:\Users\baque\AppData\Local\Programs\SimplyCast\SimplyCast.exe"')
        sys.exit(1)

    if args.restore:
        restore(exe_path)
    else:
        patch(exe_path)

if __name__ == "__main__":
    main()
