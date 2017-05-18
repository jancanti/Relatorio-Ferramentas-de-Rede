#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello World!")

#2 Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".
a = int(input("Digite um número: "))
print("O número informado foi " %a)

#3Faça um Programa que peça dois números e imprima a soma.
a = int(input("Digite o 1o número: "))
b = int(input("Digite o 2o número: "))
print(a+b)

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
a = int(input("Digite a 1a nota: "))
b = int(input("Digite a 2a nota: "))
c = int(input("Digite a 3a nota: "))
d = int(input("Digite a 4a nota: "))

m = (a+b+c+d)/4
print("Sua média é: %.2f" %m)

#5 Faça um Programa que converta metros para centímetros
m = float(input("Digite a medida em METROS: "))
cm = m*100
print("%.2f metros em cm = %.2f" %(m,cm))

#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
r = float(input("Digite o raio: "))
a = math.pi * math.pow(r,2)

print("A área do círculo é: %.2f" %a)

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
q = float(input("Digite o valor do lado do quadradro: "))
a = math.pow(a,2)
d = a*2

print("O dobro da área do quadrado é: %.f" %d)

#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
h = float(input("Valor da hora trabalhada: "))
t = float(input("Horas trabalhadas no mês: "))
s = h*t

print("Esse mês, seu salário será de: %.2f" %s)

#9 Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
f = float(input("Digite a temperatura em Farenheit: "))
c = (5 * (f-32) / 9)

print("Temperatura em Celsius é: %.2f" %c)

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
c = float(input("Digite a temperatura em Celsius: "))
f = (c * 1,8) + 32

print("Temperatura em Farenheit é: %.2f" %f)

# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
n3 = float(input("Digite o n3: "))

a = (n1*2) * (n2/2)
b = (n1 + n3) * 3
c = math.pow(n3,3)

print("A: %.2f" %a)
print("B: %.2f" %b)
print("C: %.2f" %c)

#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
a = float(input("Digite sua altura: "))
i = (72.7 * a) - 58

print("Seu peso ideal é: %.2f" %i)

# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
