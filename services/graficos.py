import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from io import BytesIO

def formatear_numero(valor):
    if abs(valor - round(valor)) < 1e-9:  # Verificar si el número es prácticamente un entero
        return int(round(valor))
    else:
        return f"{valor:.2f}"  # Mantener dos cifras decimales si no es un entero

def graficar_funcion(funcion, tipo_funcion, coeficientes, propiedades):
    plt.figure(figsize=(8, 6))
    x = np.linspace(-10, 10, 500)
    y = [funcion(xi) for xi in x]
    
    plt.plot(x, y, label=f"{tipo_funcion}", color="blue", linewidth=2)
    
    # Mostrar puntos de corte
    corte_y = funcion(0)
    plt.scatter(0, corte_y, color="red", label=f"Punto de corte en Y: (0, {formatear_numero(corte_y)})")
    
    if tipo_funcion == "Lineal":
        x_corte = -coeficientes[1] / coeficientes[0]
        plt.scatter(x_corte, 0, color="green", label=f"Punto de corte en X: ({formatear_numero(x_corte)}, 0)")
    elif tipo_funcion == "Cuadrática":
        a, b, c = coeficientes
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            x1 = (-b + discriminante**0.5) / (2 * a)
            x2 = (-b - discriminante**0.5) / (2 * a)
            plt.scatter(x1, 0, color="green", label=f"Punto de corte en X: ({formatear_numero(x1)}, 0)")
            plt.scatter(x2, 0, color="green")
    
    # Mostrar la ecuación de la función
    if tipo_funcion == "Lineal":
        ecuacion = f"f(x) = {formatear_numero(coeficientes[0])}x + {formatear_numero(coeficientes[1])}"
    elif tipo_funcion == "Cuadrática":
        ecuacion = f"f(x) = {formatear_numero(coeficientes[0])}x² + {formatear_numero(coeficientes[1])}x + {formatear_numero(coeficientes[2])}"
    elif tipo_funcion == "Cúbica":
        ecuacion = f"f(x) = {formatear_numero(coeficientes[0])}x³ + {formatear_numero(coeficientes[1])}x² + {formatear_numero(coeficientes[2])}x + {formatear_numero(coeficientes[3])}"
    plt.title(ecuacion, fontsize=12)
    
    plt.xlabel("Eje x", fontsize=10)
    plt.ylabel("Eje y", fontsize=10)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=10)
    
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close()
    st.image(buf, caption=f"Gráfica de la Función {tipo_funcion}", width=800)