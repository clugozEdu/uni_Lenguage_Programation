# calculatora 
def calculatora ():
    # get input from user
    num1 = int(input("Ingrese el primer numero: -----> "))
    num2 = int(input("Ingrese el segundo numero: -----> "))
    # get operation from user
    operacion = input(str("Ingrese la operacion:\n 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Division\n Ingrese el numero de la operacion: ----> "))

    # do the operation
    if operacion == "1":
        return f"El resultado de la Suma es: {num1 + num2}"
    elif operacion == "2":
        return f"El resultado de la Resta es: {num1 + num2}"
    elif operacion == "3":
        return f"El resultado de la Multiplicación es: {num1 + num2}"
    elif operacion == "4":
        return f"El resultado de la División es: {num1 + num2}"
    else:
        return "Operacion no valida"

# call the function use print to show the result
print(calculatora())    