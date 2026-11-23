# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calculará
# os reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5%

# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

while True:
    salario = float(input("Salário atual: R$"))

    if salario <= 280:
        percentual = 0.2
    elif salario <= 700:
        percentual = 0.15
    elif salario < 1500:
        percentual = 0.10
    else:
        percentual = 0.05

    valor_aumento = salario * percentual
    salario_ajustado = salario + valor_aumento

    print(f"Salário atual:           R${salario:.2f}")
    print(f"Percentual aplicado:     {percentual * 100:.0f}%")
    print(f"Valor do aumento:        R${valor_aumento:.2f}")
    print(f"Salário após aumento:    R${salario_ajustado:.2f}")

    while True:
        continua = input("Deseja consultar outro valor? S/N: ").strip().upper()
        if continua in ("S", "N"):
            break
        print("Valor inválido, digite S ou N")

    if continua == "N":
        print("Encerrando")
        break