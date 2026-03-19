import random

print("ALGORITMO DE BUSQUEDA")
print("=====================")

lista_creada = sorted(random.sample(range(0, 101), 10))
print("Lista generada:", lista_creada)


def mostrar_encontrado(pos, valor):
    print(f"El número {valor} está en la posición {pos}")
    return True


def buscar_numero(numero: int, lista):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2

        if numero == lista[centro]:
            return mostrar_encontrado(centro, lista[centro])

        elif numero > lista[centro]:
            izquierda = centro + 1
        else:
            derecha = centro - 1

    return False


def pedir_opcion():
    opcion = input("¿Deseas buscar un número? (si/no): ").lower()

    if opcion == "si" or opcion == "no":
        return opcion
    else:
        print("Opción inválida. Intenta de nuevo.")
        return pedir_opcion()  


def pedir_numero():
    try:
        numero = int(input("Ingresa un número entre 0 y 100: "))

        if 0 <= numero <= 100:
            return numero
        else:
            print("El número debe estar entre 0 y 100")
            return pedir_numero()

    except ValueError:
        print("Por favor ingresa un número válido")
        return pedir_numero()


def finish():
    opcion = pedir_opcion()

    if opcion == "no":
        print("Programa finalizado")
        return

    numero = pedir_numero()
    encontrado = buscar_numero(numero, lista_creada)

    if not encontrado:
        print("Número no encontrado en la lista")

    finish()  


finish()