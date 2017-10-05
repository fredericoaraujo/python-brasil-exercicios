"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

int1 = int(input("Informe um numero inteiro: "))
int2 = int(input("Informe um numero inteiro: "))
float1 = float(input("Informe um numero real: "))

"""
a) o produto do dobro do primeiro com metade do segundo .
"""
calc_a = (2 * int1) * (int2 / 2)

print("o produto do dobro do primeiro com metade do segundo eh %.2f" %calc_a)

"""
b) a soma do triplo do primeiro com o terceiro.
"""

calc_b = 3 * int1 + float1

print("a soma do triplo do primeiro com o terceiro eh %.2f" %calc_b)

"""
c) o terceiro elevado ao cubo.
"""

calc_c = float1 ** 3

print("o terceiro elevado ao cubo eh %.2f" %calc_c)
