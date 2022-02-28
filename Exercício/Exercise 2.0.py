""">> PRIMEIROS COMANDOS <<"""

# EXERCÍCIO 2 - Respondendo ao usuário
'''
name = str(input('Digite seu nome: '))
print(f'É um prazer te conhecer, {name}!')
'''

# EXERCÍCIO 3 - Somando dois números
'''
n1 = float(input('1º Número: '))
n2 = float(input('2º Número: '))
print(f'A soma entre {n1} e {n2} vale {n1 + n2}')
'''

# EXERCÍCIO 4 - Dissecando uma variável
'''
a = input('Digite algo: ')
print(f'Tipo primitivo: {type(a)}\n'
      f'Dado espaçado: {a.isspace()}\n'
      f'Números: {a.isnumeric()}\n'
      f'Alfabético: {a.isalpha()}\n'
      f'Alphanumérico: {a.isalnum()}\n'
      f'Maiusculo: {a.isupper()}\n'
      f'Minusculo: {a.islower()}\n'
      f'Capitalizado: {a.istitle()}\n'
      f'Gostou do resultado?')
'''

'''>> OPERADORES ARITIMÉTICOS <<'''

# EXERCÍCIO 5 - Antecessor e Sucessor
'''
inum = int(input('Integer Number: '))

print(f'Analise do valor: {inum}\n'
      f'Antecessor: {inum - 1}\n'
      f'Sucessor:   {inum + 1}')
'''

# EXERCÍCIO 6 - Dobro, Triplo, Raiz Quadrada
'''
num = int(input(f'Número: '))
print(f'Dobro:          {num * 2}\n'
      f'Triplo:         {num * 3}\n'
      f'Raiz Quadrada:  {num ** 0.5:.2f}')
'''

# EXERCÍCIO 7 - Média Aritmética
'''
n1 = float(input('1ª Média: '))
n2 = float(input('2ª Média: '))
mean = (n1 + n2) / 2
print(f'Para os valores abaixo\n'
      f'Nota 1 = {n1:.1f}\n'
      f'Nota 2 = {n2:.1f}\n'
      f'Média  = {mean:.1f}')
'''

# EXERCÍCIO 8 - Conversor de Medidas
'''
dist = float(input('Distância(m): '))
print(f'{dist} Metros:\n'
      f'Km: {dist/1000}\n'
      f'Hm: {dist/100}\n'
      f'Dm: {dist/10}\n'
      f'dm: {dist*10}\n'
      f'cm: {dist*100}\n'
      f'mm: {dist*1000}')
'''

# EXERCÍCIO 9 - Tabuada
'''
num = int(input('Número: '))
print(f'{num} x  1 = {num*1}\n'
      f'{num} x  2 = {num*2}\n'
      f'{num} x  3 = {num*3}\n'
      f'{num} x  4 = {num*4}\n'
      f'{num} x  5 = {num*5}\n'
      f'{num} x  6 = {num*6}\n'
      f'{num} x  7 = {num*7}\n'
      f'{num} x  8 = {num*8}\n'
      f'{num} x  9 = {num*9}\n'
      f'{num} x 10 = {num*10}')
'''

# EXERCÍCIO 10 - Conversor de Moedas
'''
real = float(input('Dinheiro: R$ '))
btc = real / 323527.12
print(f'R$ {real}:\n'
      f'BTC {real / 323527.12:.6f}')
'''

# EXERCÍCIO 11 - Pintando Parede
'''
w = float(input('Largura (m): '))
h = float(input('Altura (m): '))
area = w * h
ink = area / 2
print(f'Dimensões: {w}x{h}\n'
      f'Área: {area} m²\n'
      f'Tinta: {ink} L')
'''

# EXERCÍCIO 12 - Calculando Descontos
'''
P = float(input('Preço: '))
D = float(input('Desconto: '))
nP = (P * (100 - D)) / 100
print(f'R$ {nP:.2f}')
'''

# EXERCÍCIO 13 - Reajuste Salarial
'''
wg = float(input('Salário: R$ '))
pc = float(input('Aumento(%): '))
nwg = wg * ((pc/100) + 1)
print(f'R$ {wg} + {pc}%:\n'
      f'R$ {nwg:.2f}')
'''

# EXERCÍCIO 14 - Conversor de Temperaturas
'''
c = float(input('ºC: '))
f = (1.8 * c) + 32
k = c + 273

print(f'Celsius:    {c}ºC\n'
      f'Kelvin:     {k}ºK\n'
      f'Fahrenheit: {f}ºF')
'''

# EXERCÍCIO 15 - Aluguel de Carros
'''
d = int(input('Dias: '))
km = float(input('Km: '))
c = (d * 60) + (km * 0.15)
print(f'Total a pagar: R$ {c:.2f}')
'''

'''>> UTILIZANDO MÓDULOS <<'''

# EXERCÍCIO 16 - Quebrando um número
'''
from math import trunc
num = float(input('Número: '))
print(f'Para o número:     {num}\n'
      f'Porção Inteira:    {trunc(num)}\n'
      f'Porção Fracionada: {num - (trunc(num)):.2f}')
'''

# EXERCÍCIO 17 - Catetos e Hypotenusa
'''
from math import hypot
fc = float(input('Cateto Oposto: '))
sc = float(input('Cateto Adjacente: '))
hp = hypot(fc,sc)
print(f'Hipotenusa: {hp:.2f}')
'''

# EXERCÍCIO 18 - Cosseno e Tangente
'''
from math import sin, cos, tan, radians
dg = float(input('Ângulo: '))
s = sin(radians(dg))
c = cos(radians(dg))
t = tan(radians(dg))

print(f'Seno:     {s:.2f}\n'
      f'Cosseno:  {c:.2f}\n'
      f'Tangente: {t:.2f}')
'''

# EXERCÍCIO 19 - Sorteando um Item na Lista
'''
from random import *
a = str(input('1º Aluno: '))
b = str(input('2º Aluno: '))
c = str(input('3º Aluno: '))
d = str(input('4º Aluno: '))
li = [a, b, c, d]
print(f'Escolhido: {choice(li)}')
'''

# EXERCÍCIO 20 - Sorteando uma Ordem na Lista
'''
from random import shuffle
a = str(input('1º Aluno: '))
b = str(input('2º Aluno: '))
c = str(input('3º Aluno: '))
d = str(input('4º Aluno: '))
li = [a, b, c, d]
shuffle(li)
print(f'Ordem:\n'
      f'{li}')
'''

# EXERCÍCIO 21 - Tocando um MP3 - Imcompleto
'''
import webbrowser as wb
wb.open('smt.mp3')
'''

'''>> MANIPULANDO STRING <<'''

