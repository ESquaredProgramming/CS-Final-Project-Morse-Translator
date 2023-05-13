from playsound import playsound
import os

# locations of dots and dashes

dot = os.path.dirname(__file__) + '/dot.wav'
dash = os.path.dirname(__file__) + '/dash.wav'


def play(text: str) -> None:
    """
    Function plays audible sound determined by text using the playsound module
    :param text: String that holds either dot or dash
    """
    if text == "dot":
        playsound(dot)
    if text == "dash":
        playsound(dash)
