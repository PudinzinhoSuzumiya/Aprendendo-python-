cpfs = ["12345678900", "111.222.333-44", "98765432100"]

cpfformatado = []
for cpf in cpfs:
    apenas_numeros = cpf.replace('.', '').replace('-','')
    formatado = f"{apenas_numeros[:3]}.{apenas_numeros[3:6]}.{apenas_numeros[6:9]}-{apenas_numeros[9:]}"

    cpfformatado.append(formatado)

print(cpfformatado)