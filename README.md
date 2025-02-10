# Proyecto Integrador - Análisis Matemático con Python - PUCETEC

## 📌 Descripción
Este proyecto integra Matemáticas, Álgebra y Programación para desarrollar una aplicación que permite:
- Modelar funciones matemáticas (lineales, cuadráticas y cúbicas).
- Calcular propiedades de las funciones (dominio, rango, puntos de corte, monotonía, etc.).
- Resolver sistemas de ecuaciones 3x3 mediante los métodos de Cramer, Gauss-Jordan y Álgebra Lineal.
- Graficar funciones para análisis visual.

## 🛠️ Tecnologías Utilizadas
- **Python** (versión 3.8 o superior)
- **Matplotlib** para generación de gráficos
- **Streamlit** para la interfaz gráfica

## 🚀 Instalación
1. **Clonar el repositorio**
   ```sh
   git clone https://github.com/jeyson-mueses/proyecto-integrador.git
   cd proyecto-integrador
   ```
1.1 **Si usas Windows necesitas ejecutar este comando para que te de permisos para ejecutar el entorno virtual**
   ```
   Set-ExecutionPolicy Restricted -Scope CurrentUser
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**
   ```sh
   python -m venv venv # En Windows
   python3 -m venv venv # En macOs/Linux
   ```
2.2 **Activamos el entorno virtal**
   ```sh
   source venv/bin/activate  # En macOS/Linux
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Ejecución
Para iniciar la aplicación, ejecuta el siguiente comando:
```sh
streamlit run main.py
```
Esto abrirá la interfaz gráfica en tu navegador, donde podrás seleccionar entre modelar funciones o resolver sistemas de ecuaciones.

## 📂 Estructura del Proyecto
```
proyecto_integrador-Julian-Jeyson/
├── app/
│   ├── ui.py                  # Interfaz principal de la aplicación
│   └── __init__.py            # Para que Python reconozca la carpeta como un paquete
├── core/
│   ├── sistemas.py            # Métodos para resolver sistemas de ecuaciones
│   ├── funciones.py           # Funciones para calcular propiedades de funciones
│   └── __init__.py            # Para que Python reconozca la carpeta como un paquete
├── services/
│   ├── graficos.py            # Código para generar gráficas con Matplotlib
│   └── __init__.py            # Para que Python reconozca la carpeta como un paquete
├── main.py                    # Punto de entrada de la aplicación
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## 📖 Uso
### 1️⃣ Modelado de Funciones Matemáticas
- Ingresa coeficientes de la función.
- Se calcularán propiedades como dominio, rango, puntos de corte, etc.
- Se generará la gráfica de la funcion.

### 2️⃣ Resolución de Sistemas de Ecuaciones
- Ingresa los coeficientes de un sistema 3x3.
- Se resolverá utilizando diferentes métodos matemáticos.

## 📌 Autores
- **Jeyson Mueses** 
- **Julìan Solòrzano** 

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de contribuir y mejorar! 🎯

