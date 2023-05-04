from Coctel import Coctel

precioCoctel=0
costo = 0

tipo=int(input("Digita 1. para coctel de frutas,  2. para Shot: "))

if(tipo):
    coctel = Coctel()
    if (tipo == 1):
        coctel.tipo=("Coctel de frutas")
        coctel.nombre = input("Digita el nombre del coctel: ")
        coctel.precio = int(input("Digita el precio del coctel: "))
        coctel.grado = input("Digita el grado de alcohol: ")
        coctel.cantidad = int(input("Digita cantidad: "))
        coctel.anejamiento = int(input("Digita cuantos dias tiene de anejamiento: "))
        if (coctel.anejamiento == 1):
            costo = coctel.cantidad * coctel.precio
            print(f"El costo del Coctel es de: {costo}")
        elif (coctel.anejamiento == 2):
            costo = (coctel.cantidad * coctel.precio)
            descuento = (coctel.cantidad * coctel.precio) * 0.2
            print(f"El costo del Coctel es de: {costo - descuento}")
        elif (coctel.anejamiento == 3):
            costo = (coctel.cantidad * coctel.precio)
            descuento = (coctel.cantidad * coctel.precio) * 0.5
            print(f"El costo del Coctel es de: {costo - descuento}")
        elif ( coctel.anejamiento > 3):
            
            print("No se puede vender el trago")
        else:
            print("Digita numero valido")
    elif (tipo == 2):
        coctel.tipo=("Shot")
        coctel.nombre=input("Digita el nombre del shot: ")
        coctel.precio=int(input("Digita el precio del shot: "))
        coctel.grado=input("Digita el grado de alcohol: ")
        coctel.cantidad=int(input("Digita canrtidad: "))
        coctel.anejamiento=0
        costo = coctel.precio * coctel.cantidad 
        print(f"EL costo del shot es de {costo}")