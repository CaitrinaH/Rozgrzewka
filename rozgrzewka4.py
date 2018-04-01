#napisz funkcję, która zaszyfruje tekst szyfrem cezara
ALPHABET_START = ord('a')
ALPHABET_LENGTH = ord('z') - ord('a') + 1

def cesar(text):
    cesared = ''
    for x in text:
       cesared += chr((ord(x) - ALPHABET_START + 1) %ALPHABET_LENGTH + ALPHABET_START)
    return cesared  
    

