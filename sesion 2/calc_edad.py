def calc_edad(nacimiento):
  return 2024 - nacimiento

def evalEdad(edad):
  if edad >= 18:
    return "Eres mayor de edad"
  else:
    return "Eres menor de edad"
  
def main():
  nac = eval(input("Dime tu año de nacimiento: "))
  print(f"Tu edad es: {calc_edad(nac)} y eres {evalEdad(calc_edad(nac))}")
  
main()