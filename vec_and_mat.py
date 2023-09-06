import numpy as np
import math


def generar_mat(filas, columnas):
    f = -1
    c = -1
    matriz = []
    for i in range(0, filas):
        col = []
        f += 1
        for j in range(0, columnas):
            c += 1
            valor = (input(f"Ingrese el numero complejo de la posicion {i},{j}: "))
            col.append(valor)
        matriz.append(col)
    return matriz


def matriz_comp(a):
    c = []
    for fila in a:
        fila_compleja = [complex(elemento) for elemento in fila]
        c.append(fila_compleja)
    return c


def mult_cmat(a, b):
    """Multiplica dos matrices complejas
    (list2D,list2D) -> List2D
    """
    multiplicacion = np.dot(a, b)
    return multiplicacion


def accion_mv(a, b):
    """Regresa la accion de una
    matriz sobre un vector complejos
    (list2d, list2D) -> list2D
    """
    accion = np.dot(a, b)
    return accion


def prod_int(a, b):
    """Calcula el producto
    interno de dos vectores
    (list,list) -> complex
    """
    a = np.array(a, dtype=complex)
    b = np.array(b, dtype=complex)

    interno = np.sum(np.conjugate(a) * b)

    return interno


def norma_v(a):
    """Regresa la norma de un
    vector complejo
    (list) -> float
    """
    a = np.array(a, dtype=complex)
    norma = math.sqrt(np.sum(np.conjugate(a) * a))
    return norma


def dist_v(v1, v2):
    """Calcula la distancia
    entre dos vectores
    (list,list) -> float
    """
    v1 = np.array(v1, dtype=complex)
    v2 = np.array(v2, dtype=complex)
    v3 = np.transpose(v1) - v2
    resp = norma_v(v3)
    return resp


def val_and_vec(matriz):
    """Devuelve los valores y vectores
    propios de una matriz compleja
    (list2D) -> list,list
    """
    eigenvalues, eigenvectors = np.linalg.eig(matriz)
    eigenvalues = np.round(eigenvalues, 2)
    eigenvectors = np.round(eigenvectors, 2)
    return eigenvalues, eigenvectors

def adicion_vect(matriz):
    """Realiza la operacion de suma
    de vectores complejos
    (list2D) -> list
    """
    real = int(matriz[0][0]) + int(matriz[1][0])
    img = int(matriz[0][1]) + int(matriz[1][1])
    resp = complex(real, img)
    return resp


def vec_o_mat():
    """pregunta al usuario si quiere
    meter un vector o una matriz 2x2
    (None) -> str
    """
    v_o_m = input("matriz2x2 (m) o vector (v)?: ")
    return v_o_m


def g_matriz():
    """genera dos matrices
     complejas 2x2
     (none) -> list2D,list2D
    """
    i = 1
    matriz1 = []
    matriz2 = []
    while i != 9:
        if i < 5:
            a = input("Vector para primera matriz: ")
            c = a.split(",")
            matriz1.append(c)
            i += 1
        else:
            b = input("Vector para segunda matriz: ")
            d = b.split(",")
            matriz2.append(d)
            i += 1

    return matriz1, matriz2


def imprimir_mat(lista):
    """Imprime una lista con valores
    complejos en forma de matriz
    (list) -> str
    """
    pri_elem = lista[:2]
    ult_elem = lista[2:]
    for num in pri_elem:
        print(f"{num.real}+{num.imag}j", end=" ")
    print()
    for num in ult_elem:
        print(f"{num.real}+{num.imag}j", end=" ")


def inverso_comp(matriz):
    """Devuelve el inverso aditivo
    de un vector complejo
    (list2D) -> list
    """
    real = int(matriz[0][0]) - int(matriz[1][0])
    img = int(matriz[0][1]) - int(matriz[1][1])
    resp = complex(real, img)
    return resp


def esc_comp(n, lista):
    """Multiplica un escalar
    por un vector complejo
    (int,list) -> comp
    """
    real = n * int(lista[0])
    comp = n * int(lista[1])
    resp = complex(real, comp)
    return resp


