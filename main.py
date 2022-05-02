from ViajeroFecuente import Viajero
import csv

if __name__ == '__main__':
    listaObjeto=[]
    archivo=open('persona.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        objeto=Viajero(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
        listaObjeto.append(objeto)
    #numero=int(input('Ingrese numero de VP : '))
    #opcion = None
    #valor0=0

    Vfmaximo= listaObjeto[0]
    i=1
    for i in range(len(listaObjeto)):
        if listaObjeto[i] > Vfmaximo:
             Vfmaximo = listaObjeto[i]
             
             
    print('Valor {}'.format(Vfmaximo.getNombre()))