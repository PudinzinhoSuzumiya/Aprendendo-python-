print('Calculadora')
print('opcao 1 = soma')
print('opcao 2 = subtração')
print('opcao 3 = multiplicação')
print('opcao 4 = divisão')

opcao = input('qual opção deseja?: ')

num1 = int(input('qual o primeiro algarismo: '))
num2 = int(input('qual o segundo algarismo: '))

if opcao == '1':
    resposta = num1 + num2
elif opcao == '2':
    resposta = num1 - num2
elif opcao == '3':
    resposta = num1 * num2
elif opcao == '4':
    resposta = num1/num2

respostastr = str(resposta)

print('a resposta é : '+respostastr)