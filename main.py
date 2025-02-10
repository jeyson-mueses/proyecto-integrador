import streamlit as st

# Configuración inicial de la página (debe ser la PRIMERA llamada)
st.set_page_config(
    page_title="Proyecto Integrador",
    page_icon="📚",  # Ícono de la página
    layout="wide"    # Diseño amplio
)

# Importaciones después de set_page_config
from app.ui import mostrar_interfaz

# Mostrar la interfaz principal
if __name__ == "__main__":
    mostrar_interfaz()