# EXERCÍCIO 22 - Analisador de Textos
'''
name = str(input('Nome: ')).strip()
fst = name.split()
jn = ''.join(fst)
print(f'Upper:      {name.upper()}\n'
      f'Lower:      {name.lower()}\n'
      f'Letras:     {len(jn)}\n'
      f'1º Nome:    {fst[0]}\n'
      f'Letras 1º:  {len(fst[0])}')
'''

# EXERCÍCIO 23 - Separando Dígitos de um Número
'''
num = str(input('Número: ')).strip()
len = len(num)

print(f'Milhar:  {num[len - 4]}\n'
      f'Centena: {num[len - 3]}\n'
      f'Dezena:  {num[len - 2]}\n'
      f'Unidade: {num[len - 1]}')
'''

# EXERCÍCIO 24 - Verificando as Primeiras Letras de um Texto
'''
ct = input('Naturalidade: ').strip().title()
print(ct.startswith('Santo'))
'''

# EXERCÍCIO 25 - Procurando uma String Dentro de Outra
'''
name = input('Nome completo: ').strip().lower()
s = 'silva' in name
print(f'Seu nome tem Silva?\n'
      f'{s}')
'''

# EXERCÍCIO 26 - Primeira e Última Ocorrência de uma String
'''
from unidecode import unidecode
frase = input('Frase: ').strip().lower()
frase_sa = unidecode(frase)
c = frase_sa.count('a')
pa = frase_sa.find('a')
ua = frase_sa.rfind('a')
print(f'Quantos  "A":  {c}\n'
      f'Primeiro "A":  {pa + 1}\n'
      f'Último   "A":  {ua + 1}')
'''

# EXERCÍCIO 27 - Primeiro e Último Nome de uma Pessoa
'''
name = input('Nome completo: ').strip()
l_name = name.split()
print(f'Primeiro nome: {l_name[0]}\n'
      f'Último nome:   {l_name[len(l_name) - 1]}')
'''

'''>> CONDICIONAIS <<'''

# EXERCÍCIO 28 - Jogo da Adivinhação v1.0
'''
from time import sleep
from random import randint
print('Jogo da Adivinhação')
sleep(2)
print('Sortearei um número entre 0 e 5')
sleep(1)
num = int(input('Qual número sorteado? '))
rn = randint(0, 5)
if rn == num:
    print(f'Parabéns! Você venceu!')
else:
    print(f'Que pena! Você errou!')
print(f'Número sorteado: {rn}\n'
      f'Número Digitado: {num}')
'''

# EXERCÍCIO 29 - Radar Eletrônico
'''
spd = float(input('Velocidade: '))
if spd > 80:
    print(f'MULTADO!\n'
          f'Limite permitido: 80 km/h\n'
          f'Velocidade registrada: {spd:.2f}\n'
          f'Diferença excedida: {spd - 80}\n'
          f'Multa gerada: {(spd - 80) * 7}')
else:
    print('Velocidade dentro do limite permitido.')
    print(f'Limite permitido: 80 km/h\n'
          f'Velocidade registrada: {spd:.2f}\n')
print('Tenha um bom dia!\n'
      'Dirija com segurança!')
'''

# EXERCÍCIO 30 - Par ou Ímpar
'''
num = int(input('Número Inteiro: '))
if num % 2 == 0:
    print(f'{num} é PAR!')
else:
    print(f'{num} é ÍMPAR!')
'''

# EXERCÍCIO 31 - Custo de Viagem
'''
dist = float(input('Distância (km): '))
cost = 0.5
if dist > 200:
    cost = 0.45
print(f'Custo: R$ {dist * cost}')
'''

# EXERCÍCIO 32 - Ano Bissexto
'''
from datetime import date
print('Análise de Ano Bissexto.\n'
      'Use 0 para o ano atual.')
y = int(input('Ano: '))
if y == 0:
    y = date.today().year

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('SIM')
else:
    print('NÃO')
'''

# EXERCÍCIO 33 - Maior e Menor
'''
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))
maior = n1
menor = n1
if n1 < n2 > n3:
    maior = n2
if n1 < n3 > n2:
    maior = n3
if n1 > n2 < n3:
    menor = n2
if n1 > n3 < n2:
    menor = n3
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
'''

# EXERCÍCIO 34 - Aumento Múltiplos
'''
wage = float(input('Salário: '))
pc = 15
if wage > 1250:
    pc = 10
rw = wage * (pc/100 + 1)

print(f'Salário Inicial: R${wage}\n'
      f'Salário Final:   R${rw}\n'
      f'Aumento:          {pc}%')
'''

# EXERCÍCIO 35 - Analisando Triângulo v1.0
'''
f = float(input('1º Segmento: '))
s = float(input('2º Segmento: '))
t = float(input('3º Segmento: '))

if (f + s) > t and (s + t) > f and (f + t) > s:
    print(f'Com as retas:\n'
          f'1ª - {f:.2f}\n'
          f'2ª - {s:.2f}\n'
          f'3ª - {t:.2f}'
          f'Um triângulo pode ser formado!')
else:
    print(f'Com as retas:\n'
          f'1ª - {f:.2f}\n'
          f'2ª - {s:.2f}\n'
          f'3ª - {t:.2f}'
          f'Um triângulo NÂO pode ser formado!')
'''

'''>> CONDICIONAIS ANINHADAS <<'''

# EXERCÍCIO 36 - Aprovando Empréstimo
'''
print('Cálculo de Empréstimo')
h_price = float(input('Valor do imóvel: R$ '))
wage = float(input('Renda Mensal: R$ '))
time = int(input('Prestações (anos): '))
month = time * 12
m_install = h_price / month
w_porc = wage * 0.3
if m_install > w_porc:
    print(f'EMPRÉSTIMO NEGADO:\n'
          f'Mensalidade: R$ {m_install:.2f}\n'
          f'Restrição de até 30%\n'
          f'do salário informado, R$ {w_porc:.2f}')
else:
    print(f'EMPRÉSTIMO APROVADO:\n'
          f'Mensalidade: R$ {m_install:.2f}')
'''

# EXERCÍCIO 37 - Conversor de Bases Numéricas
'''
num = int(input('Número Inteiro: '))
print('Opção de Converção:\n'
      '[ 1 ] Binário\n'
      '[ 2 ] Octal\n'
      '[ 3 ] Hexadecimal')
choice = int(input('Dígito: '))

if choice == 1:
    print(f'Binário: {bin(num)[2:]}')
elif choice == 2:
    print(f'Octal: {oct(num)[2:]}')
elif choice == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')
else:
    print('Escolha uma das Opções Válidas!')
'''

# EXERCÍCIO 38 - Comparando Números
'''
num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))

if num1 > num2:
    print('O 1º número é maior!')
elif num1 < num2:
    print('O 2º número é maior!')
else:
    print('Os dois números são iguais!')
'''

