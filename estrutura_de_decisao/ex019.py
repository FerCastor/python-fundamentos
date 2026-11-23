# Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


while True:
    try:
        numero = int(input("Informe um número: "))
        while numero >= 1000 or numero <= 0:
            print("Insira um valor entre 1 e 999.")
            numero = int(input("Informe um número: "))

        centena = numero // 100
        resto = numero % 100

        dezena = resto // 10
        unidade = resto % 10

        centenas_texto = ""
        dezenas_texto = ""
        unidades_texto = ""

        if centena > 1:
            centenas_texto = f"{centena} centenas"
        elif centena == 1:
            centenas_texto = f"{centena} centena"
        else:
            centenas_texto = ""

        if dezena > 1:
            dezenas_texto = f"{dezena} dezenas"
        elif dezena == 1:
            dezenas_texto = f"{dezena} dezena"
        else:
            dezenas_texto = ""

        if unidade > 1:
            unidades_texto = f"{unidade} unidades"
        elif unidade == 1:
            unidades_texto = f"{unidade} unidade"
        else:
            unidades_texto = ""

        lista_textos = []
        if centenas_texto != "":
            lista_textos.append(centenas_texto)
        if dezenas_texto != "":
            lista_textos.append(dezenas_texto)
        if unidades_texto != "":
            lista_textos.append(unidades_texto)

        resultado_lista = ""

        if len(lista_textos) == 2:
            resultado_lista = " e ".join(lista_textos)
        elif len(lista_textos) > 2:
            resultado_lista = (
                f"{lista_textos[0]}, {lista_textos[1]} e {lista_textos[2]}"
            )
        elif len(lista_textos) == 1:
            resultado_lista = lista_textos[0]

        print(resultado_lista)

        while True:
            continuar = (
                input("Deseja testar outro número? [S] ou [N]: ")
                .strip()
                .upper()
            )
            if continuar in ("S", "N"):
                break
            print("Valor inválido! Informe [S] ou [N]")
        if continuar == "N":
            print("Encerrando")
            break

    except ValueError:
        print("Valor inválido")
