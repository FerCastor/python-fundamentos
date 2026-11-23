# Faça um programa que leia três números e mostre o maior e o menor deles:

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 > n2 and n1 > n3:
    print(f"Maior: {n1}")
    if n2 > n3:
        print(f"Menor: {n3}")
    else:
        print(f"Menor: {n2}")
elif n2 > n3:
    print(f"Maior: {n2}")
    if n1 > n3:
        print(f"Menor: {n3}")
    else:
        print(f"Menor: {n1}")
else:
    print(f"Maior: {n3}")
    if n1 > n2:
        print(f"Menor: {n2}")
    else:
        print(f"Menor: {n1}")
