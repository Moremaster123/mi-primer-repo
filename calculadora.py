# Calculadora sencilla en Python
# Proyecto de práctica EBAC: mi primer repositorio en GitHub


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def main():
    print("=== Calculadora sencilla ===")
    a = float(input("Escribe el primer número: "))
    b = float(input("Escribe el segundo número: "))

    print(f"{a} + {b} = {sumar(a, b)}")
    print(f"{a} - {b} = {restar(a, b)}")
    print(f"{a} x {b} = {multiplicar(a, b)}")
    print(f"{a} / {b} = {dividir(a, b)}")


if __name__ == "__main__":
    main()
