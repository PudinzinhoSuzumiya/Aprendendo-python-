resposta = 0
def inicia_com_vogal(lista):

    contagem = 0
    for palavra in lista:
        primeira_letra = palavra[0].lower()
        if primeira_letra in 'aeiou':
            contagem += 1
        
        
    return contagem


palavras = ['anel', 'abelha', 'zoiao']

resultado = inicia_com_vogal(palavras)

if resultado != 0:
    print(resultado)
else:
    print('Lista vazia')