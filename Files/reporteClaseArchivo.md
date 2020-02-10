# Clase Archivo
##### Alejandro Escalante Hernandez
### Programa principal:
Este programa crea una instancia de la clase archivo y llama a todos sus métodos para comprobar la funcionalidad de estos
```sh
from arch import Archivo
#main
nomb=input("Nombre del archivo sin extensión: ") #se pide el nombre sin extensión pero este programa utiliza archivos txt
archi=Archivo(nomb) #se instancia objeto de la clase Archivo
#se comienza a llamar a métodos de la clase
archi.muestra()
print("\n El archivo tiene: "+str(archi.cuentaVocales())+" vocales")
print("\n El archivo tiene: "+str(archi.cuentaConsonantes())+" consonantes")
print("\n El archivo tiene: "+str(archi.countLines())+" lineas")
print("\n El archivo tiene: "+str(archi.countMinus())+" minusculas")
print("\n El archivo tiene: "+str(archi.countMayus())+" mayusculas")
print("\n El archivo tiene: "+str(archi.countSpaces())+" espacios")
print("\n El archivo tiene: "+str(archi.cuentaSignos())+" signos")
print("\n El archivo tiene: "+str(archi.countWords())+" palabras")
archi.copy()
print("El archivo se ha copiado")
archi.mayus()
print("El contenido del archivo se ha convertido a mayusculas")
archi.minus()
print("El contenido del archivo se ha convertido a minusculas")
print("El archivo en hexadecimal es: ")
archi.muestraHex()
```
### Clase Archivo:
Los métodos de esta clase son muy similares entre sí sobre todo aquellos que se encargan de contar ciertos elementos en el archivo, la manera en la que funciona es analizar linea por linea y por último hacer una suma para obtener el total.
```sh
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
```
### Funcionamiento
Con el fin de evaluar el funcionamiento del programa se presenta la siguiente prueba:
El texto a analizar es:
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vehicula a mauris eget euismod. Morbi vulputate et est commodo pretium. Vestibulum consequat dui tortor, quis pharetra ex pellentesque quis. Nam varius, enim eget pharetra tempor, lacus quam dapibus lectus, ac molestie purus lacus non lacus. Duis id velit congue, tempor nunc non, sagittis sapien. Praesent maximus purus id aliquam faucibus. In faucibus eu nibh ac gravida. Phasellus ac ligula nisl. Vivamus eget consequat erat, vitae euismod nisi. Pellentesque a neque mollis, vulputate tellus eget, aliquam elit. Praesent in ex libero. Curabitur sit amet purus urna.

Vestibulum sodales sodales nibh vitae imperdiet. Vestibulum sit amet efficitur leo, ac molestie nisl. Donec at hendrerit augue. Aliquam et ultrices ex. Praesent rutrum massa nulla, eu bibendum arcu suscipit sit amet. Nulla rutrum lectus eu libero mollis tempus. Etiam sed dolor accumsan, vulputate ipsum vel, tristique enim. Ut eleifend, magna vitae facilisis suscipit, odio libero dignissim enim, ac bibendum sapien lectus id tortor.
```
Además de la creación del fichero copia y la modificacion del original, la salida del programa fue:
```
1:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vehicula a mauris eget euismod. Morbi vulputate et est commodo pretium. Vestibulum consequat dui tortor, quis pharetra ex pellentesque quis. Nam varius, enim eget pharetra tempor, lacus quam dapibus lectus, ac molestie purus lacus non lacus. 
Duis id velit congue, tempor nunc non, sagittis sapien. Praesent maximus purus id aliquam faucibus. In faucibus eu nibh ac gravida. Phasellus ac ligula nisl. Vivamus eget consequat erat, vitae euismod nisi. Pellentesque a neque mollis, vulputate tellus eget, aliquam elit. Praesent in ex libero. Curabitur sit 
amet purus urna.
  2:
  3:Vestibulum sodales sodales nibh vitae imperdiet. Vestibulum sit amet efficitur leo, ac molestie nisl. Donec at hendrerit augue. Aliquam et ultrices ex. Praesent rutrum massa nulla, eu bibendum arcu suscipit sit amet. Nulla rutrum lectus eu libero mollis tempus. Etiam sed dolor accumsan, vulputate ipsum vel, tristique enim. Ut eleifend, magna vitae facilisis suscipit, odio libero dignissim enim, ac bibendum sapien lectus id tortor.
 El archivo tiene: 383 vocales

 El archivo tiene: 488 consonantes

 El archivo tiene: 3 lineas

 El archivo tiene: 850 minusculas

 El archivo tiene: 21 mayusculas

 El archivo tiene: 157 espacios

 El archivo tiene: 38 signos

 El archivo tiene: 159 palabras
El archivo se ha copiado
El contenido del archivo se ha convertido a mayusculas
El contenido del archivo se ha convertido a minusculas
El archivo en hexadecimal es:
6c6f72656d20697073756d20646f6c6f722073697420616d65742c20636f6e73656374657475722061646970697363696e6720656c69742e206d6175726973207665686963756c612061206d6175726973206567657420657569736d6f642e206d6f7262692076756c7075746174652065742065737420636f6d6d6f646f207072657469756d2e20766573746962756c756d20636f6e7365717561742064756920746f72746f722c20717569732070686172657472612065782070656c6c656e74657371756520717569732e206e616d207661726975732c20656e696d20656765742070686172657472612074656d706f722c206c61637573207175616d2064617069627573206c65637475732c206163206d6f6c6573746965207075727573206c61637573206e6f6e206c616375732e20647569732069642076656c697420636f6e6775652c2074656d706f72206e756e63206e6f6e2c2073616769747469732073617069656e2e207072616573656e74206d6178696d757320707572757320696420616c697175616d2066617563696275732e20696e206661756369627573206575206e69626820616320677261766964612e2070686173656c6c7573206163206c6967756c61206e69736c2e20766976616d7573206567657420636f6e73657175617420657261742c20766974616520657569736d6f64206e6973692e2070656c6c656e7465737175652061206e65717565206d6f6c6c69732c2076756c7075746174652074656c6c757320656765742c20616c697175616d20656c69742e207072616573656e7420696e206578206c696265726f2e206375726162697475722073697420616d65742070757275732075726e612e0a
0a
766573746962756c756d20736f64616c657320736f64616c6573206e69626820766974616520696d706572646965742e20766573746962756c756d2073697420616d657420656666696369747572206c656f2c206163206d6f6c6573746965206e69736c2e20646f6e65632061742068656e6472657269742061756775652e20616c697175616d20657420756c7472696365732065782e207072616573656e742072757472756d206d61737361206e756c6c612c20657520626962656e64756d20617263752073757363697069742073697420616d65742e206e756c6c612072757472756d206c6563747573206575206c696265726f206d6f6c6c69732074656d7075732e20657469616d2073656420646f6c6f7220616363756d73616e2c2076756c70757461746520697073756d2076656c2c2074726973746971756520656e696d2e20757420656c656966656e642c206d61676e6120766974616520666163696c697369732073757363697069742c206f64696f206c696265726f206469676e697373696d20656e696d2c20616320626962656e64756d2073617069656e206c656374757320696420746f72746f722e
```
