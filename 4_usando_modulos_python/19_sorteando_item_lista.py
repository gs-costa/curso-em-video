from random import random, choice


aluno_lista = []
for i in range(4):
    aluno_lista += [str(input(f"Aluno {i+1}: "))]

print(f"O aluno escolhido foi: {choice(aluno_lista)}")
