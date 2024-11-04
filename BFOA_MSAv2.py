# -*- coding: utf-8 -*-
from bacteria import bacteria
from chemiotaxis import chemiotaxis
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import sys
import visualizacion

def ejecutar_programa():
    print("El programa se ejecuta, por favor espera")

    # Redirigir la salida estándar a un archivo de texto
    sys.stdout = open('D:\\Administracion de Proyectos\\output.txt', 'w')

    poblacion = []

    path = "C:\\Users\\craft\\source\\repos\\BFOA1\\BFOA1\\multifasta.fasta"
    numeroDeBacterias = 5
    numRandomBacteria = 1
    iteraciones = 30
    tumbo = 1
    nado = 3
    chemio = chemiotaxis()
    veryBest = bacteria(path)
    tempBacteria = bacteria(path)
    original = bacteria(path)
    globalNFE = 0

    dAttr = 0.1
    wAttr = 0.2
    hRep = dAttr
    wRep = 10

    # Lista para almacenar los datos de cada iteración
    datos = []

    def clonaBest(veryBest, best):
        veryBest.matrix.seqs = np.array(best.matrix.seqs)
        veryBest.blosumScore = best.blosumScore
        veryBest.fitness = best.fitness
        veryBest.interaction = best.interaction

    def validaSecuencias(path, veryBest):
        tempBacteria.matrix.seqs = np.array(veryBest.matrix.seqs)
        for i in range(len(tempBacteria.matrix.seqs)):
            tempBacteria.matrix.seqs[i] = tempBacteria.matrix.seqs[i].replace("-", "")
        for i in range(len(tempBacteria.matrix.seqs)):
            if tempBacteria.matrix.seqs[i] != original.matrix.seqs[i]:
                print("*****************Secuencias no coinciden********************")
                return

    def tumboNadoYAutoEvalua(bacteria, tumbo):
        bacteria.tumboNado(tumbo)
        bacteria.autoEvalua()

    poblacion = [bacteria(path) for _ in range(numeroDeBacterias)]

    for iteracion in range(iteraciones):
        sys.stdout = sys.__stdout__
        print(f"Iteracion {iteracion + 1} de {iteraciones}")
        sys.stdout = open('D:\\Administracion de Proyectos\\output.txt', 'a')

        with ThreadPoolExecutor() as executor:
            executor.map(lambda b: tumboNadoYAutoEvalua(b, tumbo), poblacion)

        chemio.doChemioTaxis(poblacion, dAttr, wAttr, hRep, wRep)
        globalNFE += chemio.parcialNFE
        best = max(poblacion, key=lambda x: x.fitness)
        if veryBest is None or best.fitness > veryBest.fitness:
            clonaBest(veryBest, best)
        print("interaccion: {}, fitness: {}, NFE: {}".format(veryBest.interaction, veryBest.fitness, globalNFE))

        datos.append([iteracion, veryBest.fitness, globalNFE])

        chemio.eliminarClonar(path, poblacion)
        chemio.insertRamdomBacterias(path, numRandomBacteria, poblacion)
        print("poblacion: {}".format(len(poblacion)))

    veryBest.showGenome()
    validaSecuencias(path, veryBest)

    sys.stdout.close()
    visualizacion.generar_tabla_y_graficas(datos)

ejecutar_programa()
