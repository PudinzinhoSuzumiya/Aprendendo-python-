def palavra_com_mais_consoantes_que_vogal(lista):
    for palavra in lista:
        contador_vogal = 0
        contador_consoantes = 0

        for letra in palavra:
            letratotal = letra.lower()
            if letratotal.isalpha():
                if letratotal in 'aeiou':
                    contador_vogal += 1
                else:
                 contador_consoantes += 1
            
        if contador_consoantes > contador_vogal:
            print(f"'{palavra} tem mais consoantes que vogais (consoantes: {contador_consoantes} vogais: {contador_vogal}) ")
        elif contador_consoantes < contador_vogal:
            print(f"{palavra} tem menos consoantes que vogais (consoantes: {contador_consoantes} do que vogais: {contador_vogal}")
        elif contador_consoantes == contador_vogal:
            print(f"{palavra} tem a mesma quantidade de consoantes que vogais (consoantes: {contador_consoantes} vogais: {contador_vogal}")

palavras = ['Lousa', 'python', 'aeiou', 'bola', 'sim', 'oi', 'transporte', 'João']
palavra_com_mais_consoantes_que_vogal(palavras)