def dato_recursivo(numero):
    if numero >= 1:
        print(numero)
        dato_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero<=0:
        print("numero incorrecto")
dato_recursivo(7)