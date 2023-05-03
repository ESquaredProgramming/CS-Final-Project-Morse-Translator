from playsound import playsound
import time

dot = 'C:/Users/jwbar/OneDrive/Desktop/dot.wav'
dash = 'C:/Users/jwbar/OneDrive/Desktop/dash.wav'

def play(text):
    if text == "dot":
        playsound(dot)
    if text == "dash":
        playsound(dash)

if __name__ == "__main__":
    playsound(dot)
    playsound(dash)
    playsound(dot)
    playsound(dot)
    time.sleep(.75)
    playsound(dash)
    
