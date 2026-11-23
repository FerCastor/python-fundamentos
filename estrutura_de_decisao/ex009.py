# Faça um programa que leia três números e mostre-os em ordem decrescente:

n1 = int(input("Número: "))
n2 = int(input("Número: "))
n3 = int(input("Número: "))

lista = [n1, n2, n3]
lista.sort(reverse=True)

for i in lista:
    print(i)
