import os
os.system("cls")

def menu():
    print("\tElija una opción\n1) Grabar Datos\n2) Buscar\n3) Imprimir Certificados\n4) Salir")
    
def nif():
    while True:
        try:
            numNif = input("Ingrese el NIF\n> ").upper()
        except ValueError:
            print("Ingrese un NIF valido")
            continue
        if len(numNif) == 12:
            if "-" not in numNif:
                print("NIF debe contener un guion")
            else:
                return numNif
        else:
            print("Ingrese un NIF ejemplo 'xxxxxxxx-xxx'")
    
def nombre():
    while True:
        nombre = input("Ingrese nombre y apellido\n> ").strip()
        if not nombre:
            print("Nombre no puede venir vacio")
            continue
        else:
            if len(nombre) < 8:
                print("Nombre debe ser mayor a 8 caracteres")
            else:
                return nombre
        
def edad():
    while True:
        try:
            edad = int(input("Ingrese edad\n> "))   
        except ValueError:
            print("Edad no puede ser un caracter")
            continue
        if edad < 1:
            print("Edad debe ser mayor a 1")
        else:
            return edad
        
def grabarDatos():
    while True:
        numeroIF = nif()
        nombreNIF = nombre()
        edadNIF = edad()
        agregar = {
            "nif": numeroIF,
            "nombre": nombreNIF,
            "edad": edadNIF,
        }
        datos.append(agregar)
        break
        
def buscar():
    while True:
        buscar = input("Ingrese NIF a buscar\n> ").upper()
        for encontrar in datos:
            if buscar == encontrar["nif"]:
                if buscar.endswith("SP"):
                    nacionalidad = "Español"
                else:
                    nacionalidad = "Union Europea"
                print(f"Nombre: {encontrar["nombre"]}\nEdad: {encontrar["edad"]}\nNIF: {encontrar["nif"]}\nPertenencia: {nacionalidad}")
                input("Presione enter para continuar")
                return None
            else:
                print("NIF no encontrado")
                
def imprimirCertificados():
    while True:
        print(f"1) Nacimiento ${nacimiento}\n2) Estado Conyugal ${estadoConyugal}\n3) Pertenecia a la Unión Europea ${pertenencia}")
        try:
            opcionCertificado = int(input("Elija certificado requerido\n> "))
        except ValueError:
            print("Opción no valida")
            continue
        if opcionCertificado == 1:
            buscar = input("Ingrese NIF a buscar\n> ").upper()
            for encontrar in datos:
                if buscar == encontrar["nif"]:
                    if buscar.endswith("SP"):
                        nacionalidad = "Español"
                    else:
                        nacionalidad = "Union Europea"
                    print("\tCertificado de nacimiento")
                    print(f"Nombre: {encontrar["nombre"]}\nEdad: {encontrar["edad"]}\nNIF: {encontrar["nif"]}\nPertenencia: {nacionalidad}")
                    input("Presione enter para continuar")
                    return None
                else:
                    print("NIF no encontrado")
        elif opcionCertificado == 2:
            buscar = input("Ingrese NIF a buscar\n> ").upper()
            for encontrar in datos:
                if buscar == encontrar["nif"]:
                    if buscar.endswith("SP"):
                        nacionalidad = "Español"
                    else:
                        nacionalidad = "Union Europea"
                    print("\tCertificado Estado Conyugal")
                    print(f"Nombre: {encontrar["nombre"]}\nEdad: {encontrar["edad"]}\nNIF: {encontrar["nif"]}\nPertenencia: {nacionalidad}")
                    input("Presione enter para continuar")
                    return None
                else:
                    print("NIF no encontrado")
        elif opcionCertificado == 3:
            buscar = input("Ingrese NIF a buscar\n> ").upper()
            for encontrar in datos:
                if buscar == encontrar["nif"]:
                    if buscar.endswith("SP"):
                        nacionalidad = "Español"
                    else:
                        nacionalidad = "Union Europea"
                    print("\tCertificado Pertenencia a la Unión Europea")
                    print(f"Nombre: {encontrar["nombre"]}\nEdad: {encontrar["edad"]}\nNIF: {encontrar["nif"]}\nPertenencia: {nacionalidad}")
                    input("Presione enter para continuar")
                    return None
                else:
                    print("NIF no encontrado")
    
def salir():
    print("HA SALIDO...")
    print("Andres Felipe Escobar Velez")
    print("Versión 1")
        
datos = []

nacimiento = 0
estadoConyugal = 0
pertenencia = 0

while True:
    try:
        nacimiento = int(input("Ingrese el valor del Certificado de Nacimiento\n> "))
        if nacimiento < 1500 or nacimiento > 5000:
            print("Valor debe ser entre '1500 y 5000'")
            continue
        estadoConyugal = int(input("Ingrese el valor del Certificado de Estado Conyugal\n> "))
        if estadoConyugal < 1500 or estadoConyugal > 5000:
            print("Valor debe ser entre '1500 y 5000'")
            continue
        pertenencia = int(input("Ingrese el valor del Certificado de Pertenencia a la Unión Europea\n> "))
        if pertenencia < 1500 or pertenencia > 5000:
            print("Valor debe ser entre '1500 y 5000'")
            continue
    except ValueError:
        print("Ingrese un valor numerico")
        continue
    break

while True:
    menu()
    try:
        opcion = int(input("Elija una opción\n> "))
    except ValueError:
        print("Elija una opción valida")
        continue
    if opcion == 1:
        print("GRABAR")
        grabarDatos()
        
    elif opcion == 2:
        print("BUSCAR")
        buscar()
        
    elif opcion == 3:
        print("IMPRIMIR CERTIFICADOS")
        imprimirCertificados()
    
    elif opcion == 4:
        salir()
        break
    
    else:
        print("Opción no valida")


    
    
        
