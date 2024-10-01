salario = float(input("Digite o salário: R$ "))
aumento = float(input("Digite o aumento(em %): "))
salario_aumento = salario + (salario * aumento / 100)
print(
    f"O salário que era de R${salario:.2f}, com aumento de {aumento}%, passará a ser de R${salario_aumento:.2f}"
)
