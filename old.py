import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el dominio
def calcular_dominio(tipo_funcion, coeficientes):
    if tipo_funcion == "lineal":
        return "Todos los números reales"
    elif tipo_funcion == "cuadratica":
        return "Todos los números reales"
    elif tipo_funcion == "cubica":
        return "Todos los números reales"
    else:
        return "Función no soportada"

# Función para calcular el rango
def calcular_rango(tipo_funcion, coeficientes):
    if tipo_funcion == "lineal":
        return "Todos los números reales"
    elif tipo_funcion == "cuadratica":
        a = coeficientes[0]
        b = coeficientes[1]
        c = coeficientes[2]
        vertice_y = (4 * a * c - b**2) / (4 * a)
        if a > 0:
            return f"[{vertice_y}, infinito)"
        else:
            return f"(-infinito, {vertice_y}]"
    elif tipo_funcion == "cubica":
        return "Todos los números reales"
    else:
        return "Función no soportada"

# Función para determinar la monotonía
def calcular_monotonia(tipo_funcion, coeficientes):
    if tipo_funcion == "lineal":
        if coeficientes[0] > 0:
            return "Creciente"
        else:
            return "Decreciente"
    elif tipo_funcion == "cuadratica":
        return "Creciente y decreciente dependiendo del vértice"
    elif tipo_funcion == "cubica":
        return "Creciente y decreciente"
    else:
        return "Función no soportada"

# Función para calcular puntos de corte con los ejes
def calcular_puntos_corte(tipo_funcion, coeficientes):
    if tipo_funcion == "lineal":
        x_corte = -coeficientes[1] / coeficientes[0]
        y_corte = coeficientes[1]
        return f"Corte con X: ({x_corte}, 0), Corte con Y: (0, {y_corte})"
    elif tipo_funcion == "cuadratica":
        a, b, c = coeficientes
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            x1 = (-b + sqrt_aproximada(discriminante)) / (2 * a)
            x2 = (-b - sqrt_aproximada(discriminante)) / (2 * a)
            return f"Cortes con X: ({x1}, 0), ({x2}, 0), Corte con Y: (0, {c})"
        else:
            return f"No hay cortes reales con el eje X, Corte con Y: (0, {c})"
    elif tipo_funcion == "cubica":
        return "Cálculo de cortes con X no implementado para funciones cúbicas"
    else:
        return "Función no soportada"

# Función para determinar paridad de la función
def calcular_paridad(tipo_funcion, coeficientes):
    if tipo_funcion == "lineal":
        return "Ninguna (no par ni impar)"
    elif tipo_funcion == "cuadratica":
        if coeficientes[1] == 0:
            return "Par"
        else:
            return "Ninguna (no par ni impar)"
    elif tipo_funcion == "cubica":
        if coeficientes[1] == 0 and coeficientes[3] == 0:
            return "Impar"
        else:
            return "Ninguna (no par ni impar)"
    else:
        return "Función no soportada"

# Implementación de raíz cuadrada manual
def sqrt_aproximada(numero, iteraciones=10):
    aproximacion = numero / 2.0
    for _ in range(iteraciones):
        aproximacion = (aproximacion + numero / aproximacion) / 2.0
    return aproximacion

# Generación manual de valores de x
def generar_valores_x(inicio, fin, pasos):
    x = []
    valor_actual = inicio
    while valor_actual <= fin:
        x.append(valor_actual)
        valor_actual += pasos
    return x

# Función para graficar las funciones manualmente
def graficar_funciones(funciones):
    x = generar_valores_x(-10, 10, 0.1)  # Generar valores de x manualmente
    plt.figure(figsize=(10, 6))

    for funcion in funciones:
        tipo_funcion, coeficientes = funcion
        y = []

        if tipo_funcion == "lineal":
            for valor in x:
                y.append(coeficientes[0] * valor + coeficientes[1])
        elif tipo_funcion == "cuadratica":
            for valor in x:
                y.append(coeficientes[0] * valor**2 + coeficientes[1] * valor + coeficientes[2])
        elif tipo_funcion == "cubica":
            for valor in x:
                y.append(coeficientes[0] * valor**3 + coeficientes[1] * valor**2 + coeficientes[2] * valor + coeficientes[3])
        else:
            print("Función no soportada para graficar")
            continue

        plt.plot(x, y, label=f"{tipo_funcion}")

    plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
    plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
    plt.title("Gráfica de funciones")
    plt.legend()
    plt.grid()
    plt.show()

# Función del Menú Principal
def MenuPrincipal():
    try:
        while True:
            print("///////////////Bienvenido a Proyecto Interdisciplinario///////////////")
            print("Integrantes")
            print(">> Julián Solorzano")
            print(">> Jeyson Mueses")
            print("                                                                                         ")
            print("Programa diseñado para el cálculo de Sistemas de ecuaciones y Modelado de funciones matemáticas")
            print("1. Sistemas de Ecuaciones")
            print("2. Modelado de funciones matemáticas")
            print("3. Salir ")

            opcion = input(">> Ingrese el proceso que desea ejecutar:\n ")

            if opcion == "1":
                print(">> Usted ha seleccionado el proceso Sistemas de Ecuaciones")
                # Aquí puedes agregar la lógica para el cálculo de sistemas de ecuaciones
            elif opcion == "2":
                print(">> Usted ha seleccionado el proceso Modelado de funciones matemáticas")
                
                # Entrada del usuario para el modelado de funciones
                num_funciones = int(input("¿Cuántas funciones desea ingresar (máximo 3)?\n"))
                if num_funciones > 3 or num_funciones < 1:
                    print("Número no válido. Debe ser entre 1 y 3.")
                    continue

                funciones = []
                for i in range(num_funciones):
                    tipo_funcion = input(f"Ingrese el tipo de función {i+1} (lineal, cuadratica, cubica): ").lower()
                    if tipo_funcion == "lineal":
                        coeficientes = [float(input("Coeficiente de x: ")), float(input("Término independiente: "))]  
                    elif tipo_funcion == "cuadratica":
                        coeficientes = [
                            float(input("Coeficiente de x^2: ")),
                            float(input("Coeficiente de x: ")),
                            float(input("Término independiente: "))
                        ]
                    elif tipo_funcion == "cubica":
                        coeficientes = [
                            float(input("Coeficiente de x^3: ")),
                            float(input("Coeficiente de x^2: ")),
                            float(input("Coeficiente de x: ")),
                            float(input("Término independiente: "))
                        ]
                    else:
                        print("Tipo de función no soportado")
                        continue

                    funciones.append((tipo_funcion, coeficientes))

                # Procesar propiedades
                for tipo_funcion, coeficientes in funciones:
                    print(f"\nPropiedades de la función ({tipo_funcion}):")
                    print(f"Dominio: {calcular_dominio(tipo_funcion, coeficientes)}")
                    print(f"Rango: {calcular_rango(tipo_funcion, coeficientes)}")
                    print(f"Monotonía: {calcular_monotonia(tipo_funcion, coeficientes)}")
                    print(f"Puntos de corte: {calcular_puntos_corte(tipo_funcion, coeficientes)}")
                    print(f"Paridad: {calcular_paridad(tipo_funcion, coeficientes)}")

                # Graficar todas las funciones
                graficar_funciones(funciones)
            
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("Opción no válida, por favor ingrese una opción válida.")
                
    except Exception as e:
        print("Hubo un error:", e)

MenuPrincipal()

