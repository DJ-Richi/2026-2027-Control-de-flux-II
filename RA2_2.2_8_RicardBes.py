# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2024
# Versió: 1
#
# Descripció: Demana a l'usuari una frase i compta quantes vocals conté.
# Especificacions Programa que compti en una frase que compti qauantes vacals conté.

frase = input("Introdueix una frase: ")

vocals = "aeiou"
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print(f"La frase conté {comptador} vocals")