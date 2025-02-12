def formatear_numero(valor):

    if abs(valor - round(valor)) < 1e-9:  # Verificar si el número es prácticamente entero
        return int(round(valor))
    return round(valor, 2)

def formatear_matriz(matriz):

    return "\n".join([str([formatear_numero(x) for x in fila]) for fila in matriz])


def calcular_determinante(matriz):

    a11, a12, a13 = matriz[0]
    a21, a22, a23 = matriz[1]
    a31, a32, a33 = matriz[2]
    
    return (
        a11 * (a22 * a33 - a23 * a32) -
        a12 * (a21 * a33 - a23 * a31) +
        a13 * (a21 * a32 - a22 * a31)
    )

def resolver_cramer(matriz_coeficientes, vector_constantes):

    # Calcular el determinante principal
    det_A = calcular_determinante(matriz_coeficientes)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única. Puede ser inconsistente o tener infinitas soluciones. (Determinante Cero).")
    
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

    # Calcular el determinante principal
    det_A = calcular_determinante(matriz_coeficientes)
    
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única. Puede ser inconsistente o tener infinitas soluciones. (Determinante Cero).")
    
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
    # Crear la matriz aumentada
    matriz_aumentada = [fila + [vector_constantes[i]] for i, fila in enumerate(matriz_coeficientes)]
    pasos = []
    n = len(matriz_aumentada)
    
    # Contador explícito para los pasos
    paso_numero = 1
    
    # Mostrar la matriz inicial
    pasos.append(f"Paso {paso_numero}: Matriz inicial")
    pasos.append(formatear_matriz(matriz_aumentada))
    paso_numero += 1
    
    # Aplicar eliminación gaussiana
    for i in range(n):
        # Hacer el elemento principal igual a 1
        elemento_principal = matriz_aumentada[i][i]
        if elemento_principal == 0:
            raise ValueError("El sistema no tiene solución única. Puede ser inconsistente o tener infinitas soluciones. (Determinante Cero).")
        
        matriz_aumentada[i] = [x / elemento_principal for x in matriz_aumentada[i]]
        pasos.append(f"Paso {paso_numero}: Dividir fila {i + 1} por {formatear_numero(elemento_principal)}")
        pasos.append(formatear_matriz(matriz_aumentada))
        paso_numero += 1
        
        # Eliminar los elementos debajo/arriba del elemento principal
        for j in range(n):
            if i != j:
                factor = matriz_aumentada[j][i]
                matriz_aumentada[j] = [matriz_aumentada[j][k] - factor * matriz_aumentada[i][k] for k in range(n + 1)]
                pasos.append(f"Paso {paso_numero}: F{j + 1} = F{j + 1} - {formatear_numero(factor)} * F{i + 1}")
                pasos.append(formatear_matriz(matriz_aumentada))
                paso_numero += 1
    
    # Extraer las soluciones
    soluciones = [fila[-1] for fila in matriz_aumentada]
    
    # Calcular el determinante
    det_A = 1
    for i in range(n):
        det_A *= matriz_aumentada[i][i]
    
    return pasos, matriz_aumentada, det_A, soluciones