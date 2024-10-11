##DECLARACION DE VARIABLES
opc = True
riesgo =""

while(opc ):

##ENTRADAS
    nombre = input("Ingrese sus nombres:\n")
    apellidos = input("Ingrese los apellidos:\n")
    peso = int(input("Ingrese su peso:\n"))
    altura = float(input("Ingrese su altura:\n"))
    
    indice = peso/(altura**2)
 
## CONDICIONES
    if(indice < 24.9):
       riesgo = "Riesgo Bajo"
    elif(indice >=25 or indice <=34.9):
        riesgo = "Riesgo Medio"
    else:
        riesgo = "Riesgo Alto"
    
##MOSTRAR MENSAJES EN VENTANA
    print("\n" + nombre +" " + str(apellidos) )
    print("Indice de masa corporal: " + "{:.2f}".format(indice))
    print(riesgo)

    opcion = input("\nDesea ingresar otro usuario S/N\n").lower()

    if(opcion == "s"):
        opc:True
    else:
        opc = False