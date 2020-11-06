import os

def speak(speach):
    """
    this function returns the audio output of AI
    :param speach: this parameter contains the voice command of the user in text format.
    """
    os.system("espeak-ng " + speach)
