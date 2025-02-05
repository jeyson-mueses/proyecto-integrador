from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def graficar_funcion(funcion: Callable[[float], float], tipo_funcion: str):
    x = np.linspace(-10, 10, 500)
    y = funcion(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"Función {tipo_funcion}")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)