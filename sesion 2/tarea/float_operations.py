def calc_floats(number_1, number_2):
  number_1 = float(number_1)
  number_2 = float(number_2)
  
  return f"Suma: {number_1 + number_2}, Resta: {number_1 - number_2}, Multiplicación: {number_1 * number_2}, División: {number_1 / number_2}"

def main():
  print(calc_floats(10.203, 5.343))
  
  
main()