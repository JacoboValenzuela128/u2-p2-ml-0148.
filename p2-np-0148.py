import numpy as np 
# Arath Valenzuela NC:0148 (22/10/26)
# Ejemplos de NumPy, "Numerical Python."

print("------0148----+ Espaciado linealmente en Array +----0148------")
arre = np.linspace(start=0,stop=5,num=5)
print(arre)
print("------0148----+ Matriz de identidad 2D en Array +----0148------")
matriz=np.eye(3)
print(matriz)
print("------0148----+ Genera numeros aleatorios en Array 2D +----0148------")
numale=np.random.random((3,4)) # Genera 12 numeros aleatorios
print(numale)
print("Genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # Genera 9 numeros aleatorios
print(numale)
# Generar 9 numeros totalmente aleatorios comprendidos entre 1 y 20 con NumPy en un arreglo de (3*3).
print("Genera 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)
print("Arath Valenzuela NC:0148")