# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
# fazer as consistências, informando ao usuário nas seguintes situações:

### Se o usuário informar o valor de A igual a zero, a equação não é do
# segundo grau e o programa não deve fazer pedir os demais valores,
# sendo encerrado;

### Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;

### Se o delta calculado for igual a zero a equação possui apenas uma raiz
# real; informe-a ao usuário;

### Se o delta for positivo, a equação possui duas raiz reais; informe-as ao
# usuário;

while True:
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))

    if a == 0:
        print("A equação não é do segundo grau, pois A = 0")
        break
    else:
        delta = b ** 2 - 4 * a * c
        if delta == 0:
            x = (-b + pow(delta, 0.5)) / (2 * a)
            print(f"A equação possui apenas uma raiz real: {x}")
        elif delta < 0:
            print("A equação não possui raizes reais.")
        else:
            x1 = (-b + pow(delta, 0.5)) / (2 * a)
            x2 = (-b - pow(delta, 0.5)) / (2 * a)
            print(f"Essa equação possui duas raizes reais: {x1} e {x2}")

    while True:
        continua = input("Deseja consultar outro valor? S/N: ").strip().upper()
        if continua in ("S", "N"):
            break
        print("Valor inválido, digite S ou N")

    if continua == "N":
        print("Encerrando")
        break