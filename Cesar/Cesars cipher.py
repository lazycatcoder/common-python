import re

def cesar(text, code, choise):
    result = ""
    text_split = text.split(" ")
    for t in text_split:
        for i in range(len(t)):
            char = t[i]
            if choise == 1:
                if char.isupper():
                    result += chr((ord(char) + code-65) % 26 + 65)
                elif char.isdigit():
                    num = (int(char) + code) % 10
                    result += str(num)   
                else:
                    result += chr((ord(char) + code-97) % 26 + 97)  
            elif choise == 2:
                if char.isupper():
                    result += chr((ord(char) - code-65) % 26 + 65)
                elif char.isdigit():
                    num = (int(char) - code) % 10
                    result += str(num) 
                else:
                    result += chr((ord(char) - code-97) % 26 + 97) 
        result += " "
    return result

def main():
    while True:
        try:
            choise = int(input("make a choice (1-encrypt, 2-decrypt):\n"))
            if 1 <= choise <= 2: 
                break  
            else:
                print ("try again")
        except:
            print ("please enter a number 1 or 2")
    txt = str(input("message: "))
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', txt)
    code = int(input("code: "))

    cesar (text, code, choise)

    print ("cipher: " + cesar(text, code, choise))

if __name__ == "__main__":
    main()