def adic_matc(matriz1, matriz2):
    """suma 2 matrices complejas 2x2
    y regresa el resultado
    (list2D,list2D) -> list2D
    """
    matriz_suma = []
    elem_1 = complex(int(matriz1[0][0]) + int(matriz2[0][0]),
                     int(matriz1[0][1]) + int(matriz2[0][1]))
    matriz_suma.append(elem_1)
    elem_2 = complex(int(matriz1[1][0]) + int(matriz2[1][0]),
                     int(matriz1[1][1]) + int(matriz2[1][1]))
    matriz_suma.append(elem_2)
    elem_3 = complex(int(matriz1[2][0]) + int(matriz2[2][0]),
                     int(matriz1[2][1]) + int(matriz2[2][1]))
    matriz_suma.append(elem_3)
    elem_4 = complex(int(matriz1[3][0]) + int(matriz2[3][0]),
                     int(matriz1[3][1]) + int(matriz2[3][1]))
    matriz_suma.append(elem_4)

    return matriz_suma


def inv_adic_mat(matriz1, matriz2):
    """Resta 2 matrices complejas 2x2
    y regresa el resultado
    (list2D,list2D) -> list2D
    """
    matriz_res = []
    elem_1 = complex(int(matriz1[0][0]) - int(matriz2[0][0]),
                     int(matriz1[0][1]) - int(matriz2[0][1]))
    matriz_res.append(elem_1)
    elem_2 = complex(int(matriz1[1][0]) - int(matriz2[1][0]),
                     int(matriz1[1][1]) - int(matriz2[1][1]))
    matriz_res.append(elem_2)
    elem_3 = complex(int(matriz1[2][0]) - int(matriz2[2][0]),
                     int(matriz1[2][1]) - int(matriz2[2][1]))
    matriz_res.append(elem_3)
    elem_4 = complex(int(matriz1[3][0]) - int(matriz2[3][0]),
                     int(matriz1[3][1]) - int(matriz2[3][1]))
    matriz_res.append(elem_4)

    return matriz_res


def esc_matc(n, matriz):
    """multiplica un escalar por
    una matriz compleja
    (int,list2D) -> list2D
    """
    c_matriz = []
    elem_1 = complex(n * int(matriz[0][0]), n * int(matriz[0][1]))
    c_matriz.append(elem_1)
    elem_2 = complex(n * int(matriz[1][0]), n * int(matriz[1][1]))
    c_matriz.append(elem_2)
    elem_3 = complex(n * int(matriz[2][0]), n * int(matriz[2][1]))
    c_matriz.append(elem_3)
    elem_4 = complex(n * int(matriz[3][0]), n * int(matriz[3][1]))
    c_matriz.append(elem_4)

    return c_matriz


def trasp():
    """Devuelve la transpuesta
    de un matriz 2x2
    (None) -> list2D
    """
    i = 0
    matriz = []
    while i != 4:
        a = input("numero complejo: ")
        b = a.split(",")
        matriz.append(b)
        i += 1
    elemento = matriz[1][0]
    matriz[1][0] = matriz[2][0]
    matriz[2][0] = elemento
    elemento2 = matriz[1][1]
    matriz[1][1] = matriz[2][1]
    matriz[2][1] = elemento2

    t_matriz = []

    elem_1 = complex(int(matriz[0][0]), int(matriz[0][1]))
    t_matriz.append(elem_1)
    elem_2 = complex(int(matriz[1][0]), int(matriz[1][1]))
    t_matriz.append(elem_2)
    elem_3 = complex(int(matriz[2][0]), int(matriz[2][1]))
    t_matriz.append(elem_3)
    elem_4 = complex(int(matriz[3][0]), int(matriz[3][1]))
    t_matriz.append(elem_4)

    return t_matriz


def conj():
    """devuelve la conjugada de
    una matriz 2x2 compleja
    (None) -> list2D
    """
    i = 0
    matriz = []
    while i != 4:
        a = input("numero complejo: ")
        b = a.split(",")
        matriz.append(b)
        i += 1
    co_matriz = []
    elem_1 = complex(int(matriz[0][0]), int(matriz[0][1]) * -1)
    co_matriz.append(elem_1)
    elem_2 = complex(int(matriz[1][0]), int(matriz[1][1]) * -1)
    co_matriz.append(elem_2)
    elem_3 = complex(int(matriz[2][0]), int(matriz[2][1]) * -1)
    co_matriz.append(elem_3)
    elem_4 = complex(int(matriz[3][0]), int(matriz[3][1]) * -1)
    co_matriz.append(elem_4)

    return co_matriz


def adjunta_c():
    """ Devuelve la adjunta de
    una matriz compleja 2x2
    (None) -> list
    """
    paso1 = trasp()
    paso2 = [numero.real - numero.imag * 1j for numero in paso1]

    return paso2


