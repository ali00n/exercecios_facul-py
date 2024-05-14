altura_homens = float(input("Homem: digite sua altura em metros... "))

altura_mulheres = float(input("Mulher: digite sua altura em metros... "))

peso_ideal_homens =  (72.7*altura_homens) - 58

peso_ideal_mulheres =  (62.1*altura_mulheres) - 44.7


print(f"O seu peso ideal sendo homem é de {peso_ideal_homens:.2f} kg !")

print(f"O seu peso ideal sendo mulher é de {peso_ideal_mulheres:.2f} kg !")