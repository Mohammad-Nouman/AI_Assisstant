import pyttsx3 as textToSpeech


class Speaker:
    def __init__(self):
        self.__engine = textToSpeech.init('sapi5')
        self.__voices = self.__engine.getProperty('voices')
        self.configureVoice(0)

    def configureVoice(self, voiceType):
        self.__engine.setProperty('voice', self.__voices[voiceType].id)

    def speak(self, *argsText):
        for text in argsText:
            self.__engine.say(text)
            self.__engine.runAndWait()
