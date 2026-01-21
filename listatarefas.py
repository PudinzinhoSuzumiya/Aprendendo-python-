print ('=== LISTA DE TAREFAS ===')


lista = []

while True:
    print('\n--- MENU ---')
    print('1 - adicionar nova tarefa')
    print('2 - ver tarefas')
    print('3 - remover tarefa')
    print('4 - sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1': 
        adicao = input('O que você quer adicionar: ')
        lista.append(adicao)
    elif escolha == '2':
        print(lista)
    elif escolha == '3':
        remover = input('O que você quer remover: ')
        if remover in lista:
            lista.remove(remover)
        else:
            print('ERRO, item não presente na lista')
    elif escolha == '4':
        exit()
    else:
        print('Opção inválida!!')