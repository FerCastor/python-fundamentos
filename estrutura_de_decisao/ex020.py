# Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7 and media < 10:
    print(f"Aprovado! Média: {media:.1f}")
elif media < 7:
    print(f"Reprovado! Média: {media:.1f}")
else:
    print(f"Aprovado com Distinção! Média: {media:.0f}")