import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(14, 8))
    labels = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], alpha=0.6, color='blue', label='Real Data 1880-2013', s=30 )

    # Create first line of best fit
    new_year = np.array(range(2051))
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_res_all = res.slope*new_year[1880:]+res.intercept
    plt.plot(new_year[1880:], line_res_all, 
         color='red', linewidth=2, label='Linear Fitting 1880-2013')
    # Create second line of best fit
    res_after_2000 = linregress(df['Year'].iloc[120:], df['CSIRO Adjusted Sea Level'].iloc[120:])
    line_res_after_2000 = res_after_2000.slope*new_year[2000:]+res_after_2000.intercept
    plt.plot(new_year[2000:], line_res_after_2000, color='green', linewidth=2, linestyle='--', 
         label='Linear Fitting 2000-2013')
    # Add labels and title
    plt.xlabel('Year', fontsize=12)
    plt.ylabel("Sea Level (inches)", fontsize=12)
    plt.title("Rise in Sea Level", 
          fontsize=14, fontweight='bold')
    plt.xticks(ticks= labels)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    """ Utilice los datos para completar las siguientes tareas:

Utilice Pandas para importar los datos desde epa-sea-level.csv.
Utilice matplotlib para crear un diagrama de dispersión utilizando la Yearcolumna como eje x y la CSIRO Adjusted Sea Levelcolumna como eje y.
Utilice la linregressfunción `from` scipy.statspara obtener la pendiente y la ordenada al origen de la recta de mejor ajuste. Trace la recta de mejor ajuste sobre el diagrama de dispersión. Haga que la recta pase por el año 2050 para predecir el aumento del nivel del mar en 2050.
Trace una nueva línea de mejor ajuste utilizando únicamente los datos desde el año 2000 hasta el año más reciente disponible en el conjunto de datos. Extienda la línea hasta el año 2050 para predecir el aumento del nivel del mar en 2050 si la tasa de aumento continúa como lo ha hecho desde el año 2000.
La etiqueta x debería ser Year, la etiqueta y debería ser Sea Level (inches), y el título debería ser Rise in Sea Level.
"""
