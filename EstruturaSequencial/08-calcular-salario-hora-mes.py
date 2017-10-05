"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

Fórmula:
salario = valor_por_hora * numero_horas

"""

print("Calcular o salario")

valor_por_hora = float(input("Valor por hora: "))
numero_horas = float(input("Horas trabalhadas: "))

salario = valor_por_hora * numero_horas

print("O valor por hora R$ %.2f multiplicado por %.2f horas trabalhadas eh R$ %.2f" %(valor_por_hora, numero_horas, salario))
