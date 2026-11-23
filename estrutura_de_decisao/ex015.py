# Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
#
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

while True:
    lado1 = int(input("Medida lado 1:"))
    lado2 = int(input("Medida lado 2:"))
    lado3 = int(input("Medida lado 3:"))

    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if (
            lado1 + lado2 > lado3
            and lado1 + lado3 > lado2
            and lado2 + lado3 > lado1
        ):
            if lado1 == lado2 and lado1 == lado3:
                print("Triângulo Equilátero")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Triângulo Isósceles")
            else:
                print("Triângulo Escaleno")
        else:
            print("As medidas informadas não formam um triângulo.")
    else:
        print("As medidas informadas não formam um triângulo.")

    while True:
        continua = input("Deseja consultar outro valor? S/N: ").strip().upper()
        if continua in ("S", "N"):
            break
        print("Valor inválido, digite S ou N")

    if continua == "N":
        print("Encerrando")
        break
