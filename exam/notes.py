def is_beca(note):
  if note >= 95:
    return "Beca Otorgada"
  else:
    return "Beca Denegada"

def main():
  print(is_beca(100))  # Beca Otorgada
  print(is_beca(90))  # Beca Denegada
  print(is_beca(95))  # Beca Otorgada
  
main()