# EXERCÍCIO 39 - Alistamento Militar
'''
from datetime import date
year = int(input('Ano de Nascimento: '))
age = date.today().year - year

print(f'Quem nasceu em {year} tem {age} anos em {date.today().year}')

if age < 18:
    print(f'Faltam {18 - age} para o alistamento.\n'
          f'Seu alistamento será em {year + 18}.')
elif age > 18:
    print(f'Você deveria ter se alistado há {age - 18} anos\n'
          f'Seu alistamento foi em {year + 18}')

else:
    print('Está no ano de seu alistamento.')
'''

# EXERCÍCIO 40 - Média
'''
n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
mean = (n1 + n2) / 2
if mean >= 7:
    result = 'APROVADO'
elif mean < 5:
    result = 'REPROVADO'
else:
    result = 'RECUPERAÇÃO'
print(f'Média: {mean:.2f}\n'
      f'Resultado:\n{result}!')
'''

# EXERCÍCIO 41 - Classificando Atletas
'''
from datetime import date

year = int(input('Ano de Nascimento: '))
age = date.today().year - year

if age <= 9:
    cl = 'MIRIM'
elif age <= 14:
    cl = 'INFANTIL'
elif age <= 19:
    cl = 'JUNIOR'
elif age <= 25:
    cl = 'SÊNIOR'
else:
    cl = 'MASTER'
print(f'Idade do Atleta: {age}\n'
      f'Classificação: {cl}')
'''

# EXERCÍCIO 42 - Analisando Triângulos v2.0
'''
s1 = float(input('1ª Reta: '))
s2 = float(input('2ª Reta: '))
s3 = float(input('3ª Reta: '))

print(f'Com as retas:\n'
          f'{s1:.2f}\n'
          f'{s2:.2f}\n'
          f'{s3:.2f}\n')

if (s1 + s2) > s3 and (s2 + s3) > s1 and (s1 + s3) > s2:
    if s1 == s2 == s3:
        type = 'EQUILATERO'
    elif s1 != s2 and s1 != s3 and s2 != s3:
        type = 'ESCALENO'
    else:
        type = 'ISÓSCELES'
    print(f'Pode ser formado um triângulo do tipo:\n'
          f'{type}')
else:
    print(f'NÃO é possivel formar um triângulo!')
'''

# EXERCÍCIO 43 - Índice de Massa Corporal
'''
weight = str(input('Peso (kg): ')).strip()
height = str(input('Altura (m): ')).strip()
if ',' in weight or ',' in height:
    weight = weight.replace(',', '.')
    height = height.replace(',', '.')
weight = float(weight)
height = float(height)
imc = (weight / (height ** 2))

if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc < 25:
    status = 'Peso Ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'

print(f'IMC: {imc:.2f}\n'
      f'Status:\n'
      f'{status}')
'''

# EXERCÍCIO 44 - Gerenciador de Pagamentos
'''
print('Gerenciador de Pagamento')
price = float(input('Preço: '))

print('Forma de pagamento:\n'
      '[ 1 ] à vista DINHEIRO\n'
      '[ 2 ] à vista PIX\n'
      '[ 3 ] à vista CARTÂO\n'
      '[ 4 ] Parcelado CARTÃO\n')
choice = int(input('Opção: '))
portion = 1
if choice in range(1, 5):
      if choice == 1:
            price_desc = price - (price * 0.10)
      elif choice == 2:
            price_desc = price - (price * 0.05)
      elif choice == 3:
            price_desc = price
      elif choice == 4:
            portion = int(input('Parcelas: '))
            price_desc = price
            if portion > 2:
                  price_desc = price * 1.2
      print(f'Valor final: R$ {price_desc}\n'
            f'Parcelas: {portion}x de R$ {price_desc / portion}')
else:
      print('Escolha uma opção válida')
'''

# EXERCÍCIO 45 - Game: Jokenpo
'''
from time import sleep
from random import choice
print('=== JOKENPÔ ===\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')

option_list = [1, 2, 3]
option_words = ['PEDRA', 'PAPEL', 'TESOURA']
option = int(input('Opção: '))
pc_option = choice(option_list)
if option in option_list:
      if option == pc_option:
            result = 'EMPATE'
      elif option == 1 and pc_option == 3:
            result = 'VENCEU'
      elif option == 2 and pc_option == 1:
            result = 'VENCEU'
      elif option == 3 and pc_option == 2:
            result = 'VENCEU'
      else:
            result = 'PERDEU'
      print('JO')
      sleep(0.5)
      print('KEN')
      sleep(0.5)
      print('PÔ')
      sleep(0.5)
      print(f'Resultado: {result.upper()}\n'
            f'Sua escolha: {option_words[option - 1]}\n'
            f'Sorteado: {option_words[pc_option - 1]}\n')
else:
      print('Escolha uma opção válida!')
'''

'''>> ESTRUTURA DE REPETIÇÃO (for) <<'''

# EXERCÍCIO 46 - Contagem Regressiva
'''
from time import sleep
print('Firework Count Simulator')
for count in range(10, -1, -1):
      sleep(1)
      print(count)
print('FiiiiiiuuummmMMMM')
sleep(1)
print('BOOOMM!')
'''

# EXERCÍCIO 47 - Contagem de Pares
'''
for par in range(2, 51, 2):
      print(par)
'''

# EXERCÍCIO 48 - Soma Ímpares Múltiplos de Três
'''
s = 0
c = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        c += 1
        s += impares
print(f'Total de números: {c}\n'
      f'Somatório: {s}')
'''

# EXERCÍCIO 49 - Tabuada v2.0
'''
print('== TABUADA v2.0 ==')
num = int(input('Número: '))
mult = 0
for _ in range(0, 11):
    print(f'{num} x {mult:2} = {num * mult}')
    mult += 1
'''

# EXERCÍCIO 50 - Soma dos Pares
'''
s = 0
c = 0
for _ in range(1, 7):
    num = int(input(f'{_}º Número: '))
    if num % 2 == 0:
        c += 1
        s += num
print(f'Números pares: {c}\n'
      f'Soma: {s}')
'''

# EXERCÍCIO 51 - Progressão Aritmética
'''
num1 = int(input('1º Termo: '))
raz = int(input('Razão: '))

for numero in range(num1, num1 + 10 * raz, raz):
    print(f'{numero}')
'''

# EXERCÍCIO 52 - Números Primos
'''
num1 = int(input('Número: '))

c = 0
print(f'O número {num1} é divisível por:')
for div in range(1, num1 + 1):
    if num1 % div == 0:
        print('\33[34m', end='')
        c += 1
    else:
        print('\33[31m', end='')
    print(div, end=' ')
print(f'\nDivisível {c} vezes')

if c == 2:
    print('Número Primo!')
else:
    print('Não é um Número Primo!')
'''

# EXERCÍCIO 53 - Detector de Palíndromo
'''
word = str(input('Frase: ')).strip().upper()
separado = word.split()
unido = ''.join(separado)
inverso = ''

for _ in range(len(unido)-1, -1, -1):
    inverso = inverso + unido[_]
print(f'{unido} {inverso}')
if inverso == unido:
    print('A frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
'''

