"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

Para calcular a área de um quadrado é muito simples.
No quadrado os lados são iguais, logo é só pegar um dos lados e
multiplicar por ele mesmo, assim temos a área do quadrado.

Fórmula para pegar a área do quadrado:
area = lado * lado
"""

print("Calculando a area do quadrado")

lado = float(input("Lado do quadrado: "))

area = lado * lado

print ("A area do quadrado eh %.2f m2" %area)
