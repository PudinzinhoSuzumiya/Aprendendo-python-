produtos = [
    {"nome": "Mouse", "preco": 50.00, "quantidade": 10},
    {"nome": "Teclado", "preco": 120.00, "quantidade": 5},
    {"nome": "Monitor", "preco": 800.00, "quantidade": 3}
    ]
valor_total = 0
encontrado = False
while True:
    print(f"=== SISTEMA DE ESTOQUE === \n 1 - Adicionar produto \n 2 - Listar produtos \n 3 - Buscar produto \n 4 - Atualizar quantidades \n 5 - Remover produtos sem estoque \n 6 - Valor total do estoque \n 0 - Sair")
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        print("ADICIONANDO NOVO PRODUTO")
        nome_pa = input('Qual produto deseja adicionar: ')
        preco_pa = float(input('Qual o preço do produto: '))
        qtd_pa = int(input('Qual a quantidade do produto: '))
        pa = {"nome": nome_pa, "preco": preco_pa, "quantidade": qtd_pa}
        produtos.append(pa)

        
    elif escolha == '0':
        exit()
    
    elif escolha == '2':
        for produto in produtos:
            print(f"PRODUTO -- {produto['nome']} | PREÇO -- {produto['preco']} | QTD -- {produto['quantidade']} \n")
    
    elif escolha == '3':
        pesquisado = input('Qual produto deseja encontrar: ')
        for produto in produtos:
        
            
            if produto['nome'].lower() == pesquisado.lower():
                print(f"Produto encontrado! \n {produto['nome']} -- {produto['preco']} -- {produto['quantidade']}")
                break
            
        if not encontrado:
            print('Produto não encontrado')

    elif escolha == '4':
        nome_upd_qtd = input('Qual produto deseja alterar a quantidade: ').lower()
        upd_qtd = int(input('Qual a nova quantidade: '))
        for produto in produtos:
            
            if produto['nome'].lower() == nome_upd_qtd:
                produto['quantidade'] = upd_qtd
                print('Valor alterado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('Produto não encontrado')    

    elif escolha == '5':
    
        produtos = [p for p in produtos if p['quantidade'] > 0]
        print('Produtos sem estoque removidos!')
    
    elif escolha == '6':

        valor_total = sum(p['preco']*p['quantidade'] for p in produtos)
        print(valor_total)