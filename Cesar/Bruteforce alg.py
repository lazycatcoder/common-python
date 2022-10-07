# BruteForce algorithm
def decryptor(txt,key):
    lower_txt = txt.lower()
    decrypted = ""
    for lt in lower_txt:
        if lt.islower():
            lt_index = ord(lt) - ord('a')
            lt_pos = (lt_index-key) % 26 + ord('a')
            lt_og = chr(lt_pos)
            decrypted += lt_og
        else:
            decrypted += lt
    return decrypted

txt = "Oyeajpeopo dwra okhraz pda iuopanu kb odeiianejc hwgao qjzan pda okqpd lkha kb Iwno"

for i in range(1, 26):
    text = decryptor(txt,i)
    print ("For key {}, decrypted text: {}".format(i, text))