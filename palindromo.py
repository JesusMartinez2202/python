def palindromo(texto):
    #Convertimos a minúsculas y eliminamos espacios
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

entrada = input("Ingresa una palabra o frase: ")

if palindromo(entrada):
    print("Tu texto introducido SÍ es palíndromo")
else:
    print("Tu texto introducido NO es palíndromo")
