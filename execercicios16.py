# peça ao usuario o tamanho da area que deve ser pintada
# 1L de tinta pinta 3 metros quadrados
# a lata de tinta tem de 18L e cada uma custa 80,00R$
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# 18L pintam 54 metros quadrados de parede

def calcular_tinta(area_necessaria):
    cobertura_tinta = 3  # metros quadrados por litro
    litros_por_lata = 18  # Lata de tinta: 18 litros
    preco_por_lata = 80.00  # Preço da lata de tinta em reais
    
    litros_necessarios = area_necessaria / cobertura_tinta # Calcular a quantidade de litros necessários
    
    if litros_necessarios % litros_por_lata == 0: # Calcular a quantidade de latas necessárias
        latas_necessarias = litros_necessarios // litros_por_lata
    else:
        latas_necessarias = (litros_necessarios // litros_por_lata) + 1
    
    preco_total = latas_necessarias * preco_por_lata# Calcular o preço total
    
    return latas_necessarias, preco_total

def main():
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))# Solicitar o tamanho da área a ser pintada

    latas, preco = calcular_tinta(area)# Calcula a quantidade de latas e o preço total

    print(f"Quantidade de latas de tinta a serem compradas: {latas}")
    print(f"Preço total: R$ {preco:.2f}")

if __name__ == "__main__":
    main()
