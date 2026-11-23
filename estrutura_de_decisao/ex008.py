# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

produto1 = float(input("Valor primeiro produto: R$"))
produto2 = float(input("Valor segundo produto: R$"))
produto3 = float(input("Valor terceiro produto: R$"))

if produto1 < produto2 and produto1 < produto3:
    print(f"A melhor opção é o primeiro produto, custando R${produto1:.2f}")
elif produto2 < produto3:
    print(f"A melhor opção é o segundo produto, custando R${produto2:.2f}")
else:
    print(f"A melhor opção é o terceiro produto, custando R${produto3:.2f}")
