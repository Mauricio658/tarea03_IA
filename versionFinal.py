# Version 3.6.5
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función que calcula la distancia entre un punto y los centroides
def calcular_distancia(punto, centroides, tipo_distancia='media_cuadratica', p=3):

    # Verifica el tipo de distancia especificado y calcula las distancias correspondientes
    if tipo_distancia == '1':
        distancias = np.sum((punto - centroides) ** 2, axis=1)
    elif tipo_distancia == '2':
        distancias = np.sum(np.abs(punto - centroides), axis=1)
    elif tipo_distancia == '3':
        distancias = np.sum(np.abs(punto - centroides) ** p, axis=1) ** (1/p)
    else:

        # Lanza una excepción si el tipo de distancia no es válido
        raise ValueError("Tipo de distancia no válido") 

    # Devuelve las distancias calculadas
    return distancias


# Función para realizar el algoritmo de K-medias
def k_medias(X, k, centroides_iniciales, tipo_distancia, max_iter=100, p=3):
    # Convierte los centroides iniciales en un array NumPy
    centroides = np.array(centroides_iniciales) 

    # Itera hasta alcanzar el número máximo de iteraciones
    for iteracion in range(max_iter):
        # Calcula las asignaciones de cada punto al centroide más cercano
        asignaciones = np.argmin([calcular_distancia(x, centroides, tipo_distancia, p) for x in X], axis=1)

        # Calcula nuevos centroides como la media de los puntos asignados a cada grupo
        nuevos_centroides = np.array([np.mean(X[asignaciones == i], axis=0) for i in range(k)]) 
        print("================================================================================================================")
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Iteración {iteracion + 1}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", end="\n\n")
        print("Asignaciones:", [f'Centroide_{asignacion + 1}' for asignacion in asignaciones])
        print("\nCentroides:")
        for i, c in enumerate(centroides):
            print(f"\tCentroide_{i+1}: {c}")
        # Comprueba si los centroides no han cambiado, en cuyo caso se detiene la iteración
        if np.array_equal(centroides, nuevos_centroides):
            break

        # Actualiza los centroides para la siguiente iteración
        centroides = nuevos_centroides
        # Imprime información sobre la iteración actual
        
    # Devuelve las asignaciones y los centroides finales
    return asignaciones, centroides


# Función para visualizar los resultados del algoritmo
def plot_resultados(X, asignaciones, centroides):
    # Colores para los puntos y los centroides
    colores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    # Configuración del fondo del gráfico como gris
    plt.style.use('ggplot')

    # Grafica cada punto con un color según su asignación al centroide más cercano
    for i in range(len(X)):
        plt.scatter(X[i, 0], X[i, 1], c=colores[asignaciones[i]], marker='o')

    # Grafica cada centroide con un marcador 'x', color y tamaño específicos
    for i in range(len(centroides)):
        plt.scatter(centroides[i, 0], centroides[i, 1], c=colores[i], marker='x', s=200, linewidths=3)

    # Etiquetas y título del gráfico
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('K-medias')

    # Muestra el gráfico
    plt.show()

# Función principal que realiza la interacción con el usuario y ejecuta el algoritmo
def main():
    # Datos de entrada (puntos)
    X = np.array([(0, -2), (-2, 1), (3, 4), (-3, 5), (4, -5), (-3, -2), (7, 2)])  

    # Solicitar al usuario el valor de k (número de clusters)
    k = int(input("Ingrese el valor de k: "))  

    # Solicitar al usuario el número de conjuntos iniciales
    num_iniciales = int(input("Ingrese el número de conjuntos iniciales: ")) 

    # Solicitar al usuario el tipo de distancia a utilizar
    tipo_distancia = input("Ingrese el tipo de distancia \n[1]media_cuadratica\n[2]manhattan\n[3]minkowski\n") 

    # Si se selecciona la distancia de Minkowski, solicitar al usuario el valor de p
    if tipo_distancia == '3':
        p = int(input("Ingrese el valor de p para la distancia de Minkowski: "))
    else:
        p = 3 

    # Inicializar lista para almacenar las coordenadas de los centroides iniciales
    centroides_iniciales = [] 

    # Solicitar al usuario las coordenadas de cada centroide inicial
    for i in range(num_iniciales):
        # Se imprime el número de centroide actual
        print(f"Ingrese las coordenadas del Centroide_{i+1} inicial (separadas por espacios): ")
        centroide = [float(x) for x in input().split()]
        centroides_iniciales.append(centroide)  

    # Ejecutar el algoritmo K-medias y obtener asignaciones y centroides finales
    asignaciones, centroides = k_medias(X, k, centroides_iniciales, tipo_distancia, p) 

    # Mostrar las asignaciones y centroides finales
    # Se imprime la asignación de cada punto junto con el nombre del centroide asignado
    print("\n")
    print("==========================================================================================================================================")
    print("El conjunto de vectores es: ", [f'({x[0]}, {x[1]})' for x in X])
    print("Asignaciones finales:", [f'Centroide_{asig + 1}' for asig in asignaciones])
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    for i in range(len(centroides)):
        print(f'Centroide_{i + 1}_final es {centroides[i]}')
        print("\n")
 
    # Visualizar los resultados mediante la función plot_resultados
    plot_resultados(X, asignaciones, centroides)


# Verifica si el script es el programa principal
if __name__ == "__main__":
    print("-----------------------------Metodo k-medias-----------------------------")
    print("|Instrucciones:                                                          |")
    print("|Puedes elegir entre la distancia media cuadratica,Manhattan o Minskowski|")
    print("|Puedes introducir el valor de K, P y valores iniciales                  |")
    print(" ----------------------------------------------------------------------- ")
    main()
