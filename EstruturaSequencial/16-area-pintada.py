"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.
"""

LITROS_LATA = 18
PRECO_LATA = 80.0
LITRO_PINTA_AREA_M2 = 3
TOTAL_AREA_M2_UMA_LATA_PINTA = LITROS_LATA * LITRO_PINTA_AREA_M2

quantidade_de_latas_para_pintura = 1
total_preco = PRECO_LATA

tamanho_de_area_pintada = float(input('Tamanho em m2:'))

if TOTAL_AREA_M2_UMA_LATA_PINTA < tamanho_de_area_pintada:
    quantidade_de_latas_para_pintura = tamanho_de_area_pintada // TOTAL_AREA_M2_UMA_LATA_PINTA
    if tamanho_de_area_pintada % TOTAL_AREA_M2_UMA_LATA_PINTA > 0:
        quantidade_de_latas_para_pintura += 1
    total_preco = quantidade_de_latas_para_pintura * PRECO_LATA

print("""
QTDE de Latas: {}\n
Preço R$: {}
""".format(quantidade_de_latas_para_pintura, total_preco))