ganhos_hora = float(input("Quantos voce ganha por hora ?: "))
horas_trabalhadas = float(input("Quantas horas voce trabalhou esse mes ?: "))

salario = ganhos_hora * horas_trabalhadas 

print(f"Voce trabalhou {horas_trabalhadas} horas, e ganha {ganhos_hora} reais por hora, entao recebera {salario:.2f} reais este mes !.")
