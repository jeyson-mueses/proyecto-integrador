import streamlit as st
import numpy as np
from core.sistemas import resolver_cramer, resolver_algebra_lineal, resolver_gauss_jordan, formatear_numero, formatear_matriz
from core.funciones import calcular_propiedades_funcion, validar_coeficientes
from services.graficos import graficar_funcion

# Función auxiliar para formatear números
def formatear_numero(valor):
    if abs(valor - round(valor)) < 1e-9:  # Verificar si el número es prácticamente un entero
        return int(round(valor))
    else:
        return f"{valor:.2f}" 

# Función auxiliar para formatear matrices
def formatear_matriz(matriz):

    return "\n".join([str([formatear_numero(x) for x in fila]) for fila in matriz])

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
            st.markdown("", unsafe_allow_html=True)
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






def resolver_sistema_con_validacion(matriz_coeficientes, vector_constantes):
    A = np.array(matriz_coeficientes, dtype=float)
    b = np.array(vector_constantes, dtype=float)

    # Calcular el determinante
    det_A = np.linalg.det(A)

    if abs(det_A) < 1e-9:  # Determinante prácticamente cero
        st.warning("La determinante de la matriz es cero. Analizando el sistema...")

        # Calcular el rango de la matriz de coeficientes y la matriz ampliada
        rank_A = np.linalg.matrix_rank(A)
        rank_Ab = np.linalg.matrix_rank(np.column_stack((A, b)))

        if rank_A != rank_Ab:
            st.error("El sistema no tiene solución (las ecuaciones son inconsistentes).")
            return None
        elif rank_A == rank_Ab < A.shape[1]:  # Infinitas soluciones
            st.info("El sistema tiene infinitas soluciones. Calculando soluciones paramétricas...")
            return calcular_soluciones_parametricas(A, b)
        else:
            st.error("Error inesperado al analizar el sistema.")
            return None
    else:
        # Resolver el sistema usando álgebra lineal (método directo)
        soluciones = np.linalg.solve(A, b)
        return soluciones


def calcular_soluciones_parametricas(A, b):
    """
    Calcula las soluciones paramétricas de un sistema con infinitas soluciones.
    """
    from sympy import Matrix, symbols

    # Convertir la matriz a formato sympy
    A_sympy = Matrix(A)
    b_sympy = Matrix(b)

    # Crear una matriz ampliada [A|b]
    matriz_ampliada = A_sympy.row_join(b_sympy)

    # Reducir la matriz a su forma escalonada reducida por filas (RREF)
    rref_matrix, pivot_columns = matriz_ampliada.rref()

    # Identificar las variables libres
    num_variables = A.shape[1]
    variables_libres = [i for i in range(num_variables) if i not in pivot_columns]

    # Crear símbolos para las variables libres
    simbolos = symbols(f'p0:{len(variables_libres)}')

    # Construir las soluciones paramétricas
    soluciones = []
    for i in range(num_variables):
        if i in pivot_columns:
            expr = rref_matrix[i, -1]
            for j, libre in enumerate(variables_libres):
                expr -= rref_matrix[i, libre] * simbolos[j]
            soluciones.append(expr)
        else:
            # Variable libre: asignar el símbolo correspondiente
            idx_libre = variables_libres.index(i)
            soluciones.append(simbolos[idx_libre])

    return soluciones


def mostrar_pantalla_sistemas():
    st.header("Resolución de Sistemas de Ecuaciones")
    st.write("Ingresa los coeficientes del sistema de ecuaciones 3x3:")
    st.latex(r"""
        \begin{aligned}
        a_1x + b_1y + c_1z &= d_1 \\
        a_2x + b_2y + c_2z &= d_2 \\
        a_3x + b_3y + c_3z &= d_3
        \end{aligned}
    """)
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
        matriz_coeficientes.append([a, b, c])
        vector_constantes.append(d)

    # Mostrar la matriz ingresada
    st.subheader("Matriz de Coeficientes")
    for i, fila in enumerate(matriz_coeficientes):
        st.text(f"Ecuación {i + 1}: {[formatear_numero(x) for x in fila]}")
    st.subheader("Vector de Términos Independientes")
    st.text([formatear_numero(x) for x in vector_constantes])

    # Preguntar al usuario qué método desea usar
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
                    st.text(paso)  # Mostrar cada paso y la matriz correspondiente
                st.write("Matriz Resuelta:")
                st.text(formatear_matriz(matriz_resuelta))  # Mostrar la matriz resuelta formateada
                st.write(f"Determinante: {formatear_numero(det_A)}")
                st.write(f"x = {formatear_numero(soluciones[0])}")
                st.write(f"y = {formatear_numero(soluciones[1])}")
                st.write(f"z = {formatear_numero(soluciones[2])}")
        except ValueError as e:
            st.error(str(e).replace("pivote", "elemento principal"))

    # Botón de regreso
    if st.button("Regresar", key="back_button"):
        st.session_state.screen = "main"
