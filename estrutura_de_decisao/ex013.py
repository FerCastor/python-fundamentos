# Faça um programa que leia um número e exiba o dia correspondente da
# semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve
# aparecer valor inválido.

## Melhoria adicionada por mim: laço while para garantir que o
# usuário vai inserir um valor válido

while True:
    dia_usuario = int(input("Informe o número correspondente ao dia desejado: ["
                            "1] domingo, [2] segunda, etc:"))
    dias_semana = {1:"Domingo", 2:"Segunda-feira", 3:"Terça-feira",
                   4:"Quarta-feira", 5:"Quinta-feira", 6:"Sexta-feira", 7:"Sábado"}

    if dia_usuario in dias_semana:
        print(f"O dia escolhido foi: {dias_semana[dia_usuario]}")
        break
    else:
        print("Informe um dia válido")
