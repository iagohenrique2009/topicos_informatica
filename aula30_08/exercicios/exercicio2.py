def pares(*valores):
    soma=0
    for valor in valores:
        if(valor % 2==0):
            soma+=1
    return soma

def impares(*valores):
    soma=0
    print("Numeros Impares: ")
    for valor in valores:
        if(valor % 2 >0):
            print(f"{valor}")

def maior(*valores):
    maiorValor = valores[0]
    for valor in valores:
        if valor > valores:
            maiorValor = valor
    return maiorValor

def menorValor(*valores):
    menorValor = valores[0]
    for valor in valores:
        if valor < menorValor:
            menorValor =valor
    return menorValor

def media(*valores):
    soma=0
    somaValores=0
    for valor in valores:
        soma+=1
        somaValores+= valores
    return  somaValores/soma


def inserirValores():
    numeros=()
    while True:
        numeros.append(int(input("Insira os numeros")))
    pares(numeros)

inserirValores()

