from tkinter import *
import morse_translate
import morse_sound
from time import sleep


class GUI:
    def __init__(self, window) -> None:
        """
        Function creates a GUI using tkinter
        """
        self.window = window

        # Creates and packs a frame for the entry box
        self.frameInput = Frame(self.window)
        self.labelInput = Label(self.frameInput, text="Input:")
        self.entryInput = Entry(self.frameInput)
        self.labelInput.pack(padx=5, side="left")
        self.entryInput.pack(padx=5, side="left")
        self.frameInput.pack(anchor="w", pady=10)

        # Creates and packs a frame consisting of radio buttons
        self.frameChoose = Frame(self.window)
        self.labelStatus = Label(self.frameChoose, text="Choose:")
        self.radioStatus = IntVar()
        self.radioStatus.set(2)
        self.radio_tm = Radiobutton(self.frameChoose, text="Text to Morse", variable=self.radioStatus, value=0)
        self.radio_mt = Radiobutton(self.frameChoose, text="Morse to Text", variable=self.radioStatus, value=1)
        self.labelStatus.pack(padx=5, side="left")
        self.radio_tm.pack(side="left")
        self.radio_mt.pack(side="left")
        self.frameChoose.pack(anchor="w", pady=10)

        # Creates and packs a frame for the output of the translation
        self.frameOutput = Frame(self.window)
        self.output_text = StringVar()
        self.output_text.set("Output:")
        self.labelOutput = Label(self.frameOutput, textvariable=self.output_text)
        self.labelOutput.pack(padx=5, side='left')
        self.frameOutput.pack(anchor="w", pady=10)

        # Creates and packs a frame for both the translate button and play morse button
        self.frameTranslate = Frame(self.window)
        self.buttonTranslate = Button(self.frameTranslate, text="Translate", command=self.translate)
        self.buttonPlaySound = Button(self.frameTranslate, text="Play Morse", command=self.play_sound)
        self.buttonTranslate.pack()
        self.buttonPlaySound.pack(pady=5)
        self.frameTranslate.pack(anchor="w", pady=10, padx=75)

        self.labelLength = Label(self.window, text="Extend window if output is clipped")
        self.labelLength.pack()

    def translate(self) -> None:
        """
        Function takes the input from the entry on the GUI, translates it, and displays it on the GUI
        """
        output = ""

        # Determines proper translation direction, translates the entry box using the morse_translate file,
        # and changes the GUI the output
        match self.radioStatus.get():
            case 0:
                if len(self.entryInput.get()) > 50:
                    output = "Entry must be less than or equal to 50 characters"
                else:
                    output = morse_translate.text_to_morse(self.entryInput.get())
            case 1:
                if len(self.entryInput.get()) > 300:
                    output = "Entry must be less than or equal to 300 characters"
                else:
                    output = morse_translate.morse_to_text(self.entryInput.get())
            case 2:
                output = "Please select a translation direction"
        output = "Output: " + output
        self.output_text.set(output)

    def play_sound(self) -> None:
        """
        Function audibly plays the morse code that resides either in the entry box or the output box
        """
        order = []
        read = ""

        # Determines where the morse code is and sets read to the dots and dashes
        match self.radioStatus.get():
            case 0:
                read = self.output_text.get()[8:]
            case 1:
                read = morse_translate.text_to_morse(self.output_text.get()[8:])
            case 2:
                read = ""

        # Adds strings to the list order to prepare for playing
        for symbol in read:
            if symbol == ".":
                order.append("dot")
            elif symbol == "-":
                order.append("dash")
            elif symbol == " ":
                order.append("s")
            elif symbol == "/":
                order.append("g")
            else:
                order = []
                break

        # Runs through order and plays the correct files using the morse_sound file
        if len(order) > 0:
            for x in order:
                if x == "dot" or x == "dash":
                    morse_sound.play(x)
                elif x == "s":
                    sleep(.75)
                elif x == "g":
                    sleep(1.75)
