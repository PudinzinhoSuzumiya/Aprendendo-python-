usuarios = [
    "joao_123",
    "maria",
    "_pedro",
    "ana.silva",
    "Bruno_",
    "carla99",
    "99lucas",
    "jo"
]

validos = []
invalidos = []

validos = [u for u in usuarios 
           if not u.startswith('_')
           and all(c.isalnum() or c == '_' for c in u)
           and not u[0].isnumeric()       
           and not u[-1] == '_'
           and len(u) >= 5
           and any(c.isalpha() for c in u)
           
           

           
           ]

for u in usuarios:
    if u not in validos:
        invalidos.append(u) 


print('=== VALIDOS ===')
print(f'\n {validos}')

print(f'\n=== INVALIDOS ===')
print(f'\n {invalidos}')