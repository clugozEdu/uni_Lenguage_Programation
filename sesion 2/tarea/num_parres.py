def number_pares(list):
    pares = []
    for i in list:
        if i % 2 == 0:
            pares.append(i) 
    return pares
  
def main():
    print(number_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    
main()