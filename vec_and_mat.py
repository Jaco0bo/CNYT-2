import numpy as np
import math


def adicion_v(v1, v2):
    """Regresa la suma de
    dos vectores complejos
    (list, list) -> list
    """
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return vec1 + vec2


def inverso_av(v1, v2):
    """Regresa el inverso
    aditivo de dos vectores
    (list, list) -> list
    """
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return vec1 - vec2


def vect_esc(v1, a):
    """Regresa la multiplicacion
    de un vector por un escalar
    (list, num) -> list
    """
    vec1 = np.array(v1)
    return vec1 * a


def adicion_m(matriz1, matriz2):
    """Regresa la suma de
    dos matrices complejas
    (list2D, list2D) -> list2D
    """
    matriz1 = np.array(matriz1)
    matriz2 = np.array(matriz2)
    return matriz1 + matriz2


def resta_m(matriz1, matriz2):
    """Regresa la resta de
    dos matrices complejas
    (list2D, list2D) -> list2D
    """
    matriz1 = np.array(matriz1)
    matriz2 = np.array(matriz2)
    return matriz1 - matriz2


def esc_matco(matriz, x):
    """Regresa la multiplicacion de una
     matriz compleja por un escalar
    (list2D, num) -> list2D
    """
    matriz = np.array(matriz)
    return matriz * x


def transpuesta(a):
    """Regresa la transpuesta
    de una matriz o vector
    (List2D) -> List2D
    """
    r = np.transpose(a)
    return r


def conjugada(a):
    """Regresa la conjugada
    de una matriz o vector
    (list2D) -> list2D
    """
    r = np.conjugate(a)
    return r


def adjunta(a):
    """Devuelve la adjunta
    de una matriz o vector
    (list2D) -> list2D
    """
    r = conjugada(transpuesta(a))
    return r


def prod_cmat(a, b):
    """Multiplica dos matrices complejas
    (list2D,list2D) -> List2D
    """
    multiplicacion = np.dot(a, b)
    return multiplicacion


def accion_mv(matriz, vector):
    """Regresa la accion de una
    matriz sobre un vector complejos
    (list2d, list2D) -> list2D
    """
    accion = np.dot(matriz, vector)
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
    norma = np.round(norma, 2)
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
    resp = np.round(resp, 2)
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


def matriz_u(matriz):
    """verifica si una  matriz
    es matriz unitaria
    (list2D) -> Bool
    """
    matriz1 = np.array(matriz)
    matriz_p = adjunta(matriz1) * matriz1
    matriz_i = np.identity(len(matriz_p))


    if np.allclose(matriz_p, matriz_i, rtol=0.5, atol=0.5):
        return True
    else:
        return False


def matriz_herm(matriz):
    """verifica si una matriz
    compleja es hermitiana
    (list2D) -> Bool
    """
    matriz = np.array(matriz)
    matriz_a = adjunta(matriz)
    if np.array_equal(matriz, matriz_a):
        return True
    else:
        return False


def prd_ten(matriz1, matriz2):
    """Regresa el producto tensor
    de dos matrices o vectores
    (list2D,list2D) -> list2D
    """
    tensor = np.tensordot(matriz1, matriz2, axes=0)
    return tensor




