import json
import os

dados = "usuarios.json"

def carregar_dados():
    if os.path.exists(dados):
        with open(dados, 'r', encoding='utf-8') as arquivo:
            usuario = json.load(arquivo)
            return usuario
    else:
        return{}
def salvar_dados(usuarios):
    
    with open(dados, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4)
        
usuarios = carregar_dados()



while True:
    print("Sistema de login")
    print("1 - login")
    print("2 - cadastro")
    opcao = input('Escolha')
    if opcao == '1':
        login_input = input("Qual o login")
        senha_input = input("Qual a senha")
        if login_input in usuarios:
            if senha_input == usuarios[login_input]['senha']:
                print("Acesso permitido")
            else:
                print("Senha incorreta")
        else:
            print("Usuário não encontrado")
        
    elif opcao == '2':
        cadastro_usuario = input('Qual usuario deseja cadastrar')
        senha_usuario = input("Qual a senha")
        if cadastro_usuario in usuarios:
            print("Usuario já cadastrado")
            
        else:
            usuarios[cadastro_usuario] = {'senha': senha_usuario}
            salvar_dados(usuarios)