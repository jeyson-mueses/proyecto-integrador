# Proyecto Integrador - Análisis Matemático con Python - PUCETEC

## 📌 Descripción
Este proyecto integra Matemáticas, Álgebra y Programación para desarrollar una aplicación que permite:
- Modelar funciones matemáticas (lineales, cuadráticas y cúbicas).
- Calcular propiedades de las funciones (dominio, rango, puntos de corte, monotonía, etc.).
- Resolver sistemas de ecuaciones 3x3 mediante los métodos de Cramer, Gauss-Jordan y Álgebra Lineal.
- Graficar funciones para análisis visual.
- Exportar resultados en archivos CSV para su posterior análisis.

## 🛠️ Tecnologías Utilizadas
- **Python** (versión 3.8 o superior)
- **Matplotlib** para generación de gráficos
- **Pandas** para manejo y exportación de datos
- **Streamlit** para la interfaz gráfica

## 🚀 Instalación
1. **Clonar el repositorio**
   ```sh
   git clone https://github.com/jeyson-mueses/proyecto-integrador.git
   cd proyecto-integrador
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**
   ```sh
   python -m venv venv
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
proyecto_integrador/
│── main.py              # Punto de entrada del programa
│── funciones.py         # Modelado de funciones matemáticas
│── sistemas.py          # Resolución de sistemas de ecuaciones
│── graficos.py          # Generación de gráficas
│── exportar.py          # Funciones para exportar resultados
│── ui.py                # Interfaz en Streamlit
│── tests.py             # Pruebas unitarias básicas
│── README.md            # Documentación
│── requirements.txt     # Librerías necesarias
```

## 📖 Uso
### 1️⃣ Modelado de Funciones Matemáticas
- Ingresa coeficientes de la función separados por comas.
- Se calcularán propiedades como dominio, rango, puntos de corte, etc.
- Se generará la gráfica de la función.

### 2️⃣ Resolución de Sistemas de Ecuaciones
- Ingresa los coeficientes de un sistema 3x3.
- Se resolverá utilizando diferentes métodos matemáticos.
- Los resultados se podrán exportar en formato CSV.

## 🧪 Pruebas
Para ejecutar pruebas unitarias, usa:
```sh
pytest tests.py
```
Esto validará que los cálculos de sistemas de ecuaciones sean correctos.

## 📌 Autores
- **Jeyson Mueses** -
- **Julìan Solòrzano** -

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de contribuir y mejorar! 🎯

