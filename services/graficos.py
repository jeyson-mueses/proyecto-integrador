import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from io import BytesIO

def graficar_funcion(funcion, tipo_funcion, coeficientes):
    """
    Genera una gráfica de la función dada y la muestra en un contenedor con tamaño ajustado.
    
    Args:
        funcion: La función matemática a graficar.
        tipo_funcion: El tipo de función ('Lineal', 'Cuadrática', 'Cúbica').
    """
    # Configurar el tamaño de la figura
    plt.figure(figsize=(6, 4))  # Ancho: 6 pulgadas, Alto: 4 pulgadas
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 500)  # 500 puntos entre -10 y 10
    
    # Calcular los valores de y para la función
    y = [funcion(xi) for xi in x]
    
    # Graficar la función
    plt.plot(x, y, label=f"{tipo_funcion}", color="blue", linewidth=2)
    
    # Personalizar la gráfica
    plt.title(f"Gráfica de la Función {tipo_funcion}", fontsize=12)
    plt.xlabel("Eje x", fontsize=10)
    plt.ylabel("Eje y", fontsize=10)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Eje x
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Eje y
    plt.grid(alpha=0.3)  # Cuadrícula ligera
    plt.legend(fontsize=10)
    
    # Guardar la gráfica en un buffer como imagen
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close()  # Cerrar la figura para liberar memoria
    
    # Mostrar la imagen con un tamaño específico
    st.image(buf, caption=f"Gráfica de la Función {tipo_funcion}", width=1000)  # Ancho: 400 píxeles