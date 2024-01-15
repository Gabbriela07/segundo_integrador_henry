# %% [markdown]
# # Funciones 
# 
# Este NOTEBOOK nos ayudará a poder trabajar en el ETL y no estar construyendo las mismas funciones repetitivas.

# %% [markdown]
# ### IMPORTAMOS LIBRERÍAS NECESARIAS

# %%
import pandas as pd
import numpy as np
import re

# %% [markdown]
# ### Funcion de CARGA de los dataset
# 
# Carga de los archvios de excel y devuelve un diccionario de DATAFRAME
# 
# En resumen, esta función simplifica la carga de datos desde un archivo Excel en uno o más DataFrames de Pandas, facilitando el manejo de múltiples hojas en un solo llamado a la función.
# 
#     Parameters:
#     - archivo (str): Ruta del archivo Excel.
#     - hojas (list): Lista de nombres de hojas a cargar.
#     - engine (str, optional): Motor de Excel a utilizar. Por defecto, 'openpyxl'.
# 
#     Returns:
#     dfs: Un diccionario donde las claves son los nombres de las hojas y los valores son DataFrames correspondientes.
# 
#     Example:
#     >>> datos = cargar_datos_desde_excel('archivo.xlsx', ['Hoja1', 'Hoja2'])
#     >>> df_hoja1 = datos['Hoja1']
#     >>> df_hoja2 = datos['Hoja2']
# 

# %%
def carga_datos_excel(archivo, hojas, engine='openpyxl'):
    xls_file = pd.ExcelFile(archivo, engine=engine)
    dfs = {}

    for hoja in hojas:
       df = pd.read_excel(xls_file, hoja)
       dfs[hoja] = df

    return dfs

# %%
def analizar_valores_sd(dataframe):

    columnas_con_sd = dataframe.columns
    resultados = []

    for columna in columnas_con_sd:
        cantidad_sd = dataframe[columna].eq('SD').sum()
        porcentaje_sd = (cantidad_sd / len(dataframe)) * 100
        resultados.append({'Columna': columna, 'Cantidad de SD': cantidad_sd, 'Porcentaje de SD': porcentaje_sd})

    resultados_df = pd.DataFrame(resultados)
    resultados_con_sd = resultados_df[resultados_df['Cantidad de SD'] > 0]

    return resultados_con_sd

# %%
def extraer_coordenadas(texto):
    # Utilizamos una expresión regular para extraer las coordenadas
    coordenadas = re.findall(r'\d+\.\d+', texto)
    if len(coordenadas) == 2:
        return float(coordenadas[0]), float(coordenadas[1])
    else:
        return None, None

# %%