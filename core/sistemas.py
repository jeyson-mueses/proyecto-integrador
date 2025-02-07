def formatear_numero(valor):
    """
    Formatea un número para mostrarlo sin decimales si es entero.
    
    Args:
        valor: El número a formatear.
    
    Returns:
        Un entero si el número es entero, o un flotante redondeado si no lo es.
    """
    if abs(valor - round(valor)) < 1e-9:  # Verificar si el número es prácticamente entero
        return int(round(valor))
    return round(valor, 2)  # Redondear a 2 decimales si no es entero

def resolver_cramer(matriz_coeficientes, vector_constantes):
    """
    Resuelve un sistema de ecuaciones lineales 3x3 usando la regla de Cramer.
    """
    # Extraer los coeficientes de la matriz 3x3
    a11, a12, a13 = matriz_coeficientes[0]
    a21, a22, a23 = matriz_coeficientes[1]
    a31, a32, a33 = matriz_coeficientes[2]
    
    # Extraer los términos independientes
    b1, b2, b3 = vector_constantes
    
    # Calcular el determinante principal (det_A)
    det_A = (
        a11 * (a22 * a33 - a23 * a32) -
        a12 * (a21 * a33 - a23 * a31) +
        a13 * (a21 * a32 - a22 * a31)
    )
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante cero).")
    
    # Calcular los determinantes para x, y, z
    det_x = (
        b1 * (a22 * a33 - a23 * a32) -
        a12 * (b2 * a33 - a23 * b3) +
        a13 * (b2 * a32 - a22 * b3)
    )
    
    det_y = (
        a11 * (b2 * a33 - a23 * b3) -
        b1 * (a21 * a33 - a23 * a31) +
        a13 * (a21 * b3 - b2 * a31)
    )
    
    det_z = (
        a11 * (a22 * b3 - b2 * a32) -
        a12 * (a21 * b3 - b2 * a31) +
        b1 * (a21 * a32 - a22 * a31)
    )
    
    # Calcular las soluciones
    x = det_x / det_A
    y = det_y / det_A
    z = det_z / det_A
    
    return det_A, det_x, det_y, det_z, [x, y, z]


def resolver_algebra_lineal(matriz_coeficientes, vector_constantes):
    """
    Resuelve un sistema de ecuaciones lineales 3x3 usando álgebra lineal.
    """
    # Extraer los coeficientes de la matriz 3x3
    a11, a12, a13 = matriz_coeficientes[0]
    a21, a22, a23 = matriz_coeficientes[1]
    a31, a32, a33 = matriz_coeficientes[2]
    
    # Extraer los términos independientes
    b1, b2, b3 = vector_constantes
    
    # Calcular el determinante principal (det_A)
    det_A = (
        a11 * (a22 * a33 - a23 * a32) -
        a12 * (a21 * a33 - a23 * a31) +
        a13 * (a21 * a32 - a22 * a31)
    )
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante cero).")
    
    # Calcular la matriz adjunta
    adjunta = [
        [(a22 * a33 - a23 * a32), -(a12 * a33 - a13 * a32), (a12 * a23 - a13 * a22)],
        [-(a21 * a33 - a23 * a31), (a11 * a33 - a13 * a31), -(a11 * a23 - a13 * a21)],
        [(a21 * a32 - a22 * a31), -(a11 * a32 - a12 * a31), (a11 * a22 - a12 * a21)]
    ]
    
    # Calcular la matriz inversa
    inversa = [[adjunta[i][j] / det_A for j in range(3)] for i in range(3)]
    
    # Calcular las soluciones
    x = sum(inversa[0][j] * vector_constantes[j] for j in range(3))
    y = sum(inversa[1][j] * vector_constantes[j] for j in range(3))
    z = sum(inversa[2][j] * vector_constantes[j] for j in range(3))
    
    return det_A, adjunta, inversa, [x, y, z]


def resolver_gauss_jordan(matriz_coeficientes, vector_constantes):
    """
    Resuelve un sistema de ecuaciones lineales 3x3 usando el método de Gauss-Jordan.
    """
    # Crear la matriz aumentada
    matriz_aumentada = [fila + [vector_constantes[i]] for i, fila in enumerate(matriz_coeficientes)]
    
    pasos = []
    n = len(matriz_aumentada)
    
    # Aplicar eliminación gaussiana
    for i in range(n):
        # Hacer el pivote igual a 1
        pivote = matriz_aumentada[i][i]
        if pivote == 0:
            raise ValueError("El sistema no tiene solución única (pivote cero).")
        
        matriz_aumentada[i] = [x / pivote for x in matriz_aumentada[i]]
        pasos.append(f"Paso {len(pasos) + 1}: Dividir fila {i + 1} por {pivote:.2f}")
        
        # Eliminar los elementos debajo/arriba del pivote
        for j in range(n):
            if i != j:
                factor = matriz_aumentada[j][i]
                matriz_aumentada[j] = [matriz_aumentada[j][k] - factor * matriz_aumentada[i][k] for k in range(n + 1)]
                pasos.append(f"Paso {len(pasos) + 1}: F{j + 1} = F{j + 1} - {factor:.2f} * F{i + 1}")
    
    # Extraer las soluciones
    soluciones = [fila[-1] for fila in matriz_aumentada]
    
    # Calcular el determinante
    det_A = 1
    for i in range(n):
        det_A *= matriz_aumentada[i][i]
    
    return pasos, matriz_aumentada, det_A, soluciones