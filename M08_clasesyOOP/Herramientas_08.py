class Herramientas:
    def __init__(self,lista_in):
        self.lista_in = lista_in
    def primo(self):
        for i in (self.lista_in):
            if self.__primo(i):
                print('El número {} es primo'.format(i))
            else:
                print('El número {} no es primo'.format(i))
    def Temperatura(self,partida,llegada):
        for i in self.lista_in:
            print(self.__Temperatura(i,partida,llegada))
    
    def factorial(self):
        for i in self.lista_in:
            print('El facotorial de {} es: {}'.format(i, self.__factorial(i)))

    def __primo(self, num):
        c = True
        for i in range(2, num//2+1):
            if num%i==0:
                c = False
                break
        return c
    def el_mas_repetido(self):
        L = []
        lnr = list(set(self.lista_in))
        for i in lnr:
            L.append(self.lista_in.count(i))
        return lnr[L.index(max(L))], max(L)
    
    def __Temperatura(self, valor, partida, llegada):
        if partida == llegada:
            return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: ' + str(valor)
        else:
            if partida=='C' and llegada=='F':
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: '  + str(valor*9/5 + 32)
            elif partida == 'C' and llegada == 'K':
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: '  + str(valor + 273.15)
            elif partida == 'F' and llegada == 'C':
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: ' + str( (valor-32)*5/9)
            elif partida == 'F' and llegada == 'K':
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: ' + str((valor-32)*5/9 +273.15)
            elif partida == 'K' and llegada == 'C':
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: '  + str(valor-273.15)
            else:
                return str(valor) + ' ' + partida + ' ' + 'en' + ' ' + llegada + ' ' + 'son: ' + str(9*(valor-273.15)/5 + 32)
    def __factorial(self, num):
        if type(num) is not int:
            return 'Se espera un número entero'
        elif num<0:
            return 'Se espera un número positivo'
        else:
            if num>1:
                num = num*self.__factorial(num-1)
            return num

