#construyendo la clase archivo
class Archivo:
    def __init__(self, nombre):
        try:
            self.f=open(nombre + ".txt",'r+')  #abriendo el archivo con permisos de lectura y escritura
            self.nombre=nombre
        except:
            print("No se puede abrir el archivo", self.nombre)
            exit()
    #metodo que imprime a pantalla el contenido del fichero
    def muestra(self):
        i=1
        for linea in self.f:
            print("{:3}:{}".format(i,linea), end="") #se imprime linea a linea con un formato numerado
            i+=1
        self.f.seek(0)
    #metodo que imprime a pantalla el contenido del fichero en hexadecimal
    def muestraHex(self):
        for linea in self.f:
            print(linea.encode().hex()) #en cada linea se utliza encode().hex() para codificar el contenido a hexadecimal
        self.f.seek(0)
    #metodo que cuenta vocales
    def cuentaVocales(self):
        def vocales(s): #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i].lower() in set("aeiouáéíóú"): #se buscan coincidencias con el conjunto de vocales para aumentar el contador
                    count+=1
            return count
        contador=0
        for linea in self.f: #se suman los múltiples retornos de cada linea para obtener la suma total de vocales
            contador+=vocales(linea)
        self.f.seek(0)
        return contador
    #metodo que cuenta consonantes
    def cuentaConsonantes(self):
        def consonantes(s): #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i].lower() in set("bcdfghjklmnñpqrstvwxyz"): #se buscan coincidencias con el conjunto de consontantes para aumentar el contador
                    count+=1
            return count
        contador=0
        for linea in self.f: #se suman los múltiples retornos de cada linea para obtener la suma total de consonantes
            contador+=consonantes(linea)
        self.f.seek(0)
        return contador
    #metodo que cuenta mayusculas
    def countMayus(self):
        def mayus(s): #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i].isupper(): #se verifica si el caracter es una mayuscula para aumentar el contador en caso afirmativo
                    count +=1
            return count
        contador=0
        for linea in self.f:
            contador+=mayus(linea) #se suman los múltiples retornos de cada linea para obtener la suma total de mayusculas
        self.f.seek(0)
        return contador
    #metodo que cuenta minusculas
    def countMinus(self):
        def minus(s): #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i].islower(): #se verifica si el caracter es una minuscula para aumentar el contador en caso afirmativo
                    count +=1
            return count
        contador=0
        for linea in self.f:
            contador+=minus(linea) #se suman los múltiples retornos de cada linea para obtener la suma total de minusculas
        self.f.seek(0)
        return contador
    #metodo que cuenta lineas
    def countLines(self):
        count=0
        for line in self.f: #únicamente se aumenta el contador linea a linea
            count+=1
        self.f.seek(0)
        return count
    #metodo que cuenta espacios
    def countSpaces(self):
        def spaces(s):  #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i]==" ": #se verifica si el caracter es un espacio para aumentar el contador en caso afirmativo
                    count +=1
            return count
        contador=0
        for linea in self.f:
            contador+=spaces(linea) #se suman los múltiples retornos de cada linea para obtener la suma total de espacios
        self.f.seek(0)
        return contador
    #metodo que cuenta signos
    def cuentaSignos(self):
        def signos(s):  #se llama en cada linea hata terminar de leer
            count=0
            for i in range(len(s)):
                if s[i] in set(',.¿?\'!*-;_@#$%&/()=[{]}"'): #se verifica si el caracter está en el conjunto de simbolos para aumentar el contador en caso afirmativo
                    count+=1
            return count
        contador=0
        for linea in self.f:
            contador+=signos(linea) #se suman los múltiples retornos de cada linea para obtener la suma total de signos
        self.f.seek(0)
        return contador
    #metodo que cuenta palabras
    def countWords(self):
        def words(s):   #se llama en cada linea hata terminar de leer
            count=0
            palabra=False #se utiliza una variable booleana como guía
            for i in range(len(s)):
                if s[i] in set("abcdefghijklmnñopqrstuvwxyzáéíóú"): #si el caracter actual es una letra es porque se está recorriendo una palabra
                    palabra=True #por ello palabra se pone verdadero
                if palabra and s[i]==" ": #si se encuentra un espacio y palabra es verdadero significa que ahí terminó una palabra por lo cualse aumenta el contador
                    count+=1
                    palabra=False #se vuelve a poner palabra en falso para repetir el proceso

                if palabra and i==len(s)-1: #si palabra es verdadero y se está en el último caracter de la cadena se aumenta el contador para no pasar por alto esa última palabra
                    count+=1
                    palabra=False
                
            return count
        contador=0
        for linea in self.f:
            contador+=words(linea)  #se suman los múltiples retornos de cada linea para obtener la suma total de palabras
        self.f.seek(0)
        return contador
    #metodo que copia el archivo en otro
    def copy(self):
        out = open(self.nombre + " - copy.txt", "w") #si el archivo existe se sobreecribe y si no se crea
        for linea in self.f:
            out.write(linea)    #únicamente se copia el contenido linea a linea
        self.f.seek(0)
    #metodo que convierte a mayusculas
    def mayus(self):
        buffer="" #se utiliza una cadena de buffer para almacenar el contenido del archivo
        while True:
            c = self.f.read(1) #se lee caracter a caracter
            if not c: #se rompe el ciclo cuando se llega al EOF
                break
            buffer=buffer+c.upper() #en elbuffer se acumula cada caracter en mayusculas
        self.f.seek(0)
        self.f.write(buffer) #por último se sobreescribe en el fichero original el texto del buffer
        self.f.seek(0)
    #metodo que convierte a minusculas
    def minus(self):
        buffer=""   #se utiliza una cadena de buffer para almacenar el contenido del archivo
        while True:
            c = self.f.read(1)#se lee caracter a caracter
            if not c: #se rompe el ciclo cuando se llega al EOF
                break
            buffer=buffer+c.lower() #en el buffer se acumula cada caracter en minusculas
        self.f.seek(0)
        self.f.write(buffer) #por último se sobreescribe en el fichero original el texto del buffer
        self.f.seek(0)
