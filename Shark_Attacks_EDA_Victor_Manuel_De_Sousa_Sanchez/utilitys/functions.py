# Functions for my EDA
import pandas as pd
import numpy as np
import datetime
import re
import matplotlib.pyplot as plt 
import seaborn as sns

def remove_invalid_date(df, date_column):

    #We try to conver the column
    df[date_column] = pd.to_datetime([date_column], errors='coerce')

    #Filter the rows what the conversion was a succes
    df= df.dropna(subset=[date_column])
    return df


# Definir una función para verificar si una fecha está dentro del rango permitido
def is_valid_date(date_str):
    try:
        # Intentar convertir la fecha usando pd.to_datetime
        date = pd.to_datetime(date_str, errors='raise')
        # Verificar si la fecha está dentro del rango permitido
        if pd.Timestamp.min <= date <= pd.Timestamp.max:
            return True
        else:
            return False
    except:
        return False
    
    
    

#Extractor de numeros para la edad

def extract_first_number(s):
    if pd.isna(s):
        return s
    
    #Find all numbers in the chain
    numbers = re.findall(r'\d+', s)
    
    #Return the first number if exist
    return numbers[0] if numbers else None


def plot_scatter(df, numeric_col1, numeric_col2, category_col=None, size=None, scale=1):
    """
    Dibuja un diagrama de dispersión de una columna numérica contra otra con opciones para color y tamaño de los puntos.

    Args:
        df (pd.DataFrame): El DataFrame que contiene las columnas.
        numeric_col1 (str): Nombre de la primera columna numérica para el eje X.
        numeric_col2 (str): Nombre de la segunda columna numérica para el eje Y.
        category_col (str, optional): Nombre de la columna categórica para el color. Valor por defecto es None.
        size (str or int, optional): Nombre de la columna para el tamaño de los puntos o un valor numérico fijo. Valor por defecto es None.
        scale (float): Escala para el tamaño de los puntos si 'size' es una columna. Valor por defecto es 1.
    """
    # Ajustar el tamaño de los puntos si 'size' es una cadena
    if isinstance(size, str):
        sizes = df[size] * scale
    else:
        sizes = size
    
    # Crear el diagrama de dispersión con o sin columna categórica para el color
    plt.figure(figsize=(10, 6))
    if category_col:
        scatter_plot = sns.scatterplot(data=df, x=numeric_col1, y=numeric_col2, hue=category_col, size=sizes, sizes=(20, 200))
    else:
        scatter_plot = sns.scatterplot(data=df, x=numeric_col1, y=numeric_col2, size=sizes, sizes=(20, 200))
    
    scatter_plot.set_title(f'Diagrama de dispersión de {numeric_col1} vs {numeric_col2}')
    scatter_plot.set_xlabel(numeric_col1)
    scatter_plot.set_ylabel(numeric_col2)
    
    plt.legend()
    plt.tight_layout()
    plt.show()