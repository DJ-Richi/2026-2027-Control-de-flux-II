# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2024
# Versió: 1
#
# Descripció: Trobar el número màxim d’una llista
# Especificacions Programa que trovi el numero maxim d'una llista

llista = [32, 7, 67, 9, 64, 65, 11, 72,]

maxim = llista[0]

for numero in llista:
    if numero > maxim:
        maxim = numero

print("El número màxim és:", maxim)