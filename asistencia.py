"""""
Manejo de Asistencia en Python
1) Agregar un estudiante: id, tipo, nombres
2) Codigo  nombre del curso
3)Datos de la sesion: codigo sesion, codigo curso, hora inicio, hora final, fecha
4)Datos asistencia: codigo de la sesion, doc, estudiante codigo si llegó, no llegó o llego tarde:0,1,2
5) Listar los datos de un estudiantes ID
6) Listar los datos de un curso
7) Listar los datos de una sesion con el codigo
8) Listar los datos de un asistencia, codigo de la sesion y codigo del estudiante
9) Consultar por fecha y por hora y codigo del curso que estudiantes llegaron tarde
10)en un curso en un rango de fechas cuantas veces ha llegado tarde, codigo curso rango fechas y codigo del estudiante
11) Salir

ARREGLOS: Length, append: recibir elementos
"""

#Definir Clases

class Estudiante:
    def __init__(self,id,tipoId,nombres):
        self.id = id
        self.tipoId = tipoId
        self.nombres = nombres

class Curso:
    def __init__(self, codigoCurso,nombreCurso):
        self.codigoCurso = codigoCurso
        self.nombreCurso = nombreCurso

class Sesion:
    def __init__(self, codigoSesion, codigoCurso, horaInicio, horaFinal, fecha):
        self.codigoSesion = codigoSesion
        self.codigoCurso = codigoCurso
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        self.fecha = fecha

class Asistencia:
    def __init__ (self, codigoSesion,codigoCurso, idEstudiante,estado):
        self.codigoSesion = codigoSesion
        self.codigoCurso = codigoCurso
        self.idEstudiante = idEstudiante
        self.estado = estado

#CREAR ARREGLOS
listaEstudiantes = []
listaCurso = []
listaSesion = []
listaAsistencia= []

opc = True

