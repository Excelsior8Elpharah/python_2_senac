idade = int(input("Digite o ano que você nasceu: "))
idade = 2025 - idade
print(f"Sua idade é : {idade}")
if idade < 17:
    print("Menor de idade")
else:
    print("Maior de idade")

altura = float(input("Digite sua altura: "))
altura = altura ** altura
print(f"Sua altura ao quadrado é : {altura}")
altura_prof = 1.67
if altura < altura_prof:
    print("Professora é mais alta.")
elif altura > altura_prof:
    print("Professora é mais baixa.")
else:
    print("Mesma altura")

