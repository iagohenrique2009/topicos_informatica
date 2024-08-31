def continuar():
    while True:
        escolha = str(input("Deseja continuar? S - Sim / N - Não "))
        if escolha == "S" or "s":
            print('Parando a execução')
            break
        else:
            print("continuando...")
    

def inserir_numero(variavel):
    while True:
        try:
            return (float(input(f"Informe o valor para {variavel}: ")))
        except ValueError:
            print("Insira um valor numerico")

def calculoImc(peso,altura):
    try:
        return peso/(altura*altura)
    except ZeroDivisionError:
        print("Valores incorretos, não é possivel dividir por 0")

while True:
    print('Calculo de Imc: ')
    peso = inserir_numero("Peso")
    continuar()
    altura = inserir_numero("Altura")
    continuar()
    imc = calculoImc(peso,altura)
    print(f"Seu IMC é {imc}")


