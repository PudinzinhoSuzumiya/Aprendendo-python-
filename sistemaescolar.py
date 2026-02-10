import json
import os 



aprovados = []
reprovados = []
def calcular_media(aluno):
    somanotas = sum(aluno['notas'])
    qtd_notas = len(aluno['notas'])
    medianotas = somanotas/qtd_notas
    notasarredondas = round(medianotas, 2)
    return notasarredondas
dados = "dados.json"
def salvar_dados(lista_alunos):
    with open(dados, "w", encoding="utf-8") as arquivo:
        json.dump(lista_alunos, arquivo, indent=4, ensure_ascii=False)
def carregar_dados():
    if os.path.exists(dados):
        with open(dados, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []
alunos = carregar_dados()
def menu():
    print(50*'=')
    print(f"\n Sistema de cadastro de alunos")
    print(50*'=')
    print("1 - Cadastrar aluno ")   
    print("2 - Buscar aluno")
    print("3 - Listar todos os alunos")
    print("4 - Calcular média de aluno")
    print("5 - Calcular média geral da turma")
    print("6 - Relatório de aprovados/reprovados")    
    print("7 - Melhor e pior aluno")    
    print("8 - Editar aluno")
    print("9 - Remover aluno")
    print("0 - Sair")
    print(50*'=')

while True:
    menu()
    opcao = input("\n Escolha uma opção: ")

    if opcao == '1':

        nomea = input('Qual o nome do aluno: ')
        if len(alunos) == 0:
            matriculaa = "2024001"
        else:
            matriculaa = str(int(alunos[-1]['matricula']) + 1)
        
        qtd_notas = input("\n Quantas notas deseja adicionar para este aluno: ")

        notasa = []

        for i in range(int(qtd_notas)):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notasa.append(nota)
                        salvar_dados(alunos)
                        break
                    else:
                        print("Insira um número de 0 a 10")
                except ValueError:
                    print("Digite um número válido")
        alunoadd = {
            "matricula": matriculaa,
            "nome": nomea,
            "notas": notasa
            }
        alunos.append(alunoadd)
        salvar_dados(alunos)
    elif opcao == '2':
        print(50*'=')
        print(f"\nBUSCAR ALUNO")
        print(50*"=")
        print(f"Deseja procurar por: \n Matricula = 1 \n Nome = 2")
        procura = input("Selecione uma opção: ")
        if procura == '1':
            matriculaprocurada = input("Qual a matricula do aluno: ")
            alunoprocurado = [aluno for aluno in alunos if aluno['matricula'] == matriculaprocurada]
            print(alunoprocurado)
        elif procura == '2':
            procuranome =input("Qual o nome do aluno: ")
            alunoprocurado = [aluno for aluno in alunos if procuranome.lower() in aluno['nome'].lower()]
            print(alunoprocurado)
    elif opcao == '3':
        print(50*'=')
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado")
        else:
            for aluno in alunos:
                somanotas = sum(aluno['notas'])
                qtd_notas = len(aluno['notas'])
                medianotas = somanotas/qtd_notas
                notasarredondas = round(medianotas, 2)
                print(f"\nNome: {aluno['nome']}\nMatricula: {aluno['matricula']}\nNotas: {aluno['notas']}\n Média: {notasarredondas}\n {50*'='} ")
    elif opcao == '4':
        print(50*'=')
        mediamatricula = input("Digite a matricula do aluno: ")
        encontrado = False
        for aluno in alunos:
            if aluno['matricula'] == mediamatricula:
                mediaaluno = calcular_media(aluno)
                print(mediaaluno)
                encontrado = True
            
                if mediaaluno >= 7:
                    print("Aprovado!")
                elif mediaaluno < 7:
                    print("Reprovado!")
        if not encontrado:
                print("Aluno não encontrado!")
    elif opcao == '5':
        print(50*'=')
        print('Média geral da turma')
        print(50*'=')
        if len(alunos) >= 1:
            mediaalunos = []
            for aluno in alunos:
                mediaalunos.append(calcular_media(aluno))
                salvar_dados(alunos)
            mediaturma = (sum(mediaalunos) / len(mediaalunos))
            mediaturmaarredondado = round(mediaturma, 2)
            print(f"Media da turma = {mediaturmaarredondado}")
        else:
            print("Nenhum aluno cadastrado na turma")

    elif opcao == '6':
        reprovados.clear()
        aprovados.clear()
        for aluno in alunos:
        
            if (sum(aluno['notas']) / len(aluno['notas'])) >= 7:
                aprovados.append(aluno)
                
            else:
                reprovados.append(aluno)
                
        
        print(50*'=')
        print("APROVADOS")
        print(50*'=')
        print(f"{len(aprovados)} de {len(alunos)}")
        print(f'{round((len(aprovados)/ len(alunos))* 100), 2} %')
        for a in aprovados:
            print(a['nome'])
        
        
        print(50*'=')
        print("REPROVADOS")
        print(50*'=')
        print(f"{len(reprovados)} de {len(alunos)}")
        print(f'{round((len(reprovados)/ len(alunos))* 100), 2} %')
        for r in reprovados:
            print(r['nome'])
        salvar_dados(alunos)
    
    elif opcao == '7':
        if len(alunos) >= 1:
            maiormedia = max(alunos, key=lambda a: sum(a['notas']) / len(a['notas']))
            menormedia = min(alunos, key=lambda aluno: sum(aluno['notas']) / len(aluno['notas']))
            print(f"{50*'='}\nMelhor aluno\n {maiormedia['nome']}\n{maiormedia['matricula']}\n{calcular_media(maiormedia)}\n{50*'='}\n\nPior aluno\n{50*'='}\n{menormedia['nome']}\n{menormedia['matricula']}\n{calcular_media(menormedia)}\n{50*'='}")
        else:
            print("Nenhum aluno cadastrado!")
    elif opcao == '8':
        print(50*'=')
        print('Editar aluno')
        print(50*'=')
        matriculaeditar = input('Qual a matricula do aluno que deseja editar: ')
        encontrado = False
        for i,aluno in enumerate(alunos):
            if aluno['matricula'] == matriculaeditar:
                encontrado = True
                print("\n--- DADOS ATUAIS ---")
                print(f"Matrícula: {aluno['matricula']}")
                print(f"Nome: {aluno['nome']}")
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {calcular_media(aluno)}")
                print("\nO que deseja editar?")
                print("1 - Nome")
                print('2 - Notas')
                print('0 - Cancelar')

                opcao = input("Escolha uma opção ")

                if opcao == '1':
                    novo_nome = input("Qual o nome que deseja colocar: ").strip()
                    if novo_nome:
                        alunos[i]['nome'] = novo_nome
                        print(f"Nome alterado com sucesso para {novo_nome}")
                    else:
                        print("Novo nome não pode ser vazio")
                
                elif opcao == '2':
                    qtd_notas = int(input("Quantas notas deseja cadastrar: "))
                    novas_notas = []
                    for n in range(qtd_notas):
                        while True:
                            try:
                                nota = float(input(f"Nova nota {n+1}: "))
                                if 0 <= nota <= 10:
                                    novas_notas.append(nota)
                                    alunos[i]['notas'] = novas_notas
                                    
                                    break
                                else:
                                    print("Nota deve estar entre 0 e 10!")
                            
                            except ValueError:
                                print("Insira um número válido!")
                    salvar_dados()
                elif opcao == '0':
                    print("Operação cancelada!")
                    break
            if not encontrado:
                print("Aluno não encontrado")
    elif opcao == '9':
        print(50*'=')
        print('REMOVER ALUNO')
        print(50*'=')
        encontrado = False
        remover_matricula = input("Qual a matricula do aluno: ")
        for i,aluno in enumerate(alunos):
            if aluno['matricula'] == remover_matricula:
                encontrado = True
                print(f"Aluno: {aluno['nome']}")
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {calcular_media(aluno)}")
                escolha = input("Tem certeza que deseja remover esse aluno?s/n")
                if escolha == 's':
                    del alunos[i]
                elif escolha == 'n':
                    print("Operação cancelada")
                    break
                else:
                    print("Escolha entre s/n!")
        if encontrado == False:
            print("Matricula não encontrada!")
    elif opcao == '0':
        print("Encerando programa!")
        break
    else:
        print("Insira uma opção válida!")