# EXERCÍCIO 54 - Grupo da Maioridade
'''
from datetime import date
cont_maior = 0
cont_menor = 0
for _ in range(1, 8):
    year = int(input(f'Em que ano a {_}ª pessoa nasceu? '))
    if date.today().year - year < 18:
        cont_menor += 1
    else:
        cont_maior += 1

print(f'Dos anos digitados:\n'
      f'{cont_maior} Pessoas são maior de idade\n'
      f'{cont_menor} Pessoas são menor de idade')
'''

# EXERCÍCIO 55 - Maior e menor da sequência
'''
maior = 0
menor = 0
for _ in range(1, 6):
    weight = float(input(f'{_}º Peso: '))
    if _ == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print(f'Maior peso: {maior}\n'
      f'Menor peso: {menor}')
'''

# EXERCÍCIO 56 - Analisador completo
'''
sum_age = 0
c1 = 0
c2 = 0
older_age = 0
older_name = ''
for info in range(1, 5):
    print(f'----- {info}ª Pessoa -----')
    name = str(input('Nome: ')).strip().title()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: '))
    c1 += 1
    sum_age += age
    if gender in 'Ff' and age < 20:
        c2 += 1
    if gender == 'M':
        if info == 1:
            older_age = age
            older_name = name
        else:
            if age > older_age:
                older_age = age
                older_name = name
mean = sum_age / c1
print(f'Média de Idade: {mean} anos.\n'
      f'Homem mais velho: {older_name}, {older_age} anos.\n'
      f'{c2} mulheres menores de 20 anos.')
'''

'''>> ESTRUTURA DE REPETIÇÃO (while) <<'''


# EXERCÍCIO 57 - Validação de Dados - DESAFIO
'''
gender = ''
while gender in 'MF':
    gender = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if gender in 'Mm':
        gender = 'Masculino'
    elif gender in 'Ff':
        gender = 'Feminino'
    else:
        gender = ''
        print('Dados inválidos!')

print(f'Sexo: {gender}\n'
      f'Resgistrado com sucesso!')
'''

# EXERCÍCIO 58 - Jogo da Advinhação v2.0 - DESAFIO
'''
from random import randint
pc_choice = randint(0, 10)
play_choice = 0
c = 0
while play_choice != pc_choice:
    play_choice = int(input('Número: '))
    c += 1
    if play_choice > pc_choice:
        print('Menos...')
    elif play_choice < pc_choice:
        print('Mais...')

print(f'Número Sorteado: {pc_choice}\n'
      f'Tentativas realizadas: {c}')
'''
'''
from random import randint
pc = randint(0, 10)
attempts = 0
active = True
while active:
    play = int(input('Número: '))
    attempts += 1
    if play == pc:
        active = False
        print(f'Número Sorteado: {pc}\n'
              f'Tentativas: {attempts}')
    elif play > pc:
        print('Menos...')
    elif play < pc:
        print('Mais...')
'''

# EXERCÍCIO 59 - Criando um Menu de Opções - DESAFIO
'''
option = 0
while option != 5:
    num1 = int(input('1º Número: '))
    num2 = int(input('2º Número: '))
    print('[1] Soma\n'
          '[2] Multiplicação\n'
          '[3] Maior Valor\n'
          '[4] Novos Números\n'
          '[5] Sair')
    option = int(input('Opção: '))
    while option != 4 and option != 5:
        if option == 1:
            mode = 'Soma'
            result = num1 + num2
        elif option == 2:
            mode = 'Multiplicação'
            result = num1 * num2
        elif option == 3:
            mode = 'Maior'
            result = num1
            if num2 > num1:
                result = num2
        print(f'{mode}: {result}')
        option = int(input('Opção: '))
print('Aplicação Finalizda!')
'''

# EXERCÍCIO 60 - Cáluclo do Fatorial
'''
num = int(input('Número: '))
num1 = (num - 1)
fac = num * num1
while num1 > 1:
    num1 = num1 - 1
    fac = fac * num1
print(fac)
'''

# EXERCÍCIO 61 - Progressão Aritmética v2.0
'''
termo = int(input('1º Termo: '))
reason = int(input('Razão: '))
c = 1
print(termo, end='')
while c <= 9:
    c += 1
    termo = termo + reason
    print(f' > {termo}', end='')
'''

# EXERCÍCIO 62 - Progressão Aritmética v3.0
'''
termo = int(input('1º Termo: '))
reason = int(input('Razão: '))
c = 0
op = 1
z = 0
while op != 0:
    b = 9 + op
    if c >= 10:
        c = 10
    while c != b:
        z += 1
        c += 1
        print(f'{termo}')
        termo += reason
    op = int(input('Quantos termos mais? '))
    if op != 0:
        op += 1
print(f'Progressão Finalizada!\n'
      f'{z} Termos Mostrados')
'''

# EXERCÍCIO 63 - Sequência de Fibonacci v1.0
'''
msg = 'Sequência de Fibonacci'
print('-'*len(msg))
print(msg)
print('-'*len(msg))
num = int(input('Número: '))
new = 1
old = 0
s = 0
if num == 1:
    print(0)
elif num == 2:
    print(0)
    print(1)
elif num > 2:
    print(0)
    print(1)
    while s != num - 2:
        s += 1
        antigo_novo = new
        new = antigo_novo + old
        print(new)
        old = antigo_novo
'''

# EXERCÍCIO 64 - Tratando Vários Valores
'''
num = s = c = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        c += 1
        s += num
print(f'Números Digitados: {c}\n'
      f'Soma: {s}')
'''

# EXERCÍCIO 65 - Maior e Menor Valor
'''
r = 'S'
c = s = 0
ma = 0
me = 0
while 'S' == r != 'N':
    c += 1
    num = int(input('Número: '))
    s += num
    if c == 1:
        ma = me = num
    else:
        if num > ma:
            ma = num
        if num < me:
            me = num
    r = str(input('Continuar? [S/N]: ')).strip().upper()[0]

print(f'Números Digitados: {c}\n'
      f'Soma: {s}\n'
      f'Maior Valor: {ma}\n'
      f'Menor Valor: {me}')
'''

'''>> INTERROMPENDO REPETIÇÕES (while) <<'''

# EXERCÍCIO 66 - Vários Números Com Flag
'''
s = 0
print('Soma dos números\n'
      'Digite "999" para parar')
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
print(f'Soma: {s}')
'''

# EXERCÍCIO 67 - Tabuada v3.0
'''
print('Tabuada v3.0\n'
      'Digite um número negativo para parar')
from math import trunc
while True:
    num = int(input('Número: '))
    if num < 0:
        break
    print('-' * 11)
    for x in range(1, 11):
        print(f'{num} x {x:2} = {num * x:2}')
    print('-' * 11)
print('Aplicação Finalizada!')
'''

