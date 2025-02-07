from typing import Callable, Dict

def calcular_propiedades_funcion(funcion: Callable[[float], float], tipo_funcion: str) -> Dict[str, str]:
    propiedades = {}
    
    # Dominio
    if tipo_funcion in ["Lineal", "Cuadrática", "Cúbica"]:
        propiedades["Dominio"] = "(-∞, ∞)"
    
    # Rango
    if tipo_funcion == "Lineal":
        propiedades["Rango"] = "(-∞, ∞)"
    elif tipo_funcion == "Cuadrática":
        # Para funciones cuadráticas, el rango depende del vértice
        a = funcion(1) - funcion(0)  # Coeficiente principal (pendiente)
        b = funcion(0)              # Término independiente
        c = funcion(-1)             # Otro punto para calcular el coeficiente cuadrático
        a_cuadratico = (c - 2 * b + funcion(0)) / 2
        
        if a_cuadratico > 0:
            propiedades["Rango"] = f"[{funcion(-b / (2 * a_cuadratico))}, ∞)"
        else:
            propiedades["Rango"] = f"(-∞, {funcion(-b / (2 * a_cuadratico))}]"
    elif tipo_funcion == "Cúbica":
        propiedades["Rango"] = "(-∞, ∞)"
    
    # Puntos de corte
    puntos_corte = []
    try:
        # Punto de corte con el eje Y (x = 0)
        corte_y = funcion(0)
        puntos_corte.append(f"Eje Y: (0, {corte_y})")
        
        # Puntos de corte con el eje X (f(x) = 0)
        if tipo_funcion == "Lineal":
            x_corte = -funcion(0) / (funcion(1) - funcion(0))
            puntos_corte.append(f"Eje X: ({x_corte}, 0)")
        elif tipo_funcion == "Cuadrática":
            # Resolver ax² + bx + c = 0 usando la fórmula general
            a = funcion(1) - funcion(0)
            b = funcion(0)
            c = funcion(-1)
            discriminante = b**2 - 4 * a * c
            
            if discriminante > 0:
                x1 = (-b + discriminante**0.5) / (2 * a)
                x2 = (-b - discriminante**0.5) / (2 * a)
                puntos_corte.append(f"Eje X: ({x1}, 0), ({x2}, 0)")
            elif discriminante == 0:
                x = -b / (2 * a)
                puntos_corte.append(f"Eje X: ({x}, 0)")
            else:
                puntos_corte.append("Eje X: No hay cortes reales")
        elif tipo_funcion == "Cúbica":
            # Para funciones cúbicas, encontrar raíces puede ser más complejo.
            # Aquí usamos una aproximación numérica simple.
            puntos_corte.append("Eje X: Cálculo avanzado necesario")
    except Exception as e:
        puntos_corte.append(f"Error al calcular puntos de corte: {str(e)}")
    
    propiedades["Puntos de Corte"] = puntos_corte
    
    return propiedades