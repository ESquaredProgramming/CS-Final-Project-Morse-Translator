def text_to_morse(text):
    text = text.lower()
    build = ""
    for letter in text:
        try:
            build += morse_code[letter] + " "
        except:
            if letter == " ":
                build += "/ "
            else:
                build += "?"
#         while build.find("/ / ") != -1:
#             build = build.replace("/ / ", "/ ")
    return build

def morse_to_text(morse):
    try:
        for letter in morse:
            if not(letter == "." or letter == "-" or letter == " " or letter == "/"):
                raise TypeError
    except:
        return "Error, the only valid characters\nare periods, dashes, spaces,\nand forward slashes"

    morse = morse.split(" ")
    build = ""
    try:
        for i in range(len(morse)):
            if morse[i].find("/") != -1:
                if morse[i] == "/":
                    continue
                else:
                    raise NameError
    except:
        return "Error, slashes must be separated\nby spaces on either side"
    
    for symbol in morse:
        found = False
        if symbol == "/":
            build += " "
            found = True
            continue
        for letter in morse_code:
            if morse_code[letter] == symbol:
                build += letter
                found = True
                continue
        if not(found):
            build += "?"
    return build

morse_code = {
    'a': '.-', 
    'b': '-...', 
    'c': '-.-.', 
    'd': '-..', 
    'e': '.', 
    'f': '..-.', 
    'g': '--.', 
    'h': '....', 
    'i': '..', 
    'j': '.---', 
    'k': '-.-', 
    'l': '.-..', 
    'm': '--', 
    'n': '-.', 
    'o': '---', 
    'p': '.--.', 
    'q': '--.-', 
    'r': '.-.', 
    's': '...', 
    't': '-', 
    'u': '..-', 
    'v': '...-', 
    'w': '.--', 
    'x': '-..-', 
    'y': '-.--', 
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}
if __name__ == "__main__":
    print(text_to_morse("hello my name is  Justin"))
    print(morse_to_text("... .-.. . . .--. / .. ... / ..-. --- .-. / - .... . / .-- . .- -.-"))

