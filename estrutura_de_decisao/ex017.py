# Faça um programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.


while True:
    try:
        ano = int(input("Ano: "))

        # Anos terminados em 00 só são bissextos se forem divisíveis por 400
        if ano % 400 == 0:
            print(f'{ano} é um ano bissexto.')
        else:
            # Se passar nesse if é um ano comum terminado em 00 que não é
            # divisível por 400
            if ano % 100 == 0:
                print(f'{ano} não é bissexto.')
            elif ano % 4 == 0:
                print(f'{ano} é um ano bissexto.')
            else:
                print(f'{ano} não é bissexto.')

        while True:
            continuar = input('Deseja testar outro ano? S/N: ').strip().upper()
            if continuar in ('S', 'N'):
                break
            print('Digite um valor válido.')

        if continuar == 'N':
            print('Encerrando')
            break
    except ValueError:
        print('Valor inválido!')
