# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2024
# Versió: 1
#
# Descripció: Demana a l'usuari un número enter positiu i determina si és un nombre primer o no.
# Especificacions Programa que imprimegi en pantalla un numero enter positiu i si es primer o no.

numero = int(input("Introdueix un número enter positiu: "))

if numero <= 1:
    print(f"{numero} NO és un nombre primer")
else:
    es_primer = True
    i = 2

    while i < numero and es_primer == True:
        if numero % i == 0:
            es_primer = False
        i += 1

    if es_primer:
        print(f"{numero} és un nombre primer")
    else:
        print(f"{numero} no és un nombre primer")