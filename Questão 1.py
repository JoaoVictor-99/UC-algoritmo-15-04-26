def soma_segura(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Entrada inválida")
        return 0