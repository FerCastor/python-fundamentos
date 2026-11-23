# Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#
# M - Matutino
# V - Vespertino
# N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite a letra referente ao turno você estuda: [M] Matutino | [V] Vespertino | [N] Noturno: ")

if turno.capitalize() == "M":
    print("Bom dia! =)")
elif turno.capitalize() == "V":
    print("Boa tarde! =)")
elif turno.capitalize() == "N":
    print("Boa noite! =)")
else:
    print("Entrada inválida! Tente novamente!")