# EXERCÍCIO 68 - Jogo do Par ou Ímpar
'''
from random import randint
c = 0
while True:
    print('[1] Par\n'
          '[2] Ímpar')
    option = int(input('Opção: '))
    pc = randint(1, 10)
    if option == 1 or option == 2:
        num = int(input('Número: '))
        all = num + pc
        if option == 1:
            if all % 2 == 0:
                c += 1
                print('Ganhou!\n'
                  'Continue jogando!')
            else:
                print(f'Perdeu!\n'
                      f'{num} + {pc} = {all}\n'
                      f'{all} um número ÍMPAR')
                break
        else:
            if all % 2 == 1:
                c += 1
                print('Ganhou!\n'
                      'Continue jogando!')
            else:
                print(f'Perdeu!\n'
                      f'{num} + {pc} = {all}\n'
                      f'{all} um número PAR')
                break
    else:
        print('Escolha uma opção válida!')
print(f'Você acertou {c} vezes consecutivas.')
'''

# EXERCÍCIO 69 - Análise de Dados do Grupo
'''
age18_counter = male_counter = female_counter = 0
while True:
    print('CADASTRE UMA PESSOA')
    age = int(input('Idade: '))
    while True:
        gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if gender == 'M' or gender == 'F':
            break
    if age > 18:
        age18_counter += 1
    if gender == 'M':
        male_counter += 1
    if gender == 'F' and age < 20:
        female_counter += 1

    optn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if optn == 'N':
        break
print(f'_________________________\n'
      f'{age18_counter} Pessoas (+ de 18 anos)\n'
      f'{male_counter} Homens\n'
      f'{female_counter} Mulheres (- de 20 anos)')
'''

# EXERCÍCIO 70 - Estatística em Produtos
'''
cont = custo_total = milPlus = barato = 0
smallCost = ' '
while True:
    cont += 1
    product = str(input('Produto: ')).strip().title()
    price = float(input('Preço: R$ '))
    custo_total += price
    if price > 1000:
        milPlus += 1
    if cont == 1 or price < barato:
        barato = price
        smallCost = product
    r = ' '
    while r not in 'SN':
        r = str(input('Novo produto? [S/N] ')).upper().strip()
    if r == 'N':
        break
print(f'Custo total: {custo_total}\n'
      f'Acima de R$ 1000: {milPlus}\n'
      f'Mais barato: {smallCost}')
'''

# EXERCÍCIO 71 - Simulador de Caixa Eletrônico
'''
saque = int(input('Valor de Saque: R$ '))
listaCedulas = [50, 20, 5, 2, 1]
print('Cédulas:')
c = 0
while True:
    while c != len(listaCedulas):
        a = saque // listaCedulas[c]
        saque = saque % listaCedulas[c]
        if a != 0:
            print(f'R${listaCedulas[c]}: {a}')
        c += 1
    if c == len(listaCedulas):
        break
'''

'''>> Tuplas <<'''

# EXERCÍCIO 72 - Números por Extenso
'''
numbers1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numbers2 = ('onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
fill = numbers1 + numbers2
r = 'S'
while r == 'S':
    while True:
        num = int(input('Número entre 0 e 20: '))
        if num in range(0, 21):
            break
        print('Tente novamente.')
    print(f'O número {num} é igual a {str(fill[num]).title()}')
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if r == 'N':
        break
'''

# EXERCÍCIO 73 - Tuplas com Times de Futebol
'''
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'5 Primeiros:\n'
      f'{times[:5]}\n'
      f'4 Últimos:\n'
      f'{times[-4:]}\n'
      f'Ordem Alfabética:\n'
      f'{sorted(times)}')
'''

# EXERCÍCIO 74 - Maior e Menor Valor em Tupla
'''
from random import randint
a = (randint(0, 10), )
maior = menor = 0
for c in range(4):
    sorteio = randint(0, 10)
    b = (sorteio, )
    a = (a + b)
print(a)
print(max(a))
print(min(a))
'''

# EXERCÍCIO 75 - Análise de Dados em uma Tupla
'''
num = (int(input('Número: ')), int(input('Número: ')), int(input('Número: ')), int(input('Número: ')))
par = 0
for _ in num:
    if _ % 2 == 0:
        par += 1
print(f'Números Digitados:\n'
      f'{num}\n'
      f'O valor 9 apareceu {num.count(9)} vezes\n'
      f'{par} Valor(es) Par(es) Digitados')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O Valor 3 não apareceu em nenhuma posição')
'''

# EXERCÍCIO 76 - Lista de Preços com Tupla
'''
tup = ('Lápis', 1.75,
       'Borracha', 2.00,
       'Caderno', 15.90,
       'Estojo', 25.00,
       'Transferidor', 4.20,
       'Compasso', 9.99,
       'Mochila', 120.32,
       'Canetas', 22.30,
       'Livro', 34.90)

for _ in range(0, len(tup)):
    if _ % 2 == 0:
        print(f'{tup[_]:-<30}', end='')
    if _ % 2 == 1:
        print(f' R$ {tup[_]:>7.2f}')
'''

# EXERCÍCIO 77 - Contando Vogais em Tupla
'''
words = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRATICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO')
vog = ('A',
       'E',
       'I',
       'O',
       'U')
for palavra in words:
    print(f'Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in vog:
            print(f'{letra}', end=' ',)
    print('')
'''

'''>> Listas 1 <<'''

# EXERCÍCIO 78 - Maior e Menor Valor na Lista
'''
lista = list()
for num in range(5):
    lista.append(int(input(f'{num + 1}º Número: ')))
posMaior = list()
posMenor = list()
for a, b in enumerate(lista):
    if b == max(lista):
        posMaior.append(a)
    if b == min(lista):
        posMenor.append(a)
print(f'Números Digitados: {lista}\n'
      f'Maior Valor: {max(lista)}\n'
      f'Posições: {posMaior}\n'
      f'Menor Valor: {min(lista)}\n'
      f'Posições: {posMenor}')
'''

# EXERCÍCIO 79 - Valores Únicos em uma Lista
'''
lista = []
print('Digite "parar" para encerrar')
while True:
    num = input('Número: ').strip().upper()
    if num == 'PARAR':
        break
    if num.isnumeric():
        num = int(num)
        if num not in lista:
            lista.append(num)
    else:
        print('Digite um número!')
print(f'Os números únicos digitados foram:\n'
      f'{sorted(lista)}')
'''

# EXERCÍCIO 80 - Lista Ordenada Sem Repetições
'''
lista = []
pos = 0
for n in range(5):
    num = int(input('Número: '))
    if n == 0:
        lista.append(num)
    else:
        for item in lista:
            if num < item:
                lista.insert(lista.index(item), num)
                break
            if num > max(lista):
                lista.append(num)
            pos = lista.index(item)
    print(f'Adicionado na Posição: {pos}')
print(f'Valores Adicionados:\n{lista}')
'''

