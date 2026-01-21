alunos = [
    {"nome": "João", "nota": 8.5},
    {"nome": "Maria", "nota": 5.5},
    {"nome": "Pedro", "nota": 3.0},
    {"nome": "Ana", "nota": 7.0},
    {"nome": "Carlos", "nota": 6.0},
    {"nome": "Beatriz", "nota": 9.5},
    {"nome": "Lucas", "nota": 4.5},
    {"nome": "Fernanda", "nota": 7.8},
    {"nome": "Rafael", "nota": 6.5},
    {"nome": "Juliana", "nota": 2.5}
]

aprovados = []
reprovados = []
recuperacao = []

def classificar_alunos(lista):
    for aluno in lista:
        if aluno["nota"] >= 7:
            aprovados.append(aluno)
        elif aluno["nota"] >= 5:
            recuperacao.append(aluno)
        else:
            reprovados.append(aluno)
    print(f"APROVADOS ({len(aprovados)})")
    for aluno in aprovados:
           
        print()
        print(f" {aluno['nome']} ({aluno['nota']})")
    print(f"RECUPERACAO ({len(recuperacao)})")
    for aluno in recuperacao:
            
        print()
        print(f" {aluno['nome']} ({aluno['nota']})")
    print(f"REPROVADOS ({len(reprovados)})")
    for aluno in reprovados:
            
        print()

        print(f" {aluno['nome']} ({aluno['nota']})")


classificar_alunos(alunos)