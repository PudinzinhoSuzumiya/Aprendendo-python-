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
        print('adicionado com sucesso!')
    elif escolha == '2':
        if len(lista) == 0:
            print('Nenhuma tarefa')
        
        else:    
            print('\n Sua lista:')
            for i, tarefa in enumerate(lista, 1):
                print(f'{i}. {tarefa}')
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