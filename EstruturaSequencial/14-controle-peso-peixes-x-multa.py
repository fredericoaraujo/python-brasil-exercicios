"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de
peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na
variável multa o valor da multa que João deverá pagar. Caso contrário mostrar
tais variáveis com o conteúdo ZERO.

"""


peso_de_peixes = 0
excesso = 0
valor_da_multa = 0

peso_de_peixes = float(input('Peso dos peixes: '))

if peso_de_peixes > 50.0:
    excesso = peso_de_peixes - 50.0
    valor_da_multa = 4.0 * excesso

print('Peso de Peixes: {} kg\nExcesso: {} kg\nValor da Multa R$: {}'.format(peso_de_peixes, excesso, valor_da_multa))