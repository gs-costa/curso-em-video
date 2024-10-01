preco = float(input("Qual é o preço do produto? R$"))
desconto = float(input("Qual é o desconto do produto? Em %"))
preco_desconto = preco - (preco * desconto / 100)
print(
    f"O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}%, vai custar R${preco_desconto:.2f}"
)
