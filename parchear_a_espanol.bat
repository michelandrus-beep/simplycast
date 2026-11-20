@echo off
chcp 65001 > nul
echo ========================================================
echo     SimplyCast - Parcheador de Idioma al Español
echo ========================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] No se encontro Python en el sistema.
    echo Por favor instala Python o asegurate de que este en el PATH.
    pause
    exit /b 1
)

python "%~dp0patch_simplycast.py" "C:\Users\baque\AppData\Local\Programs\SimplyCast\SimplyCast.exe"

echo.
pause
