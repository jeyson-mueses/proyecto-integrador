import streamlit as st

# Inicializar el estado de la aplicación
if 'screen' not in st.session_state:
    st.session_state.screen = "main"  # Estado inicial: pantalla principal

def mostrar_interfaz():
    """Función principal que controla la navegación entre pantallas."""
    if st.session_state.screen == "main":
        mostrar_pantalla_principal()
    elif st.session_state.screen == "funciones":
        mostrar_pantalla_funciones()
    elif st.session_state.screen == "sistemas":
        mostrar_pantalla_sistemas()

def mostrar_pantalla_principal():
    # Centrar el título usando HTML/CSS
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 30px;'>¿Qué quieres resolver hoy?</h1>
    """, unsafe_allow_html=True)
    
    # Contenedor para centrar los botones
    with st.container():
        # Espaciado adicional antes de los botones
        st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
        
        # Dividir la pantalla en tres columnas (una central para los botones)
        col1, col2, col3 = st.columns([1, 2, 1])  # Columnas: izquierda, centro, derecha
        
        with col2:  # Los botones estarán en la columna central
            if st.button("Funciones Matemáticas", key="btn_funciones", help="Resuelve funciones lineales, cuadráticas y cúbicas"):
                st.session_state.screen = "funciones"
            
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)  # Espacio entre botones
            
            if st.button("Sistemas de Ecuaciones", key="btn_sistemas", help="Resuelve sistemas de ecuaciones 3x3"):
                st.session_state.screen = "sistemas"

def mostrar_pantalla_funciones():
    from core.funciones import calcular_propiedades_funcion
    from services.graficos import graficar_funcion
    
    st.header("Modelado de Funciones Matemáticas")
    
    tipo_funcion = st.selectbox("Seleccione el tipo de función", ["Lineal", "Cuadrática", "Cúbica"])
    
    # Entrada de parámetros según el tipo de función
    if tipo_funcion == "Lineal":
        m = st.number_input("Ingrese la pendiente (m)", value=1.0)
        b = st.number_input("Ingrese el intercepto (b)", value=0.0)
        funcion = lambda x: m * x + b
    elif tipo_funcion == "Cuadrática":
        a = st.number_input("Ingrese el coeficiente (a)", value=1.0)
        b = st.number_input("Ingrese el coeficiente (b)", value=0.0)
        c = st.number_input("Ingrese el término independiente (c)", value=0.0)
        funcion = lambda x: a * x**2 + b * x + c
    elif tipo_funcion == "Cúbica":
        a = st.number_input("Ingrese el coeficiente (a)", value=1.0)
        b = st.number_input("Ingrese el coeficiente (b)", value=0.0)
        c = st.number_input("Ingrese el coeficiente (c)", value=0.0)
        d = st.number_input("Ingrese el término independiente (d)", value=0.0)
        funcion = lambda x: a * x**3 + b * x**2 + c * x + d
    
    # Botón para calcular y graficar
    if st.button("Calcular y Graficar"):
        propiedades = calcular_propiedades_funcion(funcion, tipo_funcion)
        st.write("Propiedades:", propiedades)
        graficar_funcion(funcion, tipo_funcion)
    
    # Botón de regreso
    if st.button("Regresar al Menú Principal", key="back_funciones"):
        st.session_state.screen = "main"

def mostrar_pantalla_sistemas():
    from core.sistemas import resolver_cramer
    
    st.header("Resolución de Sistemas de Ecuaciones")
    st.write("Ingresa los coeficientes del sistema de ecuaciones 3x3:")
    
    # Entrada de coeficientes
    st.subheader("Ecuación 1")
    a1 = st.number_input("Coeficiente de x:", key="a1", value=1.0)
    b1 = st.number_input("Coeficiente de y:", key="b1", value=1.0)
    c1 = st.number_input("Coeficiente de z:", key="c1", value=1.0)
    d1 = st.number_input("Término independiente:", key="d1", value=1.0)
    
    st.subheader("Ecuación 2")
    a2 = st.number_input("Coeficiente de x:", key="a2", value=1.0)
    b2 = st.number_input("Coeficiente de y:", key="b2", value=1.0)
    c2 = st.number_input("Coeficiente de z:", key="c2", value=1.0)
    d2 = st.number_input("Término independiente:", key="d2", value=1.0)
    
    st.subheader("Ecuación 3")
    a3 = st.number_input("Coeficiente de x:", key="a3", value=1.0)
    b3 = st.number_input("Coeficiente de y:", key="b3", value=1.0)
    c3 = st.number_input("Coeficiente de z:", key="c3", value=1.0)
    d3 = st.number_input("Término independiente:", key="d3", value=1.0)
    
    # Botón para resolver el sistema
    if st.button("Resolver Sistema"):
        matriz_coeficientes = [
            [a1, b1, c1],
            [a2, b2, c2],
            [a3, b3, c3]
        ]
        vector_constantes = [d1, d2, d3]
        
        try:
            soluciones = resolver_cramer(matriz_coeficientes, vector_constantes)
            st.write("Soluciones:")
            st.write(f"x = {soluciones[0]:.2f}")
            st.write(f"y = {soluciones[1]:.2f}")
            st.write(f"z = {soluciones[2]:.2f}")
        except ValueError as e:
            st.error(str(e))
    
    # Botón de regreso
    if st.button("Regresar al Menú Principal", key="back_sistemas"):
        st.session_state.screen = "main"