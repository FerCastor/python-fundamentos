# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


while True:
    try:
        data_usuario = input("Informe a data dd/mm/aaaa: ")

        data_lista = data_usuario.split("/")
        if len(data_lista) != 3:
            print('Insira os separadores entre os dias, mês e ano "/"')
        else:
            data_formatada = []

            for i in data_lista:
                i = int(i)
                data_formatada.append(i)

            mes_30_dias = [4, 6, 9, 11]
            mes_31_dias = [1, 3, 5, 7, 8, 10, 12]

            if data_formatada[1] <= 0 or data_formatada[1] >= 13:
                print("Data inválida! O mês não existe.")
            elif data_formatada[2] <= 0:
                print("Data inválida! O ano é menor que zero..")
            else:
                # Anos terminados em 00 só são bissextos se forem divisíveis por 400
                if data_formatada[2] % 400 == 0:
                    if data_formatada[1] == 2:
                        if data_formatada[0] in range(1, 30):
                            print("Data válida")
                        else:
                            print("Data inválida!")
                    if data_formatada[1] in mes_30_dias:
                        if data_formatada[0] in range(1, 31):
                            print("Data válida")
                        else:
                            print("Data inválida!")
                    if data_formatada[1] in mes_31_dias:
                        if data_formatada[0] in range(1, 32):
                            print("Data válida")
                        else:
                            print("Data inválida!")
                else:
                    # Se passar nesse if é um ano comum terminado em 00 que não é
                    # divisível por 400
                    if data_formatada[2] % 100 == 0:
                        if data_formatada[1] == 2:
                            if data_formatada[0] in range(1, 29):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_30_dias:
                            if data_formatada[0] in range(1, 31):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_31_dias:
                            if data_formatada[0] in range(1, 32):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                    elif data_formatada[2] % 4 == 0:
                        if data_formatada[1] == 2:
                            if data_formatada[0] in range(1, 30):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_30_dias:
                            if data_formatada[0] in range(1, 31):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_31_dias:
                            if data_formatada[0] in range(1, 32):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                    else:
                        if data_formatada[1] == 2:
                            if data_formatada[0] in range(1, 29):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_30_dias:
                            if data_formatada[0] in range(1, 31):
                                print("Data válida")
                            else:
                                print("Data inválida!")
                        if data_formatada[1] in mes_31_dias:
                            if data_formatada[0] in range(1, 32):
                                print("Data válida")
                            else:
                                print("Data inválida!")

        while True:
            continuar = input("Deseja testar outro ano? S/N: ").strip().upper()
            if continuar in ("S", "N"):
                break
            print("Digite um valor válido.")

        if continuar == "N":
            print("Encerrando")
            break
    except ValueError:
        print("Valor inválido!")
