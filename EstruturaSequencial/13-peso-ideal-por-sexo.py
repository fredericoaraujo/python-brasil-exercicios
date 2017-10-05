"""
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 (h = altura)
    Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

print("Calcular peso ideal por sexo")

sexo = input("Qual o sexo (M/F): ")
altura = float(input("Qual sua altura: "))

if (sexo == "M"):
    peso_ideal = (72.7*altura) - 58
else :
    peso_ideal = (62.1*altura) - 44.7

print("Para o sexo %s e altura %.2f o peso ideal %.2f" %(sexo, altura, peso_ideal))
