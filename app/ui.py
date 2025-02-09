import streamlit as st
from core.funciones import calcular_propiedades_funcion, validar_coeficientes
from services.graficos import graficar_funcion
from core.sistemas import resolver_cramer, resolver_algebra_lineal, resolver_gauss_jordan, formatear_numero

# Inicializar el estado de la aplicación
if 'screen' not in st.session_state:
    st.session_state.screen = "main"  # Estado inicial: pantalla principal
if 'num_funciones' not in st.session_state:
    st.session_state.num_funciones = 0  # Número de funciones seleccionadas
if 'funciones_ingresadas' not in st.session_state:
    st.session_state.funciones_ingresadas = []  # Lista para almacenar las funciones

def mostrar_interfaz():
    """Función principal que controla la navegación entre pantallas."""
    if st.session_state.screen == "main":
        mostrar_pantalla_principal()
    elif st.session_state.screen == "funciones":
        mostrar_pantalla_funciones()
    elif st.session_state.screen == "sistemas":
        mostrar_pantalla_sistemas()

def mostrar_pantalla_principal():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 30px;'>¿Qué quieres resolver hoy?</h1>
    """, unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Funciones Matemáticas", key="btn_funciones"):
                st.session_state.screen = "funciones"
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            if st.button("Sistemas de Ecuaciones", key="btn_sistemas"):
                st.session_state.screen = "sistemas"

def mostrar_pantalla_funciones():
    st.header("Modelado de Funciones Matemáticas")
    
    if st.session_state.num_funciones == 0:
        st.write("¿Cuántas funciones quieres ingresar?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("1 Función", key="btn_1_funcion"):
                st.session_state.num_funciones = 1
        with col2:
            if st.button("2 Funciones", key="btn_2_funciones"):
                st.session_state.num_funciones = 2
        with col3:
            if st.button("3 Funciones", key="btn_3_funciones"):
                st.session_state.num_funciones = 3
    else:
        for i in range(st.session_state.num_funciones):
            if i >= len(st.session_state.funciones_ingresadas):
                st.subheader(f"Función {i + 1}")
                tipo_funcion = st.selectbox(
                    f"Selecciona el tipo de función {i + 1}",
                    ["Lineal (ax + b)", "Cuadrática (ax² + bx + c)", "Cúbica (ax³ + bx² + cx + d)"],
                    key=f"tipo_funcion_{i}"
                )
                
                if tipo_funcion == "Lineal (ax + b)":
                    a = st.number_input("Coeficiente a:", value=1.0, key=f"a_lineal_{i}")
                    b = st.number_input("Intercepto b:", value=0.0, key=f"b_lineal_{i}")
                    funcion = lambda x, a=a, b=b: a * x + b
                    coeficientes = (a, b)
                elif tipo_funcion == "Cuadrática (ax² + bx + c)":
                    a = st.number_input("Coeficiente a:", value=1.0, key=f"a_cuadratica_{i}")
                    b = st.number_input("Coeficiente b:", value=0.0, key=f"b_cuadratica_{i}")
                    c = st.number_input("Término independiente c:", value=0.0, key=f"c_cuadratica_{i}")
                    funcion = lambda x, a=a, b=b, c=c: a * x**2 + b * x + c
                    coeficientes = (a, b, c)
                elif tipo_funcion == "Cúbica (ax³ + bx² + cx + d)":
                    a = st.number_input("Coeficiente a:", value=1.0, key=f"a_cubica_{i}")
                    b = st.number_input("Coeficiente b:", value=0.0, key=f"b_cubica_{i}")
                    c = st.number_input("Coeficiente c:", value=0.0, key=f"c_cubica_{i}")
                    d = st.number_input("Término independiente d:", value=0.0, key=f"d_cubica_{i}")
                    funcion = lambda x, a=a, b=b, c=c, d=d: a * x**3 + b * x**2 + c * x + d
                    coeficientes = (a, b, c, d)
                
                if st.button(f"Agregar Función {i + 1}", key=f"agregar_funcion_{i}"):
                    if validar_coeficientes(coeficientes):
                        st.session_state.funciones_ingresadas.append((tipo_funcion.split(" ")[0], funcion, coeficientes))
                        st.success(f"Función {i + 1} agregada correctamente.")
                    else:
                        st.error("Error: Los coeficientes ingresados no son válidos. Por favor, verifica los valores.")
        
        if len(st.session_state.funciones_ingresadas) == st.session_state.num_funciones:
            st.subheader("Funciones Ingresadas:")
            for idx, (tipo_funcion, _, _) in enumerate(st.session_state.funciones_ingresadas):
                st.write(f"{idx + 1}. {tipo_funcion}")
            
            if st.button("Calcular y Graficar"):
                for idx, (tipo_funcion, funcion, coeficientes) in enumerate(st.session_state.funciones_ingresadas):
                    st.write(f"Propiedades de la Función {idx + 1}:")
                    propiedades = calcular_propiedades_funcion(funcion, tipo_funcion, coeficientes)
                    for propiedad, valor in propiedades.items():
                        st.write(f"{propiedad}: {valor}")
                    try:
                        graficar_funcion(funcion, tipo_funcion, coeficientes, propiedades)
                    except Exception as e:
                        st.error(f"Error al graficar la función {idx + 1}: {str(e)}")
    
    if st.button("Regresar", key="back_button"):
        st.session_state.screen = "main"
        st.session_state.num_funciones = 0
        st.session_state.funciones_ingresadas = []

def mostrar_pantalla_sistemas():
    st.header("Resolución de Sistemas de Ecuaciones")
    # Paso 1: Entrada de coeficientes del sistema 3x3
    st.write("Ingresa los coeficientes del sistema de ecuaciones 3x3:")
    # Crear una matriz vacía para los coeficientes
    matriz_coeficientes = []
    vector_constantes = []
    for i in range(3):
        st.subheader(f"Ecuación {i + 1}")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.number_input(f"Coeficiente de x (Ecuación {i + 1})", value=1.0, key=f"a_{i}")
        with col2:
            b = st.number_input(f"Coeficiente de y (Ecuación {i + 1})", value=1.0, key=f"b_{i}")
        with col3:
            c = st.number_input(f"Coeficiente de z (Ecuación {i + 1})", value=1.0, key=f"c_{i}")
        with col4:
            d = st.number_input(f"Término independiente (Ecuación {i + 1})", value=1.0, key=f"d_{i}")
        # Agregar los coeficientes a la matriz y el vector
        matriz_coeficientes.append([a, b, c])
        vector_constantes.append(d)
    
    # Mostrar la matriz ingresada
    st.subheader("Matriz de Coeficientes")
    for i, fila in enumerate(matriz_coeficientes):
        st.text(f"Ecuación {i + 1}: {[formatear_numero(x) for x in fila]}")
    st.subheader("Vector de Términos Independientes")
    st.text([formatear_numero(x) for x in vector_constantes])
    
    # Paso 2: Preguntar al usuario qué método desea usar
    metodo = st.selectbox(
        "Selecciona el método de resolución:",
        ["Método de Cramer", "Álgebra Lineal", "Gauss-Jordan"]
    )
    
    # Botón para resolver el sistema
    if st.button("Resolver Sistema"):
        try:
            if metodo == "Método de Cramer":
                det_A, det_x, det_y, det_z, soluciones = resolver_cramer(matriz_coeficientes, vector_constantes)
                st.subheader("Resultados (Método de Cramer):")
                st.write(f"Determinante General (det_A): {formatear_numero(det_A)}")
                st.write(f"Determinante Modificada (det_x): {formatear_numero(det_x)}")
                st.write(f"Determinante Modificada (det_y): {formatear_numero(det_y)}")
                st.write(f"Determinante Modificada (det_z): {formatear_numero(det_z)}")
                st.write(f"x = {formatear_numero(soluciones[0])}")
                st.write(f"y = {formatear_numero(soluciones[1])}")
                st.write(f"z = {formatear_numero(soluciones[2])}")
            elif metodo == "Álgebra Lineal":
                det_A, adjunta, inversa, soluciones = resolver_algebra_lineal(matriz_coeficientes, vector_constantes)
                st.subheader("Resultados (Álgebra Lineal):")
                st.write(f"Determinante: {formatear_numero(det_A)}")
                st.write("Matriz Adjunta:")
                for fila in adjunta:
                    st.text([formatear_numero(x) for x in fila])
                st.write("Matriz Inversa:")
                for fila in inversa:
                    st.text([formatear_numero(x) for x in fila])
                st.write(f"x = {formatear_numero(soluciones[0])}")
                st.write(f"y = {formatear_numero(soluciones[1])}")
                st.write(f"z = {formatear_numero(soluciones[2])}")
            elif metodo == "Gauss-Jordan":
                pasos, matriz_resuelta, det_A, soluciones = resolver_gauss_jordan(matriz_coeficientes, vector_constantes)
                st.subheader("Resultados (Gauss-Jordan):")
                st.write("Pasos para convertir la matriz a forma escalonada:")
                for paso in pasos:
                    st.text(paso)
                st.write("Matriz Resuelta:")
                for fila in matriz_resuelta:
                    st.text([formatear_numero(x) for x in fila])
                st.write(f"Determinante: {formatear_numero(det_A)}")
                st.write(f"x = {formatear_numero(soluciones[0])}")
                st.write(f"y = {formatear_numero(soluciones[1])}")
                st.write(f"z = {formatear_numero(soluciones[2])}")
        except ValueError as e:
            st.error(str(e).replace("pivote", "elemento principal"))  # Reemplazar "pivote" en mensajes de error
    
    # Botón de regreso
    if st.button("Regresar", key="back_button"):
        st.session_state.screen = "main"