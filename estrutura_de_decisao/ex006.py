# Faça um programa que leia três números e mostre o maior deles:

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 > n2 and n1 > n3:
    print(f"O valor mais alto digitado foi o {n1}.")
elif n2 > n3:
    print(f"O valor mais alto digitado foi o {n2}.")
else:
    print(f"O valor mais alto digitado foi o {n3}.")
