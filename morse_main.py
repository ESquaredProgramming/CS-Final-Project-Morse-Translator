from morse_gui import *


def main() -> None:
    """
    Function initializes GUI and starts the entire program
    """
    window = Tk()
    window.title("Morse Code")
    window.geometry("260x260")
    window.minsize(260, 260)
    window.resizable(True, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
