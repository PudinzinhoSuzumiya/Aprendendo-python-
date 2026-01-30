alunos = [
    {"matricula": "2024001", "nome": "João Silva", "notas": [7.5, 8.0, 9.0]},
    {"matricula": "2024002", "nome": "Maria Santos", "notas": [6.0, 7.0, 8.5]},
]
aprovados = []
reprovados = []


def menu():
    print(50*'=')
    print(f"\n Sistema de cadastro de alunos")
    print(50*'=')
    print("1 - Cadastrar aluno ")   
    print("2 - Listar todos os alunos")
    print("3 - Buscar aluno")
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
        