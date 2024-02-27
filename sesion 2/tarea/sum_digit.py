
def sumar_digitos():
  # pedir al usuario que ingrese un numero
  numero = input("Ingrese un numero: ")

  # convertir el numero a cadena de numeros y sumar
  suma = sum(int(digit) for digit in numero if digit.isdigit())

  return f"La suma de los digitos de {numero} es: {suma}"

print(sumar_digitos())