while(opc):
    print('Bienvenido al Sistema de Asistencia\n'
          '1)Agregar Estudiante\n'
          '2)Agregar Curso\n'
          '3)Registrar Sesion\n'
          '4)Registrar Asistencia\n'
          '5)Listar Estudiantes\n'
          '6)Listar Curso\n'
          '7)Listar Sesion\n'
          '8)Listar Asistencia\n'
          '9)Salir'
          )
    opcion = input('Seleccione una de las opciones anteriores\n')

    #AÑADIR ESTUDIANTE
    if (opcion == "1"):
        nombre = input("Ingrese el nombre del estudiante:\n")
        id = input("Ingrese la cedula:\n")
        tipo = input("Ingrese el tipo de documento: Cedula, Tarjeta de Identidad,Pasaporte\n")
        estudiante = Estudiante(id,tipo,nombre) 
        listaEstudiantes.append(estudiante)

    #AÑADIR CURSO
    elif (opcion == "2"):
        codigoCurso = input("Ingrese el codigo del curso\n")
        nombreCurso= input("Ingrese el nombre del curso\n")
        curso = Curso(codigoCurso,nombreCurso)
        listaCurso.append(curso)
    
    #AÑADIR SESION
    elif (opcion == "3"):
        codigoSesion = input("Ingrese el codigo de la sesion\n")
        codigoCurso= input("Ingrese el codigo del curso\n")
        horaInicio = input("Ingrese la hora de inicio de la clase \n")
        horaFinal = input("Ingrese la hora de fin de la clase \n")
        fecha = input("Ingrese la fecha \n")
        sesion = Sesion(codigoSesion,codigoCurso,horaInicio,horaFinal,fecha)
        listaSesion.append(sesion)

    #AÑADIR ASISTENCIA
    elif (opcion == "4"):
        codigoSesion = input("Ingrese el codigo de la sesion\n")
        codigoCurso= input("Ingrese el codigo del curso\n")
        idEstudiante = input("Ingrese el id o documento del estudiante\n")
        estado = input("Ingrese una de las siguientes opciones: 0)LLegada Normal, 1)Llegada Tarde, 2)No llegó\n")
        asistencia = Asistencia(codigoSesion,codigoCurso,idEstudiante,estado)
        listaAsistencia.append(asistencia)

    #LISTAR ESTUDIANTE ID
    elif (opcion == "5"):
        codigEstudiante = input("Ingrese el codigo del estudiante a buscar\n")
        for estudiante in listaEstudiantes:
            if(estudiante.id == codigEstudiante):
                print("DATOS DEL ESTUDIANTE\n")
                print(f"ID:{estudiante.id}, TIPO DE ID: {estudiante.tipoId}, NOMBRES: {estudiante.nombres}\n")
            else:
                print("\nESTUDIANTE NO REGISTRADO\n")

    #LISTAR CURSO
    elif (opcion == "6"):
        codigoCurso = input("Ingrese el codigo del curso para buscar\n")
        for curso in listaCurso:
            if(curso.codigoCurso == codigoCurso):
                print("DATOS DEL CURSO\n")
                print(f"CODIGO CURSO:{curso.codigoCurso},  NOMBRE CURSO: {curso.nombreCurso}\n")
            else:
                print("\nCURSO NO REGISTRADO\n")

    #LISTAR SESION
    elif (opcion == "7"):
        codigSesion = input("Ingrese el codigo de la sesion para buscar\n")
        for sesion in listaSesion:
            if(sesion.codigoSesion == codigSesion):
                print("DATOS DE  LA SESION\n")
                print(f"CODIGO SESION:{sesion.codigoSesion}, CODIGO DEL CURSO: {sesion.codigoCurso}, "
                    f" HORA DE INICIO: {sesion.horaInicio}\n,HORA FINAL: {sesion.horaFinal}, FECHA: {sesion.fecha}")
                      
               
            else:
                print("\nSESIÓN NO REGISTRADO\n")

    elif (opcion == "8"):
        estadoMulta = ""
        codigoSesion = input("Ingrese el codigo de la sesion\n")
        codigoEstudiante = input("Ingrese el codigo del estudiante\n")
        for asistencia in listaAsistencia:
            if(asistencia.codigoSesion == codigoSesion and asistencia.idEstudiante == codigoEstudiante ):
                print("DATOS DE  LA ASISTENCIA\n")
                if(asistencia.estado == "0"):
                    estadoMulta = "Sin Multa"
                elif(asistencia.estado == "1"):
                    estadoMulta = "Llego con Retardo"
                else:
                    estadoMulta = "No LLego a Clase"

                print(f"CODIGO SESION:{asistencia.codigoSesion}, CODIGO DEL ESTUDIANTE: {asistencia.codigoCurso}," 
                     f"ESTADO DE MULTA :{asistencia.estado}, {estadoMulta} \n")
            else:
                    print("\nSESIÓN NO REGISTRADO\n") 


    elif (opcion == "9"):
        fechaBusqueda = input("Ingrese la fecha de busqueda\n")
        horaBusqueda = input("Ingrese la hora de busqueda\n")
        codigoCurso = input("Ingrese el codigo del curso\n")
        for asistencia in listaAsistencia:
            if(asistencia.codigoSesion == codigoSesion and asistencia.idEstudiante == codigoEstudiante ):
                print("DATOS DE  LA ASISTENCIA\n")
                if(asistencia.estado == "0"):
                    estadoMulta = "Sin Multa"
                elif(asistencia.estado == "1"):
                    estadoMulta = "Llego con Retardo"
                else:
                    estadoMulta = "No LLego a Clase"

                print(f"CODIGO SESION:{asistencia.codigoSesion}, CODIGO DEL ESTUDIANTE: {asistencia.codigoCurso}," 
                     f"ESTADO DE MULTA :{asistencia.estado}, {estadoMulta} \n")
            else:
                    print("\nSESIÓN NO REGISTRADO\n")      
    

    elif (opcion == "11"):
        print("Saliendo del Sistema")
        opc= False
      
     
    else:
        print("Opcion Invalida")