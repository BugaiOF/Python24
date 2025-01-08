cores = [ 'amarelo', 'verde', 'azul', 'vermelho' ]

cor_client = input ('Digite a cor desejada : ')

if cor_client.lower() in cores:
    print(' existe no estoque')
else:
    print(' não existe no estoque')