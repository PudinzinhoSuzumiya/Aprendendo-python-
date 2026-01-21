import random

print('=== JOGO DE ADVINHACAO ===')

numeropensado = random.randint(1,100)
numtentado = 0
tentativas = 0
while numtentado != numeropensado:
    try:
        numtentado = int(input('Digite um número: '))
        tentativas += 1

        if numtentado > numeropensado:
            print('Número maior que o pensado!')
        elif numtentado < numeropensado:
            print('Número menor que o pensado!')
    except:
        print('Isso não é um número!')
    

tentativasstr = str(tentativas)
if numtentado == numeropensado:
    print('Parabéns, você acertou em '+ tentativasstr+ ' tentativas!!' )
