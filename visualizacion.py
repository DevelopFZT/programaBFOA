import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generar_tabla_y_graficas(datos):
    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(datos, columns=['Iteracion', 'Fitness', 'NFE'])

    # Obtener el timestamp actual
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Guardar la tabla en un archivo CSV con el timestamp
    df.to_csv(f'D:\\Administracion de Proyectos\\resultados_{timestamp}.csv', index=False)

    # Generar gráfica de Fitness
    plt.figure(figsize=(10, 5))
    plt.plot(df['Iteracion'], df['Fitness'], marker='o', label='Fitness')
    plt.title('Mejora de Fitness a lo largo de las iteraciones')
    plt.xlabel('Iteracion')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'D:\\Administracion de Proyectos\\fitness_{timestamp}.png')
    plt.show()

    # Generar gráfica de NFE
    plt.figure(figsize=(10, 5))
    plt.plot(df['Iteracion'], df['NFE'], marker='o', label='NFE', color='red')
    plt.title('Mejora de NFE a lo largo de las iteraciones')
    plt.xlabel('Iteracion')
    plt.ylabel('NFE')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'D:\\Administracion de Proyectos\\nfe_{timestamp}.png')
    plt.show()
