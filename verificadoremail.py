contatos = [
    "joao@email.com",
    "maria.silva",
    "pedro@site.com.br",
    "@invalido.com",
    "ana@teste"
]

validos = []
invalidos = []



validos = [e for e in contatos 
           if any(c == '@' for c in e) 
           and any(c == '.' for c in e )
           and not e.startswith('@')
           and '.' in e.split('@')[-1]
           
           
           
           ]

print(validos)
