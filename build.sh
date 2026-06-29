#!/bin/bash

# Oprim scriptul imediat dacă apare vreo eroare
set -e

echo "=== Pornire proces de Build pentru Calculator ==="

# 1. Curățare foldere vechi de build dacă există
echo "Curățare versiuni anterioare..."
rm -rf build dist

# 2. Împachetarea scriptului Python într-un singur fișier executabil binar
echo "Compilare main.py cu PyInstaller..."
pyinstaller --onefile main.py

# 3. Verificarea succesului
if [ -f "dist/main" ]; then
    echo "=== Build finalizat cu succes! ==="
    echo "Executabilul tău se află în folderul 'dist' cu numele 'main'"
else
    echo "Eroare: Build-ul a eșuat!"
    exit 1
fi