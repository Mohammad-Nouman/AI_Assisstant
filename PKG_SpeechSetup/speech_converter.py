import speech_recognition as sr


class SpeechConverter:
    @staticmethod
    def getCommand():
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            try:
                recognize.pause_threshold = 1
                audio = recognize.listen(source, 0, 4)
                print('Recognizing....')
                command = recognize.recognize_google(audio, language='en-pak')
                command = command.lower()
                print(f'User: {command}')
                return command
            except sr.UnknownValueError:
                print("Cannot Understand properly..")
                print("Speak again")
            except TypeError:
                print("typeerror")
