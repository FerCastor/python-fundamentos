# Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

while True:
    try:
        n1 = -1
        n2 = -1
        n3 = -1

        while n1 < 0 or n1 > 10:
            n1 = float(input('A nota deve estar entre 0 e 10. Primeira nota: '))
        while n2 < 0 or n2 > 10:
            n2 = float(input('A nota deve estar entre 0 e 10. Segunda nota: '))
        while n3 < 0 or n3 > 10:
            n3 = float(input('A nota deve estar entre 0 e 10. Terceira nota: '))

        media = (n1 + n2 + n3) / 3

        if media >= 7 and media < 10:
            print(f"Aprovado! Média: {media:.1f}")
        elif media == 10:
            print(f"Aprovado com Distinção! Média: {media:.0f}")
        else:
            print(f"Reprovado! Média: {media:.1f}")

        while True:
            continuar = input("Deseja verificar outra média? [S] ou [N]: "
                              "").strip().upper()
            if continuar in ("S","N"):
                break
            print("Escolha uma opção válida")
        if continuar == "N":
            print("Encerrando...")
            break
    except ValueError:
        print("As notas devem ser um valor numérico")