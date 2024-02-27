# Function to sum two numbers
def sum(a, b):
    return a + b

# Function to rest two numbers
def rest(a, b):
    return a - b

# Function to multiply two numbers
def multiplication(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: División por cero."
    else:
        return a / b

def calculator():
    print("Bienvenido a la calculadora")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    while True:
        # Tomar la elección del usuario
        choice = input("Ingresa el número de la operación (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if choice == '1':
                print(f"El resultado de {num1} + {num2} es {sum(num1, num2)}")
            elif choice == '2':
                print(f"El resultado de {num1} - {num2} es {rest(num1, num2)}")
            elif choice == '3':
                print(f"El resultado de {num1} * {num2} es {multiplication(num1, num2)}")
            elif choice == '4':
                resultado = divide(num1, num2)
                if resultado == "Error: División por cero.":
                    print(resultado)
                else:
                    print(f"El resultado de {num1} / {num2} es {resultado}")
            break
        else:
            print("Opción no válida. Por favor ingresa una opción válida (1/2/3/4).")


calculator()