valor_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_por_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f"+ Salário Bruto :{salario_bruto:.2f} R$")
print(f"- IR (11%) :{ir:.2f} R$")
print(f"- INSS (8%) : {inss:.2f} R$")
print(f"- Sindicato (5%) :{sindicato:.2f} R$")
print(f"= Salário Liquido :{salario_liquido:.2f} R$")
