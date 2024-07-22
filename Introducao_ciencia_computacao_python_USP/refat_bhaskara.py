import math


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, insira um valor numérico.")


def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c


def calcular_raizes(a, b, delta):
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x1 = -b / (2 * a)
        return x1,
    else:
        return None


def imprimir_raizes(raizes):
    if raizes is None:
        print("A equação não possui raízes reais.")
    elif len(raizes) == 1:
        print(f"A única raiz é: {raizes[0]}")
    else:
        print(f"As raízes são: {raizes[0]} e {raizes[1]}")


def main():
    a = get_float_input("Digite o valor de a: ")
    b = get_float_input("Digite o valor de b: ")
    c = get_float_input("Digite o valor de c: ")

    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, delta)
    imprimir_raizes(raizes)


if __name__ == "__main__":
    main()
