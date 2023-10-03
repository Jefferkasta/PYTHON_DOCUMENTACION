#calculadora de impuesto//
#Crea una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

#proporcione el pago sin impuesto: 1000
#proporcione el monto del impuesto: 16
#Pago con impuesto: 1160.0

#defino la funcion
def calculadora(pago_sin_impuesto, impuesto):
    #esta es la formula proporcionado por el creador del curso
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    #creo el print que dara el resultado pedido
    print(f"El pago con impuesto es: {pago_total}")
    #esta sera la funcion con el codigo correspondiente

#fuera de la funcion invoco a las variables que estan pedidas en la funcion, y les inserto un "input"  para pedir los datos al usuario   
pago_sin_impuesto = float(input(f"Ingrese el pago con impuesto:"))
impuesto = float(input(f"Ingrese el impuesto:"))
#al ya tener los datos ingresados por el usuario invoco la funcion con la variable pago_sin_impuesto
pago_sin_impuesto = calculadora(pago_sin_impuesto,impuesto)
    