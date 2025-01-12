km_percorridos = float(input("Quantos km foram percorridos pelo carro? "))
dias_aluguel = int(input("Por quantos dias o carro foi alugado? "))
preco = dias_aluguel * 60 + km_percorridos * 0.15
print(f"O total a pagar é de R${preco:.2f}")
