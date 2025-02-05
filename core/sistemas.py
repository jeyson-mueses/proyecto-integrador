def resolver_cramer(matriz_coeficientes: list[list[float]], vector_constantes: list[float]) -> list[float]:
    # Calcular el determinante de la matriz de coeficientes
    det_principal = calcular_determinante(matriz_coeficientes)
    if det_principal == 0:
        raise ValueError("El sistema no tiene solución única.")
    
    soluciones = []
    for i in range(len(matriz_coeficientes)):
        matriz_modificada = [fila[:] for fila in matriz_coeficientes]
        for j in range(len(matriz_modificada)):
            matriz_modificada[j][i] = vector_constantes[j]
        det_modificado = calcular_determinante(matriz_modificada)
        soluciones.append(det_modificado / det_principal)
    
    return soluciones

def calcular_determinante(matriz: list[list[float]]) -> float:
    # Implementar cálculo de determinante recursivo o por cofactores
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(len(matriz)):
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            cofactor = matriz[0][i] * calcular_determinante(submatriz)
            det += (-1)**i * cofactor
        return det