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
        if listaObjeto[i]> Vfmaximo:
             Vfmaximo = listaObjeto[i]
    print(Vfmaximo)


    '''for objeto in listaObjeto:
        if numero == objeto.getNumero():
            while opcion!='d':
                print('a- Cant millas')
                print('b- Acum millas')
                print('c- Canjear millas')
                print('d- Mayor entre millas acum')
                print('e- Salir')
                opcion=input('\nIngrese opcion: ')
                
                if opcion=='a':
                    cant1=objeto.cantidadTotaldeMillas()
                    print('Millas A:{}'.format(cant1))
                    
                elif opcion=='b':
                    acum_millas=int(input('Ingrese la cantidad de millas a acumular: '))
                    cant2=objeto.Acummillas(acum_millas)
                    print('Nuevas millas acum B:{}'.format(cant2))
                elif opcion=='c':
                    millas_canjear=int(input('Ingrese millas a canjear: '))
                    cant3=objeto.canjearMillas(millas_canjear)
                    print('Millas totales C:{} '.format(cant3))
                elif opcion=='d':
                    Vfmaximo= listaObjeto[0]
                    i=1
                    for i in range(len(listaObjeto))
                        if listaObjeto[i]> Vfmaximo
                            Vfmaximo = lista[i]
                        print('Valor maximo :{}'.format(Vfmaximo))
                elif opcion=='e':
                      print('¡Good Bye!')
        '''        
        


