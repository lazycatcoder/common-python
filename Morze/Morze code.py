#Morse code   
international_morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

morse_translation = {}
for key, value in international_morse_code.items():
    morse_translation[value] = key

def english_morse(txt):
    morse = []
    for char in txt:
        if char in international_morse_code:
            morse.append(international_morse_code[char])
    return " ".join(morse)

def morse_english(txt):
    txt = txt.split(" ")
    english = []
    for code in txt:
        if code in morse_translation:
            english.append(morse_translation[code])
    return " ".join(english)

def main():
    while True:
        choise = input("Morse code - 1, English text - 2: ").upper()
        if choise == "1" or choise == "2":
            break

    if choise == "1":
        txt = input("Enter Morse code (with a space after each code): ")
        english = morse_english(txt)
        print (f"English text: {english}")

    elif choise == "2":
        txt = input("Enter the text: ").upper()
        morse = english_morse(txt)
        print (f"Morse code: {morse}")

if __name__ == "__main__":
    main()