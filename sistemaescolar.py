alunos = [
    {"matricula": "2024001", "nome": "João Silva", "notas": [7.5, 8.0, 9.0]},
    {"matricula": "2024002", "nome": "Maria Santos", "notas": [6.0, 7.0, 8.5]},
]
aprovados = []
reprovados = []
def calcular_media(aluno):
    somanotas = sum(aluno['notas'])
    qtd_notas = len(aluno['notas'])
    medianotas = somanotas/qtd_notas
    notasarredondas = round(medianotas, 2)
    return(notasarredondas)

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
                    if 0 <= nota or 10 <= nota:
                        notasa.append(nota)
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
            alunoprocurado = [aluno for aluno in alunos if alunoprocurado in aluno['nome']]
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
        for aluno in alunos:
            if aluno['matricula'] == mediamatricula:
                mediaaluno = calcular_media(aluno)
                print(mediaaluno)
            else:
                print("Aluno não encontrado!")
            if mediaaluno >= 7:
                print("Aprovado!")
            elif mediaaluno < 7:
                print("Reprovado!")
        
                
