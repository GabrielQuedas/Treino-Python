# -*- coding: utf-8 -*-
"""Treino_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M1WfuA5Cx8KsnsOcWi74c4FI9JTldF0W

***Olá mundo!***
"""

print("Hello World!")

print(10)

print('-------------------------')
print('Escola de Dados da Alura!')
print('-------------------------')

print('Nome: Gabriel')
print('Sobrenome: Andrade Quedas')
print('Idade:', 22)

print('G')
print('a')
print('b')
print('r')
print('i')
print('e')
print('l')

print(8 ,'de junho de', 2001)

print('Ano atual:', 2023)

"""***Variáveis***"""

idade = 22
print(idade)

idade = 10
print(idade)

idade = 15
idade

nome = 'Gabriel'
print(nome)

"""***Tipos de variáveis***

"""

nome_aluno = 'Gabriel Andrade Quedas'
idade_aluno = 22
media_semestre = 7.0
aprovacao = 'Aprovado'

if media_semestre > 6.9:
  aprovacao = 'Aprovado'
else:
    aprovacao = 'Reprovado'

print('Aluno: ',nome_aluno)
print('Idade: ',idade_aluno)
print('Média do Semestre: ',media_semestre)
print('Situação do Semestre: ',aprovacao)

"""***Salários Escola***"""

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

q_total = q_seguranca + q_docente + q_diretoria
s_diferenca = s_diretoria - s_seguranca
s_media = (q_seguranca*s_seguranca + q_docente*s_docente + q_diretoria*s_diretoria) / q_total
print(q_total, 'Trabalhadores no total.')
print(s_diferenca, 'É a diferença salarial.')
print(s_media, 'Esta é a média salárial.')

"""***Strings***"""

s1 = 'Gabriel'
s2 = "Gabriel"
print(type(s1),type(s2))

nome_professor = '   Gabriel Andrade Quodas   '
nome_professor = nome_professor.strip().replace('o', 'e').upper()
nome_professor

"""***Inputs***"""

nome = input('Por favor, digite seu nome: ')
print('Seu nome é', nome,', correto? ')
resposta = input('Sim ou não? ')
if resposta == 'Sim':
  print('Ok, e sua idade?')
else:
  print('Paramos por aqui.')
idade = float(input('Idade: '))
print('Sua idade é ',idade ,'correto?')
i_resposta = input('Sim ou não? ')
if i_resposta == 'Sim':
  print('Muito obrigado!')
else:
  print('Paramos por aqui.')

nome = input('Por favor, qual o seu nome? ')
print('Olá,',nome,'! :)')

idade = int(input('Qual sua idade? '))
print('Olá', nome,', você tem', idade,'anos, certo?')

altura = float(input('Qual sua altura? '))
print('Olá', nome,', você tem', idade,'anos e', altura,', correto?')

"""***Calculadora***"""

soma_a = int(input('Digite o primeiro número: '))
soma_b = int(input('Digite o segundo número: '))
resultado = soma_a + soma_b
print('O resultado é:',resultado,".")

soma_a = int(input('Digite o primeiro número: '))
soma_b = int(input('Digite o segundo número: '))
soma_c = int(input('Digite o terceiro número: '))
resultado = soma_a + soma_b + soma_c
print('O resultado é:',resultado,'!')

sub_a = int(input('Digite o primeiro valor: '))
sub_b = int(input('Digite o segundo valor: '))
resultado = sub_a - sub_b
print('O resultado é:',resultado,'!')

nota_a = float(input('Digite a nota do primeiro trimestre: '))
nota_b = float(input('Digite a nota do segundo trimestre: '))
nota_c = float(input('Digite a nota do terceiro trimestre: '))
resultado = (nota_a + nota_b + nota_c) / 3
print('A média anual das notas foi de:',resultado,'!')

"""***if, else e elif***"""

if 4<1:
  print('Acertouuuu.')
else:
  print('Errouuuu.')

idade_gabriel = input('Qual a idade do Gabriel? ')
idade_alice = input('Qual a idade da Alice? ')

if idade_gabriel > idade_alice:
  print('Gabriel é o irmão mais velho.')
else:
  print('Alice é a irmã mais velha.')

nota_1 = float(input('Digite a nota do primeiro semestre: '))
nota_2 = float(input('Digite a nota do segundo semestre: '))
nota_3 = float(input('Digite a nota do terceiro semestre: '))
nota_4 = float(input('Digite a nota do quarto semestre: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7.0:
  print('O aluno está aprovado!')
elif 7.0 > media >= 4.0:
  print('O aluno pode fazer recuperação!')
elif media < 4.0:
  print('O aluno está reprovado!')

t1 = t2 = True
f1 = f2 = False

if f1 and f2:
  print('Expressão verdadeira.')
else:
  print('Expressão falsa.')

if t1 or t2:
  print('Expressão verdadeira.')
else:
  print('Expressão falsa.')

if not f1:
  print('Expressão verdadeira.')
else:
  print('Expressão falsa.')

nome = 'Mariana'

if 'Mariana' in nome:
  print('Expressão correta.')
else:
  print('Expressão falsa.')

"""***Promoção***"""

jogo_promocao = input("O jogo está em promoção? (Sim/Não): ")

if jogo_promocao.lower() == "sim":
  print('Comprar o jogo.')
else:
  print('Esperar promoção')

"""***WHILE***

"""

contador = 1

while contador <= 10:
  print(contador)
  contador = contador+1

contador = 1

while contador <= 3:
  nota_1 = float(input('Digite a 1º nota: '))
  nota_2 = float(input('Digite a 2º nota: '))

  print(f'Média: {(nota_1+nota_2)/2}')
  contador += 1

"""***FOR***"""

for contador in range(1, 11):
  print(contador)

for contador in range(1,5):
  nota_1 = float(input('Digite a 1º nota: '))
  nota_2 = float(input('Digite a 2º nota: '))

  print(f'Média: {(nota_1+nota_2)/2}')

numerointeiro_a = int(input('Digite o primeiro número: '))
numerointeiro_b = int(input('Digite o segundo número: '))

for numeros in range(numerointeiro_a, numerointeiro_b):
  print(numeros)
if numerointeiro_a >= numerointeiro_b:
  for numeros in range(numerointeiro_b, numerointeiro_a):
    print(numeros)