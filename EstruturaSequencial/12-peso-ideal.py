"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

"""

print("Calculando o peso ideal")

altura = float(input("Informe a altura: "))

peso_ideal = (72.7*altura) - 58

print("O seu peso ideal eh %.2f" %peso_ideal)
