# Programa elaborado por Kevin Jesus Martinez Martinez

def options():
    print("Menú",
          "\n1. Transformar una frase o texto a minúsculas o mayúsculas",
          "\n2. Invertir una frase o números",
          "\n3. Mostrar si una frase o número es palíndromo")
    option = input("Selecciona una opción: ")
    verify_num(option)
    

while True:
    def verify_num(num):
        if num.isdigit():
            return num
        else: print("\n***** No introdujiste un número *****\n")

    options()
    option = input("Selecciona una opción: ")
    verify_num(option)
        
    def option1():
        text = input("Ingresa el texto a convertir: ")
        text = text.upper()
        text2 = text.lower()
        print("Mayúsculas: ", text,
              "\nMinúsculas: ", text2)

    def option2():
        inp = input("Ingresa el texto o números a invertir: ")
        inp2 = inp[::-1]
        print("Entrada original: ", inp,
            "\nEntrada invertida: ", inp2)

    def option3():
        def palindromo(texto):
            texto = texto.replace(" ", "").lower()
            return texto == texto[::-1]

        entrada = input("Ingresa una palabra o frase: ")

        if palindromo(entrada):
            print("Tu texto introducido SÍ es palíndromo")
        else:
            print("Tu texto introducido NO es palíndromo")

    def default():
        return "Ingresa una opción válida"

    switch = {
        "1": option1,
        "2": option2,
        "3": option3
    }

    eleccion = option

    result = switch.get(eleccion, default)()
    print(result)

    respuesta = input("¿Deseas ejecutar otro programa? S/N: ")
    if respuesta.lower() != "s":
        break

print("\n *****Gracias por utulizar éste programa!!! *****")