# EXERCÍCIO 81 - Extraindo Dados de uma Lista
'''
print('Digite "parar" para encerrar.\n')
lista = []
EstouSemCriatividadePraNome = 'Não'
while True:
    num = str(input('Número: ')).strip().upper()
    if num == 'PARAR':
        break
    if num.isnumeric():
        lista.append(int(num))
    else:
        print('Digite um número')
    if 5 in lista:
        EstouSemCriatividadePraNome = 'Foi'
lista.sort(reverse=True)
print(f'Números Digitados: {len(lista)}\n'
      f'Ordem decrescente: {lista}\n'
      f'Valor 5: {EstouSemCriatividadePraNome} Digitado')
'''

# EXERCÍCIO 82 - Dividindo Valores em Várias Listas
'''
listaTotal = []
listaPar = []
listaImpar = []
while True:
    num = str(input('Número: ')).upper().strip()
    if num == 'PARAR':
        break
    if num.isnumeric() is True:
        listaTotal.append(int(num))
    else:
        print('Digite um Número!')
for item in listaTotal:
    if item % 2 == 0:
        listaPar.append(item)
    if item % 2 == 1:
        listaImpar.append(item)

print(f'Lista Total: {listaTotal}\n'
      f'Lista Par: {listaPar}\n'
      f'Lista Ímpar: {listaImpar}')
'''

# EXERCÍCIO 83 - Validando Expressões Matemáticas
'''
parenteses = []
exp = input('Digite a Expressão: ').strip()
for letras in exp:
    if letras == '(' or letras == ')':
        parenteses.append(letras)

# (((a+b)*2)/(a*(2+b)))


if parenteses.count('(') == parenteses.count(')'):
    while True:
        if parenteses.count('(') == 1:
            if parenteses[0] == '(' and parenteses[-1] == ')':
                print('Expressão Válida!')
                break
        else:
            if parenteses[0] == '(' and parenteses[-1] == ')':
                del parenteses[0]
                del parenteses[-1]
            elif parenteses[0] == ')' and parenteses[-1] == '(':
                del parenteses[0]
                del parenteses[-1]
else:
    print('Expressão Inválida!')
'''  # Falha - Tentar depois
'''
parenteses = []
exp = input('Digite a Expressão: ').strip()
for letra in exp:
    if letra == '(':
        parenteses.append(letra)
    elif letra == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            break
if len(parenteses) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
'''

'''>> Listas 2 <<'''

# EXERCÍCIO 84 - Lista Composta e Análise de Dados
'''
lista = []
data = []
print('Digite "parar" a Qualquer\nMomento para Encerrar!\n')
while True:
    name = str(input('Nome: ')).strip().title()
    if name == 'Parar':
        break
    weight = str(input('Peso: ')).strip().title()
    if weight == 'Parar':
        break
    weight = float(weight)
    data.append(name)
    data.append(weight)
    lista.append(data[:])
    data.clear()
maxW = minW = c = 0
for pessoa in lista:
    if c == 0:
        maxW = minW = pessoa
    else:
        if pessoa[1] > maxW[1]:
            maxW = pessoa
        if pessoa[1] < minW[1]:
            minW = pessoa
    c += 1
print(f'{len(lista)} Pessoas Cadastradas\n'
      f'Maior Peso: {maxW[1]} kg, {maxW[0]}\n'
      f'Menor Peso: {minW[1]} kg, {minW[0]}')
'''

# EXERCÍCIO 85 - Listas com Pares e Ímpares
'''
numeros = [[], []]
for loop in range(1, 8):
    num = int(input(f'{loop}º Número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)

print(f'Pares: {sorted(numeros[0])}\n'
      f'Ímpares: {sorted(numeros[1])}')
'''

# EXERCÍCIO 86 - Matriz em Python
'''
matriz = [[], [], []]
c = 0
while len(matriz[2]) != 3:
    for giro in range(3):
        matriz[c].append(int(input(f'[{c}, {giro}]: ')))
    c += 1
print(f'[{matriz[0][0]:^3}] [{matriz[0][1]:^3}] [{matriz[0][2]:^3}]\n'
      f'[{matriz[1][0]:^3}] [{matriz[1][1]:^3}] [{matriz[1][2]:^3}]\n'
      f'[{matriz[2][0]:^3}] [{matriz[2][1]:^3}] [{matriz[2][2]:^3}]')
'''

# EXERCÍCIO 87 - Mais Sobre Matriz em Python
'''
matriz = [[], [], []]
c = 0
par = 0
ter = 0
while len(matriz[2]) != 3:
    for loop in range(3):
        matriz[c].append(int(input(f'[{c}, {loop}]: ')))
        if matriz[c][loop] % 2 == 0:
            par += matriz[c][loop]
    ter += matriz[c][2]
    c += 1
print(f'[{matriz[0][0]:^3}] [{matriz[0][1]:^3}] [{matriz[0][2]:^3}]\n'
      f'[{matriz[1][0]:^3}] [{matriz[1][1]:^3}] [{matriz[1][2]:^3}]\n'
      f'[{matriz[2][0]:^3}] [{matriz[2][1]:^3}] [{matriz[2][2]:^3}]')

print(f'Soma de Pares: {par}\n'
      f'Soma 3ª Coluna: {ter}\n'
      f'Máximo 2ª Linha: {max(matriz[1])}')
'''

# EXERCÍCIO 88 - Palpites Para a Mega Sena
'''
from random import randint
from time import sleep
jogos = int(input('Quantos Jogos? '))
for attempt in range(jogos):
    matriz = []
    while len(matriz) != 6:
        num = randint(1, 60)
        if num not in matriz:
            matriz.append(num)
    print(f'\n{attempt + 1}º Jogo: {sorted(matriz)}')
    matriz.clear()
    sleep(0.5)
'''

