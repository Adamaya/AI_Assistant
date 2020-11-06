import pyttsx3

"""
pyttsx3 is pytqhon library which is used to access the windows default voices 
"""
engine = pyttsx3.init('sapi5')


class Voice_Configuration:
    def configure_voice(self, voiceID):
        """
        This method configures the voice of the ai according to user requirements.
        :param voiceID: it contains the voice id of selected voice by user.
        """
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voiceID].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.7)

    def speak(self, speach):
        """
        this function returns the audio output of AI
        :param speach: this parameter contains the voice command of the user in text format.
        """
        engine.say(speach)
        engine.runAndWait()
