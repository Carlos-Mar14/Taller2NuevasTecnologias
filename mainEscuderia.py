from Escuderia import Escuderia

escuderias=[]

numeroEscuderia=0

while(numeroEscuderia<2):
    escuderia = Escuderia()
    escuderia.nombre=input("Digite el nombre de la escuderia: ")
    escuderia.motor=input("Digite el motor de la escuderia: ")
    escuderia.piloto1=input("Digita el nombre del primer piloto: ")
    escuderia.piloto2=input("Digita el nombre del segundo piloto: ")
    escuderia.costoAnual=int(input("Digite el costo anual: "))
    
    escuderias.append(escuderia)
    numeroEscuderia+=1
    
if(escuderias[0].costoAnual == escuderias[1].costoAnual):
    print("Las escuderias tienen el mismo valor")
elif(escuderias[0].costoAnual > escuderias[1].costoAnual):
    print(f"La escuderia mas cara1 es:  {escuderias[0].nombre}")
else:
    print(f"La escuderia mas cara2 es:  {escuderias[1].nombre}")