import moviepy.editor as mp
import speech_recognition as sr
import os
from PKG_OSCommands.OsHandler import OsHandler


class TranscriptGeneration:
    def __init__(self):
        self.__result = None
        self.__audioFileName = None
        self.__filePath = None

    def __convert_to_audio(self, query):
        self.__filePath = TranscriptGeneration.search_file(query)

        clip = mp.VideoFileClip(self.__filePath)
        try:
            self.__audioFileName = f'{query}.wav'
            clip.audio.write_audiofile(self.__audioFileName)

            audioFolderName = "Extracted Audio"
            path = OsHandler.getDestinationFolderPath(audioFolderName)

            os.rename(os.path.join(os.getcwd(), self.__audioFileName), f'{audioFolderName}/{self.__audioFileName}')

            print("file created successfully")
            audioFilePath = os.path.join(path, self.__audioFileName)
            return audioFilePath
        except FileExistsError:
            print("File Already Exists")

    @staticmethod
    def search_file(query):
        root_dir = "D:\\"

        for relPath, dirs, files in os.walk(root_dir):
            for f1 in files:
                temp = f1.lower()
                if os.path.splitext(temp)[0] == query:
                    filePath = os.path.join(relPath, f1)
                    return filePath

    def audio_to_text(self, query):
        recognize = sr.Recognizer()
        try:
            audio = sr.AudioFile(self.__convert_to_audio(query))

            with audio as source:
                recognize.adjust_for_ambient_noise(source)
                audio_file = recognize.record(source)
                print("Generating text....")
                self.__result = recognize.recognize_google(audio_file)
                print(f'Recognizer: \n{self.__result}')
            self.__createTranscriptFile(query)
        except Exception:
            print("Cannot create the file")

    def __createTranscriptFile(self, query):
        if self.__result:
            fileName = f'{query}.txt'
            folderPath = OsHandler.getDestinationFolderPath("Transcipt Output")
            filePath = os.path.join(folderPath, fileName)

            with open(filePath, mode='w') as file:
                file.write(self.__result)
                print("file is ready")
                file.close()

            os.startfile(filePath)
        else:
            print("file does not exist")

