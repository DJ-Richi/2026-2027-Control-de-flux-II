# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2024
# Versió: 1
#
# Descripció: Demana a l'usuari una cadena de text i mostra-la invertida.
# Especificacions Programa que imprimegi una cadena de text i mostrar-la invertida.

text = input("Introdueix una cadena de text: ")

text_invertit = ""
i = len(text) - 1

while i >= 0:
    text_invertit += text[i]
    i -= 1

print("Text invertit:", text_invertit)