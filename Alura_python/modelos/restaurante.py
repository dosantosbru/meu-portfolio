class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_casa = Restaurante()
restaurante_casa.nome = 'Maria'
restaurante_japa = Restaurante()
restaurante_japa.nome = 'Temaki'
restaurante_japa.categoria = 'Japonesa'

restaurantes = [restaurante_casa, restaurante_japa]

print(vars(restaurante_japa))