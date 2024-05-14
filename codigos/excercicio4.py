def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    notas = []

    # Solicitar as notas ao usuário
    for i in range(4):
        nota = float(input("Digite a nota do {}º bimestre: ".format(i + 1)))
        notas.append(nota)

    # Calcular a média das notas
    media = calcular_media(notas)

    # Imprimir a média
    print("A média das notas é:", media)

if __name__ == "__main__":
    main()
