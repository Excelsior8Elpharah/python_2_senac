salario = float(input("Digite seu salário: "))
if salario > 3999.99:
    desconto = salario * 15/100
    sal_desc = salario - desconto
elif salario > 2500.00 and salario < 4000.00:
    desconto = salario * 10/100
    sal_desc = salario - desconto
elif salario > 1500.00 and salario < 2500.00:
    desconto = salario * 5/100
    sal_desc = salario - desconto
else:
    salario = salario
print(f"Seu descontos é : {desconto}")
print(f"Seu salario com desconto é: {sal_desc}")