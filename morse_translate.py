def text_to_morse(text: str) -> str:
    """
    Function takes text in the form of words and translates it to morse code
    :param text: a string in the form of words that will be translated
    :return: a string with successfully translated morse code or an error describing what was wrong
    """
    text = text.lower()
    build = ""
    for letter in text:
        # Determines and adds character to build if the character is a letter or number, error is thrown if the
        # character is not part of morse_code
        try:
            build += morse_code[letter] + " "
        except:
            if letter == " ":
                build += "/ "
            else:
                return "Error, the only valid characters\nare letters and numbers."
    return build


def morse_to_text(morse: str) -> str:
    """
    Function takes morse code and translates it to words and numbers
    :param morse: a string a morse code that will be translated
    :return: a string with successfully translated words and numbers or an error describing what was wrong
    """

    # Looks for invalid characters, raises error if invalid characters are found
    try:
        for letter in morse:
            if not (letter == "." or letter == "-" or letter == " " or letter == "/"):
                raise TypeError
    except:
        return "Error, the only valid characters\nare periods, dashes, spaces,\nand forward slashes."

    morse = morse.split(" ")
    build = ""

    # Looks for slashes in a sequence of morse code (ex: --/. ex: /) and raises an error if the slash is mixed with
    # other symbols (ex:--/.)
    try:
        for i in range(len(morse)):
            if morse[i].find("/") != -1:
                if morse[i] == "/":
                    continue
                else:
                    raise NameError
    except:
        return "Error, slashes must be separated\nby spaces on either side."

    # Increments through the list morse, add valid characters to build, return error if sequence is not valid morse
    # code (ex: ----)
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
                break
        if not found:
            return f"Error, [{symbol}] is not a letter or number."
    return build


# A dictionary with keys of all letters and numbers and values with corresponding morse code representations
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
