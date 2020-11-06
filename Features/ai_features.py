import wikipedia
import webbrowser
import os
import datetime
import speech_recognition as sr
from voice.voice_configuration import speak


class Ai_Features:

    def wishMe(self):
        """
        this method returns makes wish to user according to current time
        """
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            speak("Good Morning")
        elif 12 <= hour < 18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak(" I am Elon. How can I help you to think over your problem.")

    def takeCommand(self):
        """
        this is a method used to take the microphone input and return string output
        :return: Text of voice in String format.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return None
        return query

    def wikipedia_search(self, query, sentence_count):
        """
        this method searches the query on wikipedia via its api named wikipedia.
        :param query: String formatted text of user's voice
        :param sentence_count: set the value of readable sentences.
        :return: it prints the result of query and reads it.
        """
        self.speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=sentence_count)
        self.speak("According to Wikipedia")
        print(results)
        self.speak(results)

    def open_website(selfself, query):
        """
        this method opens the website
        :param query: String formatted text of user's voice
        :return: opens the website on internet explorer
        """
        itr_sentence = query.split()
        for data in itr_sentence:
            if ".com" in data:
                website = data
        webbrowser.open(website)

    def location_finder(self, query):
        """
        this method shows the location of the place on the webbrowser
        :param query: String formatted text of user's voice
        :return: location on google maps
        """
        data = query.split(" ")
        location = data[2]
        self.speak("Hold on , I will show you where " + location + " is.")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

    def play_music(self):
        """
        this function play the music which is saved in my system.
        :return: play music on your default music player
        """
        music_dir = "E:\\Songs\\"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    def google_search(self, query):
        """
        this function search the query on google.cpm
        :return: result on google web page
        """
        webbrowser.open("https://www.google.com/?#q=" + query)

