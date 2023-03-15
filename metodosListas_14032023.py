data = ["Jaider","Ronald","Didier"]

def menu():
    print("APRENDIENDO LOS METODOS DE LISTAS")
    print("1. Metodo Append")
    print("2. Metodo Index")
    print("3. Metodo Count")
    print("4. Metodo Clear")
    print("5. Metodo Extend")
    print("6. Metodo Remove")
    print("7. Metodo Len")
    print("8. Metodo Pop")
    print("9. Metodo Sort")
    print("10. Metodo Insert")
    print("11. Metodo Reverse")
    opcion = int(input("Digita una opción: "))

    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4): 
        pass
    elif (opcion == 5): 
        pass
    elif (opcion == 6): 
        pass
    elif (opcion == 7): 
        pass
    elif (opcion == 8): 
        pass
    elif (opcion == 9): 
        pass
    elif (opcion == 10): 
        print(""); insertar=insert(data); print(insertar)
    elif (opcion == 11): 
        print("la funcion del metodo reverse es mostrar a lista en orden contrario")
        datos=reversa(data); print(datos)


def insert(data): #Funcion Insert de Jaider
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
def reversa(a): #Funcion Reverse de Ronald
    l = list(a)
    l.reverse()
    return l


#Resto de funciones


#Codigo principal
if __name__ == "__main__":
    menu()
