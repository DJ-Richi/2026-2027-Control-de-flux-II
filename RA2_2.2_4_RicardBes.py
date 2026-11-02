# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2026
# Versió: 1
#
# Descripció: Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti.
# Especificacions Programa que imprimeixi en pantalla un numero aleatori entre 1 al 100.

numero = 57
encertat = False

while encertat == False:
    intent = int(input("Endevina el número (1-100): "))

    if intent == numero:
        print("Correcte! Has encertat")
        encertat = True
    elif intent < numero:
        print("Massa baix")
    else:
        print("Massa alt")