def main():
    """a = input("Primer vector")
    b = input("segundo vector")
    primer = a.split(",")
    segundo = b.split(",")
    matriz = [primer, segundo]
    resp = adicion_vect(matriz)
    print(resp)
    inv = inverso_comp(matriz)
    print(inv)
    n = int(input("escalar: "))
    mult = esc_comp(n, primer)
    print(mult)
    matriz1, matriz2 = g_matriz()
    print("suma de matrices")
    suma_mat = adic_matc(matriz1, matriz2)
    print()
    imprimir_mat(suma_mat)
    print()
    print("resta de matrices")
    resta_mat = inv_adic_mat(matriz1, matriz2)
    print()
    imprimir_mat(resta_mat)
    print()
    m = int(input("escalar: "))
    print()
    e = esc_matc(m, matriz1)
    print()
    imprimir_mat(e)
    print()
    print("transpuesta")
    print()
    z = vec_o_mat()
    if z == "m":
        transpuesta = trasp()
        imprimir_mat(transpuesta)

    else:
        lista = input("vector complejo: ")
        arreglo = lista.split(",")
        complejo = complex(int(arreglo[0]), int(arreglo[1]))
        print(complejo.real)
        print(f"{complejo.imag}j")

    print()
    print("Conjugada")
    print()
    a = vec_o_mat()
    if a == "m":
        conjugada = conj()
        imprimir_mat(conjugada)

    else:
        lista = input("vector complejo: ")
        arreglo = lista.split(",")
        a = int(arreglo[0])
        b = int(arreglo[1]) * -1
        r = complex(a, b)
        print(r)

    print()
    print("Adjunta")
    print()
    b = vec_o_mat()
    if b == "m":
        m_adjunta = adjunta_c()
        for i in range(2):
            for j in range(2):
                print(m_adjunta[i * 2 + j], end="\t")
            print()

    else:
        lista = input("vector complejo: ")
        arreglo = lista.split(",")
        a = int(arreglo[0])
        b = int(arreglo[1]) * -1
        complejo = complex(a, b)
        print(complejo.real)
        print(f"{complejo.imag}j")

    filas = int(input("Filas primera matriz? "))
    columnas = int(input("columnas primera matriz? "))
    a = generar_mat(filas, columnas)
    matriz1 = matriz_comp(a)
    print()
    print("segunda matriz")
    filas2 = int(input("Filas segunda matriz? "))
    columnas2 = int(input("columnas segunda matriz? "))
    if columnas != filas2:
        print("Estas matrices no se pueden multiplicar")
    else:
        b = generar_mat(filas2, columnas2)
        matriz2 = matriz_comp(b)
        mult = mult_cmat(matriz1, matriz2)
        print(mult)

    print()
    print("matriz")
    filas = int(input("Filas primera matriz? "))
    columnas = int(input("columnas segunda matriz? "))
    a = generar_mat(filas, columnas)
    matriz1 = matriz_comp(a)
    print()
    print("Vector")
    a = generar_mat(columnas, 1)
    vector = matriz_comp(a)
    acc = accion_mv(matriz1, vector)
    print(acc)
    print()
    print("primer vector: ")
    a = input("Componentes del vector1 separados por comas ")
    vect1 = a.split(",")
    b = input("Componentes del vector2 separados por comas ")
    vect2 = b.split(",")
    if len(vect1) != len(vect2):
        print("Error, los vectores no son del mismo tamaño")
    else:
        r = prod_int(vect1, vect2)
        print(r)
    print()
    v = input("Componentes del vector separados por comas: ")
    v1 = v.split(",")
    lo = norma_v(v1)
    print(lo)
    print()
    print("primer vector: ")
    a = input("Componentes del vector1 separados por comas ")
    vect1 = a.split(",")
    b = input("Componentes del vector2 separados por comas ")
    vect2 = b.split(",")
    if len(vect1) != len(vect2):
        print("Error, los vectores no son del mismo tamaño")
    else:
        z = dist_v(vect1, vect2)
        print(z)"""
    print()
    filas = int(input("Filas primera matriz? "))
    columnas = int(input("columnas primera matriz? "))
    a = generar_mat(filas, columnas)
    matriz1 = matriz_comp(a)
    valores, vectores = val_and_vec(matriz1)
    print()
    print("valores propios: ")
    print(valores)
    print()
    print("vectores propios")
    print(vectores)




main()
