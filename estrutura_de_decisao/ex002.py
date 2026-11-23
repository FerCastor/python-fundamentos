# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Informe um valor positivo ou negativo: "))

if num > 0:
    print(f"O valor {num} é positivo.")
elif num < 0:
    print(f"O valor {num} é negativo.")
else:
    print("O número digitado é zero.")
