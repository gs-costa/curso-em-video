nome = input("Digite seu nome completo: ")

print(f"Nome completo em letras maiúsculas é {nome.upper()}")
print(f"Nome completo em letras minúsculas é {nome.lower()}")
quantidade_letras = len(nome.replace(" ", "")) or (len(nome) - nome.count(" "))
print(f"O nome tem {len(nome.replace(' ',''))} letras")
primeiro_nome = nome.split(" ")[0]
print(f"O primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras")
