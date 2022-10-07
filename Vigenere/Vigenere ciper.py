import re

def vigenere(text, code, choise, decrypt=False):
    n = len(code)
    result = ""
    i = 0
    for c in text:
        if choise == 1:
            shift = code[i%n]
        elif choise == 2:
            shift = -code[i%n]
        if c.islower():
            if decrypt == True:
                shift = -shift
            shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_c
            i += 1
        elif c.isupper():
            if decrypt == True:
                shift = -shift
            shifted_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            result += shifted_c
            i += 1
        elif c.isdigit():
            shifted_c = (int(c) + shift) % 10
            result += str(shifted_c)
            i += 1
        else:
            result += c
    return result

def main():
    while True:
        try:
            choise = int(input("make a choice (1-encode, 2-decode):\n"))
            if 1 <= choise <= 2: 
                break  
            else:
                print ("try again")
        except:
            print ("please enter a number 1 or 2")
    txt = str(input("message: "))
    # txt = "a cryptocurrency entrepreneur bought the world's largest painting for 62 million dollars"
    text = re.sub('[^a-zA-Z0-9 \n]', '', txt)
    code = [7, 2, 4, 5, 23]
    result_txt = vigenere(text, code, choise)  
    print ("result: " + result_txt)

if __name__ == "__main__":
    main()