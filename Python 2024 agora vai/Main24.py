def soma(*numeros):
    resultado = 0  # Inicializa o resultado como zero
    for num in numeros:
        resultado += num
    return resultado

x = soma (2, 3, 4, 7)  
print (x)  