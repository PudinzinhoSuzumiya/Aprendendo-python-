import sistema_login
import sistemaescolar

if __name__ == "__main__":
    status = sistema_login.iniciar_sistema_login()
    if status:
        sistemaescolar.iniciar_sistema_escolar()
    elif status is False:
        print("Sessão encerrada.")