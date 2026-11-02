# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 02/11/2024
# Versió: 1
#
# Descripció: Mostra els primers 10 termes de la seqüència de Fibonacci.
# Especificacions Programa que imprimegi 10 termes de la seqüència de Fibonacci.

num = int(input("intrudueix un numero de la secuencia de Fibonacci:"))

a,b = 0,1
comptador = 0
while comptador < 10:
    print (a,end="")
    suma_termes = a+b
    a = b
    b = suma_termes
    comptador = comptador + 1
print()