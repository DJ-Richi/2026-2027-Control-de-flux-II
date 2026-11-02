# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2026
# Versió: 1
#
# Descripció: Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10.
# Especificacions d'Entrada: Numero enter i que es mostri la seva taula de multiplicar

numero = int(input("Introdueix un numero per a la taula: "))

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i*numero)