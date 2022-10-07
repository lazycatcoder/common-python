lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
          'Z': 'bbaab', '\n': 'bbbbb'}

def hide_cipher(encrypt_text, code, decrypt=False):
    text_symbols = list(encrypt_text)
    n = len(code)
    result =""
    i = 0
    for symbol in text_symbols:
        shift = code[i%n]
        if symbol.islower():
            if decrypt == True:
                shift = -shift
            shifted_c = chr((ord(symbol) - ord('a') + shift)%26 + ord('a'))
            result += shifted_c
            i += 1
        elif symbol.isdigit():
            shifted_c = (int(symbol) + shift) % 10
            result += str(shifted_c)
            i += 1
        else:
            result += symbol 
    return result.replace(" ", "")

def encrypt(text):
    cipher = ''
    for letter in text:
        if letter.isalpha():
            cipher += lookup[letter]
        elif letter.isdigit():
            cipher += letter
        elif letter == ' ':
            cipher += ' '
    print("\n"+f"Bacon's cipher: {cipher}"+"\n")
    return cipher

def decrypt(cipher):
    message = ''
    i = 0
    while i < len(cipher) - 4:
        substr = cipher[i:i + 5]
        if substr[0] != ' ':
            message += list(lookup.keys())[list(lookup.values()).index(substr)]
            i += 5
        else:
            message += ' '
            i += 1
    return message.lower()

def decrypt_message(text, code, decrypt=False):
    n = len(code)
    result =""
    i = 0
    for symbol in text:
        shift = -code[i%n]
        if symbol.islower():
            if decrypt == True:
                shift = -shift
            shifted_c = chr((ord(symbol) - ord('a') + shift)%26 + ord('a'))
            result += shifted_c
            i += 1
        elif symbol.isdigit():
            shifted_c = (int(symbol) + shift) % 10
            result += str(shifted_c)
            i += 1
        else:
            result += symbol 
    print("\n"+f"Bacon's cipher: {result}"+"\n")
    return result

def message_cleanup(message):
    message_simbols = list(message)
    clean_message = ''
    for s in message_simbols:
        if s.isalpha():
            clean_message += s
        elif s.isdigit():
            clean_message += s
        elif s == ' ':             
            clean_message += " " 
        elif s == '\n':
            clean_message += '\n' 
    return clean_message

def text_punctuation(txt):
    message_simbols = list(txt)
    p_message = ''
    marks=[" ", ",", "."]
    for s in message_simbols:
        if s.isalpha():
            p_message += s
        elif s.isdigit():
            p_message += s
        elif s in marks:             
            p_message += s 
    return p_message

def punctuation_indexes(txt):
    ind = []
    text_dot_indexes = [i for i, dots in enumerate(txt) if dots == '.']
    ind.extend(text_dot_indexes)
    text_comma_indexes = [i for i, commas in enumerate(txt) if commas == ',']
    ind.extend(text_comma_indexes)
    text_space_indexes = [i for i, spaces in enumerate(txt) if spaces == ' ']
    ind.extend(text_space_indexes)
    return sorted(ind)

def punctuation_marks(text_p):
    mess = list(text_p)
    res = ""
    marks = [" ", ",", "."]
    for m in mess:
        if m in marks:
            res += m
    return list(res)

def decrypt_punct(decrypted_data, indexes, marks):
    txt=list(decrypted_data)
    c = 0
    for i in indexes:
        txt.insert(i, marks[c])
        c += 1
    joined_txt = "".join(txt)
    return joined_txt

def main():
    code = [7, 15, 4, 2, 32, 3, 17, 26] #input code to encrypt/decrypt
    while True: 
        try:
            movement = int(input("Enter type of operation:\n1) Encrypt, 2) Decrypt, 3) Exit\n"))
            if movement >= 1 and movement <= 3: 
                break
            else: 
                print("try again")
        except:
            pass
    if movement == 3:
        exit()
    elif movement == 1:
        # txt = input("Enter text that will be encrypted: ") #input text to encrypt
        txt = "The? range /of an electric :car depends- on the number and_ type of batteries used, and !the aerodynamics, weight and* type of vehicle, performance requirements, and the@ weather." #example
        text_p = text_punctuation(txt)
        print (f"text: {text_p}")

        indexes = punctuation_indexes(text_p)
        print (f"indexes: {indexes}")

        marks = punctuation_marks(text_p)
        print (f"marks: {marks}")

        text_cleanup = message_cleanup(txt)
        text = text_cleanup.upper()
        encrypt_text = encrypt(text)
        encrypted_data = hide_cipher(encrypt_text, code)
        print ("Encrypted message: " + encrypted_data)
    else:
        # txt = input("Enter text that will be decrypted: ") #input code to decrypt
        txt = "ipedhdrbiqechdrbhpedgdrahpfdgeraiqecgerahqfdgdrbhqecgdraiqedgdsahpfcheraipecgdsaipedherahqedgdrahpfcgdrbhpecgdsahpfcgdsbhpfcgdsbiqechdraiqedgdrbiqechdrbiqecherbipedhdrbiqechdraiqedhdsahpfdgdrahpfcgeraipechdrahpedhdsahpfdhdrbiqfcgdrbiqfcgerahqfdgdrbhqecgdsahpechdrbiqecheraipedgdrbhqecgdrbhpfcgerbhqechdrbhpedgdrahqfcgdrahqfchdraiqfcgesahqfdgdsahpecgdraipedgdrbhqfdgdraiqfdgdraiqedgdrahpfdgdrbhpecgdsaipedgerbipechdraipecgdsbhpedhesahqfcgdrahqfchdraiqfcgesbipecgesbipedgdrbiqecgerbipfchdrbhpechesaipecgdrbhpfcheraipechesbhpfcgerahqechdsaiqfchdraipfdgdrahpecherbhpedgdrbhpfcgdsahqechdrahqedgdrbhpedgdrbhpfcgdsbhpechdraiqedhdrbiqechdrahpecherbhpedheraiqechesahqechdsbhpedgdrahpedgdsbhpfdhdrbhpfcgds" #example
        text = txt.lower()

        # indexes = [] #input indexes of dots/commas/spaces to readability improvements
        indexes = [3, 9, 12, 15, 24, 28, 36, 39, 43, 50, 54, 59, 62, 72, 77, 78, 82, 86, 99, 100, 107, 111, 116, 119, 127, 128, 140, 153, 154, 158, 162, 170] #example
       
        marks = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ',', ' ', ' ', ' ', '.'] #example
        
        decrypt_text = decrypt_message(text, code)
        decrypted_data = decrypt(decrypt_text)
        decrypted_data_with_punctuation = decrypt_punct(decrypted_data, indexes, marks)
        print ("Decrypted message with punctuation: " + decrypted_data_with_punctuation)

if __name__ == '__main__':
    main()