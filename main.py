def get_operation():
    op = input("Digite a operação: ")

    return op


def gether_data():
    n1 = input("Digite o primeiro valor: ")
    n2 = input("Digite o segundo valor: ")
    op = get_operation()
    return n1, n2, op


def main():
    n1,n2,op = gether_data()

    print(eval(n1+op+n2))

    return None

if __name__ == "__main__":
    main()
