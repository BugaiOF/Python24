import datetime

ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = datetime.datetime.now().year

idade = (ano_atual - ano_nascimento)


print(f"Você tem {idade} anos.")