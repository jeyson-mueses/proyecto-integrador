import pandas as pd

def exportar_a_csv(datos: dict, nombre_archivo: str):
    df = pd.DataFrame(datos)
    df.to_csv(nombre_archivo, index=False)