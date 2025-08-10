"""This code takes a word and translates it into Pig Latin"""
def main():
    """Funcion to generate the word"""
    vowels_to_check = "aeioyAEIOU"
    while True:
        introduced_word = input("Please insert word to translate into pig latin: \n")

        if introduced_word.isalpha() and introduced_word[0] in vowels_to_check :
            pig_latin_word = introduced_word + "way"
            print(f"Pig Lating translation of '{introduced_word}' is '{pig_latin_word}'")
        elif introduced_word.isalpha():
            pig_latin_word = introduced_word[1:] + introduced_word[0] + "ay"
            print(f"Pig Lating translation of '{introduced_word}' is '{pig_latin_word}'")
        else:
            print("Sorry, word need to be in alphanumeric characters!")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            print("Bye bye!")
            break

if __name__ == "__main__":
    main()
