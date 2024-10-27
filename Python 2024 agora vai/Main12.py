compra_confirmada = True
dados_compra = "Compra no valor de R$300 e entraga confirmada"


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes da compra enviados para seu Email")
        break
else:
    print("Compra não confirmada")
    print("Por favor, realize a compra novamente")

