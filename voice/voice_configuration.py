import os

"""
pyttsx3 is pytqhon library which is used to access the windows default voices 
"""


def speak(speach):
    """
    this function returns the audio output of AI
    :param speach: this parameter contains the voice command of the user in text format.
    """
    os.system("espeak-ng " + speach)
