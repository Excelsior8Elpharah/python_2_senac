idade = int(input("Qual a sua idade: "))
tem_carteira = input("Tem carteira de motorista? Digite 'S' para SIM, e 'N' para NÃO: ").lower
if idade >= 18 and tem_carteira == "s":
    print("Pode dirigir")
else:
    print("Não pode dirigir")
