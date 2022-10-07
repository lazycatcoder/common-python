txt = '''Morbi ac malesuada nisi. Vivamus hendrerit tellus sed diam maximus blandit. Vestibulum eu ipsum quis erat fermentum ornare...'''

banned_words = "hendrerit, ipsum, fermentum"

def load_list(banned_words):
    list_words = banned_words.replace(",", "").lower().split(" ")
    return list_words

def display(list_1, list_2):
    for i in list_1:
        if str.lower(i) in list_2:
            print ("*" * (len(i)), end=" ")
        else:
            print (i, end=" ")

def main():
    List = load_list(banned_words)
    text = str(txt).replace(",", "").split()
    display(text, List)

if __name__ == "__main__":
    main()