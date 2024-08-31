import os

def limpar_tela():
    os.system("cls")

def ler_numero():
    while True:
        try:
            return int(input("informe um valor:"))
        except ValueError:
            print("Insira um numero")
            

def soma(n1, n2):
    try:
        return n1+n2
    except Exception:
        print("Erro durante a soma de dados")


def main():
    limpar_tela()
    n1 = ler_numero()
    n2 = ler_numero()
    print(soma(n1,n2))

main()