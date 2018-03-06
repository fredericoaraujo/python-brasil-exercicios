"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
"""

LATA_18 = 18
LATA_3_6 = 3.6
PRECO_LATA_18 = 80.0
PRECO_LATA_3_6 = 25.0
LATA_UM_LITRO_PINTA_AREA_M2 = 6
TOTAL_AREA_M2_UMA_LATA_18_PINTA = LATA_18 * LATA_UM_LITRO_PINTA_AREA_M2
TOTAL_AREA_M2_UMA_LATA_3_6_PINTA = LATA_3_6 * LATA_UM_LITRO_PINTA_AREA_M2
AREA_DE_FOLGA = 1.1

quantidade_de_latas_18_para_pintura = 0
quantidade_de_latas_3_6_para_pintura = 0
total_preco = PRECO_LATA_3_6

tamanho_de_area_pintada = 100 #float(input('Tamanho em m2:'))
tamanho_de_area_pintada *= AREA_DE_FOLGA


if TOTAL_AREA_M2_UMA_LATA_3_6_PINTA < tamanho_de_area_pintada < TOTAL_AREA_M2_UMA_LATA_18_PINTA:
    total_preco = PRECO_LATA_18
    quantidade_de_latas_18_para_pintura = 1
elif TOTAL_AREA_M2_UMA_LATA_18_PINTA < tamanho_de_area_pintada:
    quantidade_de_latas_18_para_pintura = tamanho_de_area_pintada // TOTAL_AREA_M2_UMA_LATA_18_PINTA
    if tamanho_de_area_pintada % TOTAL_AREA_M2_UMA_LATA_18_PINTA > 0:
        area_restante = ((quantidade_de_latas_18_para_pintura * TOTAL_AREA_M2_UMA_LATA_18_PINTA)
                         - tamanho_de_area_pintada)
        if TOTAL_AREA_M2_UMA_LATA_3_6_PINTA < area_restante:
            quantidade_de_latas_3_6_para_pintura = area_restante // TOTAL_AREA_M2_UMA_LATA_3_6_PINTA
            if area_restante % TOTAL_AREA_M2_UMA_LATA_3_6_PINTA:
                quantidade_de_latas_3_6_para_pintura += 1

    total_preco = (quantidade_de_latas_3_6_para_pintura * PRECO_LATA_3_6) + (quantidade_de_latas_18_para_pintura * PRECO_LATA_18)


print("""
QTDE de Latas 18: {}\n
QTDE de Latas 3,6: {}\n
Preço R$: {}
""".format(quantidade_de_latas_18_para_pintura, quantidade_de_latas_3_6_para_pintura, total_preco))