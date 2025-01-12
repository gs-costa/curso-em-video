from math import sqrt


oposto = float(input("Valor do cateto oposto: "))
adjacente = float(input("Valor do cateto adjacente: "))
hipotenusa = sqrt(oposto**2 + adjacente**2)
print(f"Valor da hipotenusa é: {hipotenusa:.2f}")
