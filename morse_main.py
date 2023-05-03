from morse_gui import *

def main():
    window = Tk()
    window.title("Morse Code")
    window.geometry("260x250")
    window.resizable(False,False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
