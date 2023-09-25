
temp = float(input("Ingrese temperatura a convertir:"))
grad = input("Es Fahrenheit(F) o Celsius(C)? ").upper()

if grad == "F":
    resultado = (temp - 32) * 5/9  
    print("Tu resultado es: ",resultado)
    
elif grad == "C":
    resultado = temp * 1.8 + 32
    print("Tu resultado es: ",resultado)
    
else:
    print("Escala incorrecta")