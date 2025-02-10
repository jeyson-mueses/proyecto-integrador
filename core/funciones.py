from typing import Callable, Dict

def formatear_numero(valor):
    if abs(valor - round(valor)) < 1e-9:  # Verificar si el número es prácticamente un entero
        return int(round(valor))
    else:
        return f"{valor:.2f}"  # Mantener dos cifras decimales si no es un entero

def calcular_propiedades_funcion(funcion: Callable[[float], float], tipo_funcion: str, coeficientes) -> Dict[str, str]:
    propiedades = {}
    
    propiedades["Dominio"] = "(-∞, ∞)"
    if tipo_funcion == "Lineal":
        propiedades["Rango"] = "(-∞, ∞)"
    elif tipo_funcion == "Cuadrática":
        a, b, c = coeficientes
        vertice_x = -b / (2 * a)
        vertice_y = funcion(vertice_x)
        if a > 0:
            propiedades["Rango"] = f"[{formatear_numero(vertice_y)}, ∞)"
        else:
            propiedades["Rango"] = f"(-∞, {formatear_numero(vertice_y)}]"
    elif tipo_funcion == "Cúbica":
        propiedades["Rango"] = "(-∞, ∞)"
    
    # Crecimiento y decrecimiento
    if tipo_funcion == "Lineal":
        a = coeficientes[0]
        if a > 0:
            propiedades["La función es creciente en"] = "(-∞, ∞)"
            propiedades["La función es decreciente en"] = "Ningún intervalo"
        elif a < 0:
            propiedades["La función es decreciente en"] = "(-∞, ∞)"
            propiedades["La función es creciente en"] = "Ningún intervalo"
        else:
            propiedades["La función es constante en"] = "(-∞, ∞)"
    elif tipo_funcion == "Cuadrática":
        a, b, _ = coeficientes
        vertice_x = -b / (2 * a)
        if a > 0:
            propiedades["La función es decreciente en"] = f"(-∞, {formatear_numero(vertice_x)})"
            propiedades["La función es creciente en"] = f"({formatear_numero(vertice_x)}, ∞)"
        else:
            propiedades["La función es creciente en"] = f"(-∞, {formatear_numero(vertice_x)})"
            propiedades["La función es decreciente en"] = f"({formatear_numero(vertice_x)}, ∞)"
    elif tipo_funcion == "Cúbica":
        propiedades["La función es creciente en"] = "(-∞, ∞)"  # Simplificación
    
    # Paridad
    if tipo_funcion == "Lineal":
        a, b = coeficientes
        if b == 0 and a != 0:
            propiedades["Paridad"] = "Impar"
        else:
            propiedades["Paridad"] = "Ni par, ni impar"
    elif tipo_funcion == "Cuadrática":
        a, b, c = coeficientes
        if b == 0:
            propiedades["Paridad"] = "Par"
        else:
            propiedades["Paridad"] = "Ni par, ni impar"
    elif tipo_funcion == "Cúbica":
        a, b, c, d = coeficientes
        if b == 0 and d == 0:
            propiedades["Paridad"] = "Impar"
        else:
            propiedades["Paridad"] = "Ninguna"
    
    # Puntos de corte
    puntos_corte = []
    try:
        corte_y = funcion(0)
        puntos_corte.append(f"Eje Y: (0, {formatear_numero(corte_y)})")
        
        if tipo_funcion == "Lineal":
            x_corte = -coeficientes[1] / coeficientes[0]
            puntos_corte.append(f"Eje X: ({formatear_numero(x_corte)}, 0)")
        elif tipo_funcion == "Cuadrática":
            a, b, c = coeficientes
            discriminante = b**2 - 4 * a * c
            if discriminante > 0:
                x1 = (-b + discriminante**0.5) / (2 * a)
                x2 = (-b - discriminante**0.5) / (2 * a)
                puntos_corte.append(f"Eje X: ({formatear_numero(x1)}, 0), ({formatear_numero(x2)}, 0)")
            elif discriminante == 0:
                x = -b / (2 * a)
                puntos_corte.append(f"Eje X: ({formatear_numero(x)}, 0)")
            else:
                puntos_corte.append("Eje X: No hay cortes reales")
        elif tipo_funcion == "Cúbica":
            puntos_corte.append("Eje X: Cálculo avanzado necesario")
    except Exception as e:
        puntos_corte.append(f"Error al calcular puntos de corte: {str(e)}")
    
    propiedades["Puntos de corte en el eje X"] = puntos_corte[1:]
    propiedades["Puntos de corte en el eje Y"] = puntos_corte[0]
    
    return propiedades

def validar_coeficientes(coeficientes):
    #Valida que los coeficientes sean números válidos
    for coef in coeficientes:
        if not isinstance(coef, (int, float)):
            return False
    return True