from tkinter import *
import morse_translate
import sound
import time


class GUI:
    def __init__(self, window):
        self.window = window

        self.frameInput = Frame(self.window)
        self.labelInput = Label(self.frameInput, text="Input:")
        self.entryInput = Entry(self.frameInput)
        self.labelInput.pack(padx=5, side="left")
        self.entryInput.pack(padx=5, side="left")
        self.frameInput.pack(anchor="w", pady=10)
        
        self.frameChoose = Frame(self.window)
        self.labelStatus = Label(self.frameChoose, text="Choose:")
        self.radioStatus = IntVar()
        self.radioStatus.set(2)
        self.radio_tm = Radiobutton(self.frameChoose, text="Text to Morse", variable=self.radioStatus, value=0)
        self.radio_mt = Radiobutton(self.frameChoose, text="Morse to Text",variable=self.radioStatus, value=1)
        self.labelStatus.pack(padx=5, side="left")
        self.radio_tm.pack(side="left")
        self.radio_mt.pack(side="left")
        self.frameChoose.pack(anchor="w", pady=10)
        
        self.frameOutput = Frame(self.window)
        self.output_text = StringVar()
        self.output_text.set("Output:")
        self.labelOutput = Label(self.frameOutput, textvariable=self.output_text)
        self.labelOutput.pack(padx=5, side='left')
        self.frameOutput.pack(anchor="w", pady=10)
        
        self.frameTranslate = Frame(self.window)
        self.buttonTranslate = Button(self.frameTranslate, text="Translate", command=self.translate)
        self.buttonPlaySound = Button(self.frameTranslate, text="Play Output", command=self.play_sound)
        self.buttonTranslate.pack()
        self.buttonPlaySound.pack()
        self.frameTranslate.pack(anchor="w", pady=10, padx=75)

    def translate(self):
        output = "what"
        match self.radioStatus.get():
            case 0:
                output = morse_translate.text_to_morse(self.entryInput.get())
            case 1:
                output = morse_translate.morse_to_text(self.entryInput.get())
            case 2:
                output = "Please select a translation direction"
        output = "Output: " + output
        self.output_text.set(output)
    
    def play_sound(self):
        order = []
        for symbol in self.output_text.get()[8:]:
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
        if len(order) > 0:
            for x in order:
                if x == "dot" or x == "dash":
                    sound.play(x)
                elif x == "s":
                    time.sleep(.75)
                elif x == "g":
                    time.sleep(1.5)
            
        

