import streamlit as st
from app.ui import mostrar_interfaz

if __name__ == "__main__":
    st.set_page_config(page_title="Proyecto Integrador", layout="wide")
    mostrar_interfaz()