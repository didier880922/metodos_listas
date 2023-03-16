from os import system; system("cls")
data = ["Jaider","Ronald","Andres","Cristian","Manuel","Hector","Emil","Didier"]
data2 = [1,2,3,4,5,6,7]

def menu():
    print("APRENDIENDO LOS METODOS DE LISTAS")
    print("1. Metodo Append") #✓
    print("2. Metodo Index")
    print("3. Metodo Count") #✓
    print("4. Metodo Clear")
    print("5. Metodo Extend") #✓
    print("6. Metodo Remove") #✓
    print("7. Metodo Len")
    print("8. Metodo Pop") #✓
    print("9. Metodo Sort") #✓
    print("10. Metodo Insert") #✓
    print("11. Metodo Reverse") #✓
    opcion = int(input("Digita una opción: "))

    if (opcion == 1):
        Metodo_Append(data,data2)
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        print(data)
        x=Fcount(data)
        print(x)
    elif (opcion == 4): 
        pass
    elif (opcion == 5): 
        motodo_extend(data,data2)
    elif (opcion == 6): 
        cel(data)
    elif (opcion == 7): 
        pass
    elif (opcion == 8): 
        fun_pop(data)
    elif (opcion == 9): 
        compu()
    elif (opcion == 10): 
        print(""); insertar=insert(data); print(insertar)
    elif (opcion == 11): 
        datos=reversa(data); print(datos)

#Funciones

def Metodo_Append(data,data2): #Función Append de Hector Garcia
    Pregunta=input("¿Desear agregar un elemento a la lista? Si/No: ") #La primera letra es Mayuscula
    if Pregunta=="Si":
        print("1.Nombres")
        print("2.Codigos")
        Opcion=input("¿Bienvenido que desea agregar?: ")
        if Opcion=="1":
            DataNom=(input("Ingrese los nombres que desea agregar a la lista: "))
            data.append(DataNom)
            print(data)
        elif Opcion=="2":
            DataCodi=int(input("Ingrese el codigo que desea agregar a la lista: "))
            data2.append(DataCodi)
            print(data2)
    elif Pregunta=="No":
        print("Entendido, tenga un buen dia")            

#Funcion Index no disponible

def Fcount(lista):
    dato1=int(input("ingrese el dato numerico que desea conocer su repeticion: "))
    dato2=input("Ingrese el valor textual que desea conocer la repeticion: ")
    final=lista.count(dato1)
    final1=lista.count(dato2)
    return final1,final

#Funcion Clear no disponible

def motodo_extend(data,data2): #Función Extend de Manuel Montes Barrios
    dato=input("Quiere agregar un dato a la lista? si/no: ")
    if dato == "si":
        x=input("ingrese un dato: ")
        data2.append(x)
        data.extend(data2)
        print(data)
    elif dato=="no":
        data.extend(data2)
        print(data)
def cel(data): # Funcion Remove de Emil Sanchez
    print("")
    for i in data:
        print(i)
    print("")
    dato=(input("Ingrese el nombre que desea eliminar !!(Escribe el nombre tal cual como se ve en la lista)!! : "))
    system ("cls")
    print("Eliminando nombre de la lista...")
    data.remove(dato)
    print("")
    for i in data:
        print(i)       

#Funcion Len no disponible

def fun_pop(data): #Función Pop de Cristian Barrera
    print(data)
    x=(int(input("ingrese el elemento que desea el dato a borrar: ")))
    v=data.pop(x)
    print("nueva lista", data)
def compu(): #Función Sort de Andres Barragán
    data.sort()
    print("La lista se organizará automaticamente")
    print("-----------------------")
    print(data)
    print("-----------------------")
    print("listo")
    print("you did it")
def insert(data): #Función Insert de Jaider
    print("Bienvenido a la inserción de datos, primero se te pedirá un dato para añadir a la lista (data)")
    print("Luego se te pedirá la posición (indexación) en donde se ubicará el dato a la lista, por ejemplo: 0"); print("")
    print("1. Dato Textual"); print("2. Dato Numerico")
    tipo=int(input("Que tipo de dato añadirás a la lista?: "))
    if tipo == 1:
        datos=input("Escriba el dato textual que desea ingresar: ")
        posicion=int(input("Escriba la posición del nuevo dato: "))
    elif tipo == 2:
        datos=float(input("Escriba el dato numerico que desea ingresar: "))
        posicion=int(input("Escriba la posición del nuevo dato: "))
    data.insert(posicion,datos)
    return data
def reversa(a): #Función Reverse de Ronald
    print("la funcion del metodo reverse es mostrar a lista en orden contrario")
    l = list(a)
    l.reverse()
    return l

#Codigo principal
if __name__ == "__main__":

    print("Cambios en el archivo....")