# EXERCÍCIO 89 - Boletim com Listas Compostas
'''
alunos = []
nomes = []
notas = []
while True:
    nome = str(input('Nome: ')).strip().title()
    if nome == 'Parar':
        break
    nota1 = str(input(f'1ª Nota: ')).strip().title()
    if nota1 == 'Parar':
        break
    nota2 = str(input(f'2ª Nota: ')).strip().title()
    if nota2 == 'Parar':
        if len(notas) > 0:
            nomes.clear()
            notas.clear()
        break
    if nota1.isnumeric() and nota2.isnumeric():
        notas.append(float(nota1))
        notas.append(float(nota2))
    else:
        print('Digite números!')

    nomes.append(nome)
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()

print(f'{"Nº":<5}{"Nome":<15}Média')
for aluno in alunos:
    print(f'{alunos.index(aluno):<5}{aluno[0]:<15}{(aluno[1][0] + aluno[1][1]) / 2}')

while True:
    option = str(input('\nExibir Detalhes: Nº ')).strip().upper()
    if option == 'PARAR':
        break
    if option.isnumeric():
        option = int(option)
        print(f'Aluno: {alunos[option][0]}\n'
              f'Notas: {alunos[option][1]}')
'''
'''
dados = []
notas = []
print('\nDigite "parar" a qualquer momento para encerrar!\n')
while True:
    stop = False
    nome = str(input('Nome: ')).strip().title()
    if nome == 'Parar':
        break
    while len(notas) != 2:
        nota = str(input(f'{len(notas) + 1}ª Nota: ')).strip().title()
        if nota == 'Parar':
            if len(nota) != 0:
                notas.clear()
            stop = True
            break
        if nota.isnumeric():
            nota = float(nota)
            notas.append(nota)
    mean = (sum(notas) / len(notas))
    if stop:
        break
    dados.append([nome, notas[:], mean])
    notas.clear()

print(f'{"Nº":<5}{"Nome":<20}{"Média":^5}')
for i, aluno in enumerate(dados):
    print(f'{i:<5}{aluno[0]:<20}{aluno[2]:^5}')

print('\nDigite "parar" para encerrar!\n')
while True:
    option = str(input('Exibir Detalhes: Nº ')).strip().upper()
    if option == 'PARAR':
        break
    if option.isnumeric():
        option = int(option)
        if option <= len(dados) - 1:
            print(f'Aluno: {dados[option][0]}\n'
                  f'Notas: {dados[option][1]}')
        else:
            print('Aluno não encontrado!')
print(len(dados))
'''

'''>> Dicionários <<'''

# EXERCÍCIO 90 - Dicionário em Python
'''
dados = {'aluno': str(input('Aluno: ')).strip().title(),
         'média': float(input('Média: '))
         }
if dados['média'] < 5:
    dados['status'] = 'Reprovado'
elif dados['média'] < 7:
    dados['status'] = 'Recuperação'
else:
    dados['status'] = 'Aprovado'

for k, v in dados.items():
    print(f'- {k.title()}: {v}')
'''

# EXERCÍCIO 91 - Jogos de Dados em Python
'''
from random import randint
from time import sleep
from operator import itemgetter
dic = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6),
}
for k, v in dic.items():
    print(f'{k.title()} tirou o número {v} ')
    sleep(1)

rank = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(f'\n{"== RANKING DOS JOGADORES ==":^20}')
for i, v in enumerate(rank):
    print(f'{i + 1}º Lugar: {v[0]}, com {v[1]}')
    sleep(1)
'''

# EXERCÍCIO 92 - Cadastro de Trabalhador em Python
'''
from datetime import datetime
info = {'Nome': str(input('Nome: ')).strip().title(),
        'Idade': datetime.today().year - int(input('Ano de Nascimento: ')),
        'CTPS': int(input('CTPS (0 Não Possui): '))
        }
if info['CTPS'] != 0:
    info['Ano de Contratação'] = int(input('Ano de Contratação: '))
    info['Salário'] = float(input('Salário: R$ '))
    info['Aposentadoria'] = info['Idade'] + ((info['Ano de Contratação'] + 35) - datetime.now().year)
else:
    info['CTPS'] = 'Não possui'

print('__________________________________________')
for k, v in info.items():
    print(f'{k} - {v}')
'''

# EXERCÍCIO 93 - Cadastro de Jogador de Futebol
'''
principal = {'Nome': str(input('Nome do Jogador: ')).strip().title()}
gols = []
match = int(input('Partidas: '))
for loop in range(match):
    gols.append(int(input(f'[Partida {loop + 1}] Gols:  ')))
principal['Gols'] = gols
principal['Total'] = sum(principal['Gols'])
print('-=-' * 19)
print(principal)
print('-=-' * 19)
for k, v in principal.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 19)
print(f'O jogador {principal["Nome"]} jogou {match} partidas.')
for i, n in enumerate(principal['Gols']):
    print(f'   => Na partida {i + 1}, fez {n} gols.')
print(f'   => Total: {principal["Total"]} gols.')
'''

# EXERCÍCIO 94 - Unindo Dicionários e Listas
'''
principal = list()
dados = dict()
idades = []
mulheres = []
media_plus = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Favor digitar "M" para Masculino ou "F" para Feminino!')
    dados['Idade'] = int(input('Idade: '))
    principal.append(dados.copy())
    idades.append(dados['Idade'])
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    while True:
        resp = str(input('Adicionar mais? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Favor digitar "S" para Sim ou "N" para Não!')
    if resp == 'N':
        break

print(f'(A) Total: {len(principal)} Pessoas\n'
      f'(B) Idade (média): {sum(idades) / len(idades):.2f}\n'
      f'(C) Mulheres: ', end='')
for i, mulher in enumerate(mulheres):
    if i + 1 != len(mulheres):
        print(f'{mulher}', end=', ')
    else:
        print(mulher)
print(f'(D) Acima da média:')
for dado in principal:
    if dado['Idade'] > (sum(idades) / len(idades)):
        for k, v in dado.items():
            if k != 'Idade':
                print(f'   {k} = {v:<8}', end='')
            else:
                print(f'{k} = {v}', end='')
        print()
'''

# EXERCÍCIO 95 - Aprimorando os Dicionários
'''
team = []
player = {}
while True:
    player.clear()
    player['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    player['Gols'] = list(range(int(input('Partidas: '))))
    for i, v in enumerate(player['Gols']):
        player['Gols'][i] = int(input(f'[{i + 1}ª Partida] Gols: '))
    player['Total'] = sum(player['Gols'])
    team.append(player.copy())
    while True:
        resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Favor digitar apenas "S" para Sim ou "N" para Não!')
    if resp == 'N':
        break

a = f'{"Nº":<3}{"Nome":<25}{"Gols":<25}{"Total"}'
print(a)
print('-' * len(a))
for i, p in enumerate(team):
    print(f'{i + 1:<3}' + f'{p["Nome"]:<25}' + f'{str(p["Gols"]):<25}' + f'{p["Total"]}')
print('-' * len(a))

while True:
    opc_1 = str(input('Quer Analisar os Gols Por Partida? [S/N]: ')).strip().upper()
    if opc_1 in 'SN':
        break
    print('ERRO! Favor digitar apenas "S" para Sim ou "N" para Não!')
if opc_1 == 'S':
    while True:
        while True:
            opc_2 = str(input('Nº Jogador: ')).upper().strip()
            if opc_2.isnumeric():
                opc_2 = int(opc_2)
                if opc_2 <= len(team):
                    break
                print('ERRO! Favor digitar uma opção da lista!')
            else:
                if opc_2 == 'PARAR':
                    break
                print('ERRO! Favor digitar apenas números!')
        if opc_2 == 'PARAR':
            break
        for ind, val in enumerate(team[opc_2 - 1]["Gols"]):
            print(f'[{ind + 1}ª Partida] Gols: {val}')
        print('Digite "parar" para encerrar!')
'''

