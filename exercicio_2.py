nht = int(input("Informe o número de horas trabalhadas: "))
vph = float(input("Informe o valor pago por hora trabalhada: "))
ptd = float(input("Informe o percentual total de descontos: "))

sb = nht * vph
desconto = sb * (ptd/100)
sl = sb - desconto

print(f"O salário base é: {sb}")
print(f"O desconto é: {desconto}")
print(f"O salário líquido é: {sl}")