# Programa elaborado por: Kevin Jesus Martinez Martinez

print("\n ***** Programa que realiza el factorial de un número y muestra números primos *****\n")

def verify_num(opcion):
        if opcion.isdigit():
            return True
        else: 
            print("\n***** Introduce algo válido *****")
        
def option1():
            opc = input("\nEscribe un número entero para calcular su factorial: ")
            if verify_num(opc):
                opc = int(opc)
                n = opc
                def comprob (opc):
                    if (opc < 0):
                        print("Los números negativos no son válidos.")
                        return False
                    elif (opc == 0 or opc == 1):
                        print("El factorial de ", opc, " es 1")
                        return False
                    else:
                        return True
                    
                def factorial (n):
                    for i in range(1, n):
                        n *= i
                    print("El factorial de ", opc, " es ", n)
            
                if comprob(opc) == True:
                    factorial(n)

def option2():
            opc = input("Ingresa un número: ")
            if verify_num(opc):
                opc = int(opc)
                n = opc
                def comproba(n):
                    if (n < 0):
                        print("Los números negativos no son primos")
                    elif(n == 0):
                        print("El 0 no es primo ni par (???)")
                    else: return True
                
                if (comproba(n) == True):
                    def primo(n):
                        for i in range(1, n+1):
                            if(i == 1):
                                print(i)
                            elif (i == 2 or i == 3 or i == 5 or i == 7):
                                print(i, " Es primo")
                            elif (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
                                print(i) 
                            elif (i % i == 0 and i % 1 == 0):
                                print(i, " Es primo")
                    primo(n)

def default():
            return "\nIngresa una opción válida"

while True:
    print("\nMenú",
          "\n1. Factorial de un número.",
          "\n2. Mostrar números primos en un rango")
    opcion = input("\nSelecciona una opción: ")
    if(verify_num(opcion) == True):
        switch = {
             "1": option1,
             "2": option2
             }       

        eleccion = opcion

        result = switch.get(eleccion, default)()
        print(result)

    respuesta = input("\n¿Deseas realizar otra operación? S/N: ")
    if respuesta.lower() != "s":
        print("\n***** Gracias por utilizar el programa *****")
        break