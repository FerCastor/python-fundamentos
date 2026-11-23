# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Sexo Inválido.

sexo = input("Informe o sexo: [F] ou [M]: ")

if sexo.capitalize() == "F":
    print("Sexo feminino")
elif sexo.capitalize() == "M":
    print("Sexo masculino")
else:
    print("Sexo inválido")
