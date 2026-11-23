# Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16



while True:
    try:
        numero = int(input('Informe um número: '))
        while numero >= 1000 or numero <= 0:
            print('Insira um valor entre 1 e 999.')
            numero = int(input('Informe um número: '))

        centena = numero // 100
        resto = numero % 100

        dezena = resto // 10
        unidade = resto % 10

        centenas = ''
        dezenas = ''
        unidades = ''

        if centena > 1:
            centenas = f'{centena} centenas'
        elif centena == 1:
            centenas = f'{centena} centena'
        else:
            centenas = ''

        if dezena > 1:
            dezenas = f'{dezena} dezenas'
        elif dezena == 1:
            dezenas = f'{dezena} dezena'
        else:
            dezenas = ''

        if unidade > 1:
            unidades = f'{unidade} unidades'
        elif unidade == 1:
            unidades = f'{unidade} unidade'
        else:
            unidades = ''

        lista = []
        if centenas != '':
            lista.append(centenas)
        if dezenas != '':
            lista.append(dezenas)
        if unidades != '':
            lista.append(unidades)

        resultado_lista = ''

        if len(lista) == 2:
            resultado_lista = ' e '.join(lista)
        elif len(lista) > 2:
            resultado_lista = f'{lista[0]}, {lista[1]} e {lista[2]}'
        elif len(lista) == 1:
            resultado_lista = lista[0]

        print(resultado_lista)


        while True:
            continuar = input('Deseja testar outro número? [S] ou [N]: '
                              '').strip().upper()
            if continuar in ('S', 'N'):
                break
            print('Valor inválido! Informe [S] ou [N]')
        if continuar == 'N':
            print('Encerrando')
            break

    except ValueError:
        print('Valor inválido')