import csv
class ViajeroFrecuente:
    __Numero = 0
    __DNI = 0
    __Nombre = ''
    __Apellido = ''
    __MillasAcum = 0.0
    
    
    def __init__(self,num,dni,nom,apell,mill):
        self.__Nombre = num
        self.__DNI = dni
        self.__Nombre = nom
        self.__Apellido = apell
        self.__MillasAcum = mill
        
        
    def __eq__(self, mill):
        return self.__MillasAcum == mill
    
    
    def __add__(self,millas):
        return millas + self.__MillasAcum
    
    
    def __sub__(self,canje):
        return canje  - self.__MillasAcum   
    
    
    def numero(self):
        return self.__Numero

    def totalMillas(self):
        return self.__MillasAcum

    def __str__(self):
        return 'Nombre:{}\nApelido:{}\nMillas: {}'.format(self.__Nombre,self.__Apellido,self.__MillasAcum)
        





if __name__ == '__main__':
    
    archivo = open('ViajeroFrecuente')
    reader = csv.reader(archivo,delimet=';')
    
    viajeros = None
    for fila in reader:
        unViajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        viajeros.append(unViajero)
    
    
    archivo.close()
    
    print('--------Viajeros con mas millas---------')
    
    for i in range(len(viajeros)):       
        if viajeros[i] > viajeros[i+1]:
            mill = viajeros[i].totalMillas()
            
    for i in range(len(viajeros)):
        if viajeros[i] == mill:
            print(viajeros[i])
    
    print('---------Acumulara millas-------')
    
    num = int(input('Ingrese el numero del viajero: '))
    ban = False
    i = 0
    while ban == False:
        if viajeros[i].numero() == num:
            ban = True
        else:
            i = i+1
    
    nuevasMillas = float(input('Ingrese la nueva cantidad de millas: '))
    viajeros[i] = nuevasMillas + viajeros[i]
        
    
    print('---------Canjear Millas---------')
    
    num = int(input('Ingrese el numero del viajero: '))
    ban = False
    i = 0
    while ban == False:
        if viajeros[i].numero() == num:
            ban = True
        else:
            i = i+1
            
    canjear = float(input('Ingrese las millas a canjear: '))
    if viajeros[i].totalMillas() >= canjear:
        viajeros[i] = canjear - viajeros[i]
        print('Canje realizado. Nuevas millas: {}'.format(viajeros[i].totalMillas()))
    else:
        print('No se puede canjear')
    
        