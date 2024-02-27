# Contador de letras
def count_letter():
    # obtener palabra del usuario
    word = input("Escribe una palabra: ")

    # contar letras omitiendo espacios
    letter_count = sum(len(word) for word in word.split())

    return f"La palabra o frase {word} tiene {letter_count} letras"

# llamar a la funcion y mostrar el resultado
print(count_letter())