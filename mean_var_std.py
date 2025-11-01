import numpy as np

# La función debe recibir como entrada una lista de 9 dígitos. Debe convertir la lista en un array Numpy de 3x3 y devolver un diccionario con la media, la 
# varianza, la desviación estándar, el máximo, el mínimo y la suma de los valores en ambos ejes y en la matriz aplanada.
""" {
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}"""

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(list).reshape(3,3)
    calculations= {'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), float(array.mean())],
             'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), float(array.var())],
             'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), float(array.std())],
             'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), float(array.max())],
             'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), float(array.min())],
             'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), float(array.sum())] }

    return calculations
print(calculate([0,1,2,3,4,5,6,7,8]))

