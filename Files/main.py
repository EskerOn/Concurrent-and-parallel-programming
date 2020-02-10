from arch import Archivo #se importa la clase Archivo desde el fichero arch
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