'''>> Funções 1 <<'''

# EXERCÍCIO 96 - Função que Calcula Área
'''
def area(length, width):
    print(length * width, end=' m²')


print('Insira dimensões em metro (m)')
comp = float(input('Comprimento: '))
larg = float(input('Largura: '))

area(comp, larg)
'''

# EXERCÍCIO 97 - Um Print Especial
'''
def escreva(msg):
    tam = len(msg)
    print('-' * (tam + 6))
    print('--', end=' ')
    print(f'{msg:^{tam}}', end=' --')
    print()
    print('-' * (tam + 6))


msg = str(input('Mensagem: ')).strip().title()
escreva(msg)
'''

# EXERCÍCIO 98 - Função de Contador
'''
from time import sleep


def contador(start, end, step):
    print('-' * 30)
    for loop in range(start, end, step):
        print(loop, end=' ')
        sleep(0.5)
    print()
    print('-' * 30)


ct = 1
while True:
    if ct == 1:
        contador(0, 10, 1)

    elif ct == 2:
        contador(10, 0, -2)

    elif ct == 3:
        c = int(input('Começo: '))
        f = int(input('Final: '))
        s = int(input('Passo: '))
        if f > c:
            if s > 0:
                f += 1
            elif s < 0:
                print('Como passos negativos só podem ser usados para contagens regressivas\n'
                      'Considerarei erro de digitação e prosseguerei como pregressiva')
                s *= (-1)
                f += 1
            else:
                s = 1
                f += 1
        else:
            if s > 0:
                s *= (-1)
                f -= 1
            elif s < 0:
                f -= 1
            else:
                s = -1
                f -= 1

        print('-' * 30)
        contador(c, f, s)
        break
    ct += 1
'''
'''
# Feito por outra pessoa, analisar código
def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('FIM!')
    sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
'''
# EXERCÍCIO 99 - Função que Descobre o Maior
'''
def maior(* num):
    from time import sleep
    print('Analisando os Valores Passados')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    print()
    print(f'Maior Valor: {max(num)}\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
'''

# EXERCÍCIO 100 - Função Para Sortear e Somar
'''
def sorteio(arg):
    from random import randint
    for loop in range(5):
        arg.append(randint(0, 10))
    print(arg)

def somaPar(arg):
    c = 0
    for num in arg:
        if num % 2 == 0:
            c += num
    print(c)


lista = []
sorteio(lista)
somaPar(lista)
'''

'''>> Funções 2 <<'''

# EXERCÍCIO 101 - Funções para Votação
'''
def voto(year=0):
    """
    :param year: Ano de Nascimento
    :return: Checagem de obrigatoriedade de voto
    """  # DOCSTRING
    from datetime import date
    a = date.today().year - year
    if a < 16:
        return f'{a} anos: Voto Negado'
    if a < 18 or a > 65:
        return f'{a} anos: Voto Opcional'
    else:
        return f'{a} anos: Voto Obrigatório'


print(voto(int(input('Ano de Nascimento: '))))
'''

# EXERCÍCIO 102 - Função para Fatorial
'''
def fac(value, show=False):
    """
    Função para calculo de fatorial com detalhamento opcional da operação.
    :param value: Valor a calcular fatorial
    :param show: Expressar na tela detalhamento da expressão
    :return: Valor fatorado do parametro 'value'
    """  # DOCSTRING
    for loop in range(value - 1, 0, -1):
        if show:
            print(f'{value} x {loop}', end=' -> ')
        value *= loop

    return value


print(fac(5, show=True))
'''

# EXERCÍCIO 103 - Ficha do Jogador
'''
def ficha(name='', gols=0):
    if name == '':
        name = '<desconhecido>'
    if gols == 0:
        gols = 0
    return print(f'O jogador {name} fez {gols} gol(s) no campeonato')


n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: ')).strip()
if g != '' and g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
'''

# EXERCÍCIO 104 - Validando Entrada de Dados
'''
def lerInt(number):
    while True:
        n = str(input(f'{number}'))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f'\33[0;31mERRO! Digite um número inteiro válido!\33[m')
    return n


n = lerInt('Número: ')
print(f'Número Digitado: {n}')
'''

# EXERCÍCIO 105 - Analisando e Gerando Dicionários
'''
def notes(* notas, sit=False):
    """
    -> Função para análise de notas de alunos.
    :param notas: Valores das notas dos alunos. Quantidade Opcional
    :param sit: Adição opcional da calculo/situação referente a média do aluno
    :return: Retorna dicionário com dados analisados
    """
    dic = {'Total': len(notas),
           'Maior': max(notas),
           'Menor': min(notas),
           'Média': sum(notas) / len(notas)
    }
    if sit:
        if dic['Média'] < 5:
            dic['Situação'] = 'Ruim'
        elif dic['Média'] < 7:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Boa'
    return dic


resp = notes(5.5, 6, 10)
print(resp)
'''

# EXERCÍCIO 106 - Sistema Interativo de Ajuda em Python
'''
def helpSys(param):
    return help(param)


while True:
    b = input('Função ou Biblioteca: ').strip().lower()
    if b == 'parar':
        break
    else:
        if b.isalpha():
            helpSys(b)
'''

'''>> Módulos e Pacotes <<'''

# EXERCÍCIO 107 - Módulos e Pacotes
'''
import func
p = float(input('Preço: R$ '))
print(f'Metade de {p}: > {func.metade(p)}\n'
      f'Dobro de {p}: > {func.dobro(p)}\n'
      f'Aumentando 10%: >  {func.aumentar(p, 10)}\n'
      f'Reduzindo 13%: > {func.aumentar(p, 13, reverse=True)}')
'''

# EXERCÍCIO 108 - Formatando Moedas em Python
'''
from func import *
p = float(input('Preço: R$ '))
print(f'Metade de {real(p)}: > {real(metade(p))}\n'
      f'Dobro de {real(p)}: > {real(dobro(p))}\n'
      f'Aumentando 10%: >  {real(aumentar(p, 10))}\n'
      f'Reduzindo 13%: > {real(aumentar(p, 13, reverse=True))}')
'''

# EXERCÍCIO 109 - Formatando Moedas em Python
='''
from func import *
p = float(input('Preço: R$ '))
print(f'Metade de {p}: > {metade(p, True)}\n'
      f'Dobro de {p}: > {dobro(p, True)}\n'
      f'Aumentando 10%: >  {aumentar(p, 10, money=True)}\n'
      f'Reduzindo 13%: > {aumentar(p, 13, reverse=True, money=True)}')
'''

# EXERCÍCIO 110 - Reduzindo Ainda Mais Seu Código
'''
from func import *

num = float(input('Preço: R$ '))
resumo(num, 80, 35)
'''

# EXERCÍCIO 111 - Transformando Módulos em Pacotes
from cevu import moeda

num = float(input('Preço: R$ '))
moeda.resumo(num, 150, 22)