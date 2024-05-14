peso = float(input("Digite o peso dos peixes em KG: "))

if peso > 51:
    excesso = peso - 50
    multa = excesso * 4 
    print(f"O peso excedente é de {excesso} kg")
    print(f"A multa a ser paga é de {multa}R$")
    
else:
    print("Nao houve excesso de peso, nenhuma multa sera aplicada")