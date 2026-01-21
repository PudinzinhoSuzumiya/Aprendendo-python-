import random

print('=== JOGO DE ADVINHACAO ===')

numeropensado = random.randint(1,100)
numtentado = 0
tentativas = 0
while numtentado != numeropensado:
    try:
        numtentado = int(input('Digite um número: '))
        tentativas += 1
        if numtentado < 1 or numtentado >100:
            print('Digite um número entre 1 e 100')


        elif numtentado > numeropensado:
            print('Número maior que o pensado!')
        elif numtentado < numeropensado:
            print('Número menor que o pensado!')
    except:
        print('Isso não é um número!')
    

tentativasstr = str(tentativas)
if numtentado == numeropensado:
    print('Parabéns, você acertou em '+ tentativasstr+ ' tentativas!!' )
