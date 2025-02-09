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

def calcular_determinante(matriz):
    """
    Calcula el determinante de una matriz 3x3.
    
    Args:
        matriz: Una matriz 3x3 representada como una lista de listas.
    
    Returns:
        El determinante de la matriz.
    """
    a11, a12, a13 = matriz[0]
    a21, a22, a23 = matriz[1]
    a31, a32, a33 = matriz[2]
    
    return (
        a11 * (a22 * a33 - a23 * a32) -
        a12 * (a21 * a33 - a23 * a31) +
        a13 * (a21 * a32 - a22 * a31)
    )

def resolver_cramer(matriz_coeficientes, vector_constantes):
    """
    Resuelve un sistema de ecuaciones lineales 3x3 usando la regla de Cramer.
    
    Args:
        matriz_coeficientes: Matriz 3x3 de coeficientes.
        vector_constantes: Vector de términos independientes.
    
    Returns:
        det_A: Determinante principal.
        det_x, det_y, det_z: Determinantes modificados para x, y, z.
        soluciones: Lista con las soluciones [x, y, z].
    """
    # Calcular el determinante principal
    det_A = calcular_determinante(matriz_coeficientes)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante cero).")
    
    # Crear matrices modificadas para calcular det_x, det_y, det_z
    matriz_x = [
        [vector_constantes[0], matriz_coeficientes[0][1], matriz_coeficientes[0][2]],
        [vector_constantes[1], matriz_coeficientes[1][1], matriz_coeficientes[1][2]],
        [vector_constantes[2], matriz_coeficientes[2][1], matriz_coeficientes[2][2]]
    ]
    matriz_y = [
        [matriz_coeficientes[0][0], vector_constantes[0], matriz_coeficientes[0][2]],
        [matriz_coeficientes[1][0], vector_constantes[1], matriz_coeficientes[1][2]],
        [matriz_coeficientes[2][0], vector_constantes[2], matriz_coeficientes[2][2]]
    ]
    matriz_z = [
        [matriz_coeficientes[0][0], matriz_coeficientes[0][1], vector_constantes[0]],
        [matriz_coeficientes[1][0], matriz_coeficientes[1][1], vector_constantes[1]],
        [matriz_coeficientes[2][0], matriz_coeficientes[2][1], vector_constantes[2]]
    ]
    
    # Calcular los determinantes modificados
    det_x = calcular_determinante(matriz_x)
    det_y = calcular_determinante(matriz_y)
    det_z = calcular_determinante(matriz_z)
    
    # Calcular las soluciones
    x = det_x / det_A
    y = det_y / det_A
    z = det_z / det_A
    
    return det_A, det_x, det_y, det_z, [x, y, z]

def resolver_algebra_lineal(matriz_coeficientes, vector_constantes):
    """
    Resuelve un sistema de ecuaciones lineales 3x3 usando álgebra lineal.
    
    Args:
        matriz_coeficientes: Matriz 3x3 de coeficientes.
        vector_constantes: Vector de términos independientes.
    
    Returns:
        det_A: Determinante principal.
        adjunta: Matriz adjunta.
        inversa: Matriz inversa.
        soluciones: Lista con las soluciones [x, y, z].
    """
    # Calcular el determinante principal
    det_A = calcular_determinante(matriz_coeficientes)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única (determinante cero).")
    
    # Calcular la matriz adjunta
    adjunta = [
        [(matriz_coeficientes[1][1] * matriz_coeficientes[2][2] - matriz_coeficientes[1][2] * matriz_coeficientes[2][1]),
         -(matriz_coeficientes[0][1] * matriz_coeficientes[2][2] - matriz_coeficientes[0][2] * matriz_coeficientes[2][1]),
         (matriz_coeficientes[0][1] * matriz_coeficientes[1][2] - matriz_coeficientes[0][2] * matriz_coeficientes[1][1])],
        
        [-(matriz_coeficientes[1][0] * matriz_coeficientes[2][2] - matriz_coeficientes[1][2] * matriz_coeficientes[2][0]),
         (matriz_coeficientes[0][0] * matriz_coeficientes[2][2] - matriz_coeficientes[0][2] * matriz_coeficientes[2][0]),
         -(matriz_coeficientes[0][0] * matriz_coeficientes[1][2] - matriz_coeficientes[0][2] * matriz_coeficientes[1][0])],
        
        [(matriz_coeficientes[1][0] * matriz_coeficientes[2][1] - matriz_coeficientes[1][1] * matriz_coeficientes[2][0]),
         -(matriz_coeficientes[0][0] * matriz_coeficientes[2][1] - matriz_coeficientes[0][1] * matriz_coeficientes[2][0]),
         (matriz_coeficientes[0][0] * matriz_coeficientes[1][1] - matriz_coeficientes[0][1] * matriz_coeficientes[1][0])]
    ]
    
    # Calcular la matriz inversa
    inversa = [[adjunta[i][j] / det_A for j in range(3)] for i in range(3)]
    
    # Calcular las soluciones
    soluciones = [
        sum(inversa[0][j] * vector_constantes[j] for j in range(3)),
        sum(inversa[1][j] * vector_constantes[j] for j in range(3)),
        sum(inversa[2][j] * vector_constantes[j] for j in range(3))
    ]
    
    return det_A, adjunta, inversa, soluciones

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
        # Hacer el elemento principal igual a 1
        elemento_principal = matriz_aumentada[i][i]
        if elemento_principal == 0:
            raise ValueError("El sistema no tiene solución única (elemento principal cero).")
        
        matriz_aumentada[i] = [x / elemento_principal for x in matriz_aumentada[i]]
        pasos.append(f"Paso {len(pasos) + 1}: Dividir fila {i + 1} por {elemento_principal:.2f}")
        
        # Eliminar los elementos debajo/arriba del elemento principal
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