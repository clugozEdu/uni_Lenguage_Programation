def letter_revers(word_1, word_2, word_3):
    return f"Primera palabra: {word_1[::-1]}, Segunda palabra: {word_2[::-1]}, Tercera palabra: {word_3[::-1]}"


def main():
    print(letter_revers("Hola", "Mundo", "Cruel"))
    
main()