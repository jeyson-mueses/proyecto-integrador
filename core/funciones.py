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
        propiedades["Rango"] = "[0, ∞)"  # Ajustar según el vértice
    elif tipo_funcion == "Cúbica":
        propiedades["Rango"] = "(-∞, ∞)"
    
    # Monotonía (pendiente positiva o negativa para funciones lineales)
    if tipo_funcion == "Lineal":
        pendiente = funcion(1) - funcion(0)
        if pendiente > 0:
            propiedades["Monotonía"] = "Creciente"
        elif pendiente < 0:
            propiedades["Monotonía"] = "Decreciente"
        else:
            propiedades["Monotonía"] = "Constante"
    
    return propiedades