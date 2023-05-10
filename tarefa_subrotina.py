
import os
import sys
import math

os.system('cls||clear')

# verifica média aritmética
def lerN1():
    n1 = float(input('Nota 1:'))
    return n1

def lerN2():
    n2 = float(input('Nota 2:'))
    return n2

def getMedia(n1 , n2):
    media = (n1+n2)/2
    return media

def mostrar(media) :
    os.system('cls||clear')
    print(f'\n Média = {media}')
    if media < 6:
        print('\n Aluno reprovado')
    else:
        print('\n Aluno Aprovado')
    
def executar():
    nota1 = lerN1()
    nota2 = lerN2()
    media = getMedia(nota1, nota2)
    mostrar(media)

# verifica se o nome contem vogais
def names():
    # Set up name variable with input
    name = str(input('Enter your name: ')) 
    # Check whether name has a vowel
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')

    # Iterate over name
    for letter in name:
        print(letter)

def areaCirculo():
    diametro = float(input('Digite o diametro:'))
    raioCirculo = diametro/2
    area = math.pi * (raioCirculo**2)
    print(round(area, 2))
    return areaCirculo

print('SELECIONE A FUNÇÃO DESEJADA')
print('1. Descobrir se um nome contém vogais')
print('2. Cálculo de média aritmética ')
print('3. Cálculo da área de um círculo')
menu = input(str('Digite a opção: '))

match menu:
    
    case '1':
        print('Função nome selecionada')
        names() # chama função vogal no nome

    case '2':
        print('Função média selecionada')
        executar() # chama função de média

    case '3':
        print('Função área do círculo selecionada')
        areaCirculo() # chama função area do círculo

input()


sys.exit