from PKG_Email.email_sender import Email
from PKG_SpeechSetup.speech import Speaker
from PKG_SpeechSetup.speech_converter import SpeechConverter
from PKG_OSCommands.OsHandler import OsHandler
from PKG_TransciptGenerator.transcriptFileGenerator import TranscriptGeneration
from PKG_GUIGenerator.Natural_language_processor import *
from PKG_GUIGenerator.Widgets import *
from PKG_GUIGenerator.Connector import *
import os

# Tokenizing the Class for processing
commandList = []

def tokenizeSent(query):
    # Tokenizing the Class for processing
    tokenizer = Tokenizer(query)
    tokenizer.getTokens()
    tokenizer.removePunctuation()
    words = tokenizer.removeStopword()
    return words


def buildConnection(words):
    # building connection with database
    connection = Connector()
    connection.connect()

    index = None
    index1 = []
    for count in range(len(words)):
        if len(index1) == 0:
            index1 = connection.searchFword(words[count])
        else:
            index2 = connection.searchLword(words[count])
            if len(index2) != 0:
                if index2[0] in index1:
                    index = index2[0][0]
    return index

tasks = {}
task = lambda f: tasks.setdefault(f.__name__, f)


@task  # Screen Generator
def value001():
    title = 'Gui'
    height = 500
    width = 500
    screen = Screen(title, height, width)
    return screen.getString()


# assuming fixing col of label and entry

@task  # Label Generator
def value002():
    labelName = 0
    labelRow = 0
    text = 'Nomi'
    framename = 'frame1'
    layout = 'pack'
    label = Label(framename, labelName, text, layout)
    setLayout(layout, label)
    return label.getString()


def setLayout(layout, element):
    if layout == 'grid':
        col = 1
        row = 1
        element.setGrid(col, row)
    elif layout == 'place':
        x = 0
        y = 0
        element.setPlace(x, y)
    elif layout == 'pack':
        side = 'LEFT'
        fill = 'X'
        pad = 10
        ipad = 4
        element.setPack(side, fill, pad, ipad)


@task  # Entry Generator
def value004():
    name = 1
    col = 2
    row = 1
    framename = 'frame1'
    width = 10
    layout = 'pack'
    entry = Entry(framename, name, width, layout)
    setLayout(layout, entry)
    return entry.getString()


@task  # ComboBox Generator
def value005():
    name = 1
    framename = 'frame1'
    values = (1, 2, 3, 4, 'test')
    layout = 'pack'
    combobox = ComboBox(framename, name, values, layout)
    setLayout(layout, combobox)
    return combobox.getString()


@task  # MessageBox Generator
def value006():
    name = 1
    title = 'ALERT'
    text = 'Sabir is BadAss'
    messageBox = MessageBox(name, title, text)
    return messageBox.getString()


@task  # RadioButton Generator
def value007():
    name = 1
    framename = 'frame1'
    values = 1
    layout = 'pack'
    text = 'hello'
    radiobtn = RadioButton(framename, name, text, values, layout)
    setLayout(layout, radiobtn)
    return radiobtn.getString()


@task  # Scrolltext Generator
def value008():
    name = 1
    framename = 'frame1'
    width = 10
    layout = 'pack'
    height = 10
    text = 'Nomiboya'
    scrolltxt = ScrolledText(framename, name, width, height, text, layout)
    setLayout(layout, scrolltxt)
    return scrolltxt.getString()


@task  # Position Changer
def valueposition():
    name = 'label'
    id = '1'
    requiredWidget = name + id
    newCommand = ''
    layout = '1'

    # search the required command from list
    copyCommandList = commandList.copy()
    for command in copyCommandList:
        if requiredWidget in command:
            tokens = command.split("\n")

            for index in range(len(tokens) - 2):
                if index == len(tokens) - 3:
                    layout += tokens[index]
                else:
                    newCommand += tokens[index] + '\n'

    if layout != '1':
        tokens = layout.split('(')
        tokens = tokens[0].split('.')

        widgets = Widgets()
        setLayout(tokens[1], widgets)
        newCommand += requiredWidget + widgets.setLayout(tokens[1])
    else:
        print('element not found')
    # scrolltxt = ScrolledText(framename, name, width, height, text, layout)
    # setLayout(layout, scrolltxt)
    # return scrolltxt.getString()


@task  # spinbox Generator
def value009():
    name = 1
    framename = 'frame1'
    width = 10
    layout = 'pack'
    min = 10
    max = 100
    spinbox = SpinBox(framename, name, width, min, max, layout)
    setLayout(layout, spinbox)
    return spinbox.getString()


@task  # frame generatot
def value003():
    background = "Silver"
    border = 10
    borderWidth = 5
    # releief = "SUNKEN"
    name = 1
    side = 'LEFT'  # .place(relx=.5,rely=.5,anchor= CENTER)
    fill = 'Y'
    pad = 1
    ipad = 1
    frame = Frame(name, background, border, borderWidth)
    command = frame.getFrame()
    command = command + frame.placeFrameInCenter()
    return command


# peocessing the command
def getCommand(value):
    if value == None:
        print("Command Not exits")
    else:
        key = 'value' + value
        partialCommand = tasks[key]()
        return partialCommand


def createScreen(finalList):
    directory = os.getcwd()
    f = open(directory + "\Task.py", "w")
    f.writelines(finalList)
    f.close()


def showScreen():
    directory = os.getcwd()
    os.system('cd ' + directory)
    os.system('pyinstaller --onefile Task.py')
    directory += '\dist\Task.exe'
    os.startfile(r'' + directory)


def emailCheck(s):
    s.speak('To Whom you want to send email')
    name = SpeechConverter.getCommand()

    s.speak('what is the subject of the email')
    subject = SpeechConverter.getCommand()

    s.speak('tell me the text in your email')
    message = SpeechConverter.getCommand()

    sender = Email(name, subject, message)
    sender.send_mail()


if __name__ == '__main__':
    # command = OsHandler()
    # generate = TranscriptGeneration()
    #
    #
    # while True:
    #     my_query = SpeechConverter.getCommand()
    #     speaker = Speaker()
    #
    #     if 'hello' in my_query:
    #         speaker.speak("Hello,I am Your Personal AI Assistant",
    #                       "How can I help you?")
    #
    #     elif 'how are you' in my_query:
    #         speaker.speak("I am Fine,What about you?")
    #
    #     elif 'are you there' in my_query:
    #         speaker.speak('Yes, I am here,what do you want me to do ')
    #
    #     elif 'thanks' in my_query:
    #         speaker.speak('No Problem, I am glad to assist you')
    #
    #     elif 'open' in my_query and 'folder' not in my_query:
    #         speaker.speak(command.open_app(my_query))
    #
    #     elif 'close' in my_query:
    #         speaker.speak(command.close_app(my_query))
    #
    #     elif 'weather' in my_query:
    #         speaker.speak(command.weather(my_query))
    #
    #     elif 'battery' in my_query:
    #         speaker.speak(command.battery_check())
    #
    #     elif 'internet speed' in my_query:
    #         speaker.speak('Please wait..it will take a little time to calculate it...')
    #         speaker.speak(command.internet_speed_check())
    #
    #     elif 'volume' in my_query:
    #         command.volume_settings(my_query)
    #
    #     elif 'cpu' in my_query:
    #         speaker.speak(command.cpu_details())
    #
    #     elif 'write' in my_query:
    #         speaker.speak('What do you want me to write')
    #         text = SpeechConverter.getCommand()
    #         command.write_in_notepad(text)
    #
    #     elif 'play' in my_query:
    #         speaker.speak('Your music is starting in a while')
    #         command.play_audio_file(my_query)
    #
    #     elif 'set' and 'reminder' in my_query:
    #         speaker.speak('Tell me what reminder you want to set')
    #         reminder = SpeechConverter.getCommand()
    #         speaker.speak(command.set_reminder(reminder))
    #
    #     elif 'check reminder' and 'check my reminder' in my_query:
    #         speaker.speak(command.check_reminder())
    #
    #     elif 'open' and 'folder' in my_query:
    #         speaker.speak('Searching your requested folder')
    #         speaker.speak(command.open_folders(my_query))
    #
    #     elif 'set' and 'alarm' in my_query:
    #         try:
    #             speaker.speak('set the hour')
    #             hour = SpeechConverter.getCommand()
    #             speaker.speak('set the minute')
    #             minute = SpeechConverter.getCommand()
    #             speaker.speak('set am or pm')
    #             amPm = SpeechConverter.getCommand()
    #             speaker.speak(command.set_alarm(int(hour), int(minute), amPm))
    #         except Exception:
    #             speaker.speak('cannot set the alarm')
    #
    #     elif 'screenshot' in my_query:
    #         speaker.speak(command.take_screenshot())
    #
    #     elif "send" and "email" in my_query:
    #         emailCheck(speaker)
    #
    #     elif 'generate' and 'transcript' in my_query:
    #         speaker.speak('For which video file you want a transcript')
    #         fileName = SpeechConverter.getCommand()
    #         generate.audio_to_text(fileName)
    #
    #     elif 'bye' in my_query:
    #         speaker.speak("Ok Bye, Call me whenever you need me")
    #         quit()

    userCommands = [" create a screen", "create a frame", "create a combobox", "create a spinbox",
                    "create a scrolltext", "create a label", "Create Entry", "Create Entry", "change position"]

    for com in userCommands:
        # query = fetchCommand()
        words = tokenizeSent(com)
        value = buildConnection(words)
        command = getCommand(value)
        commandList.append(command)

    commandList.append('window.mainloop()')
    print(commandList)

    copyCommandlist = commandList.copy()
    for item in copyCommandlist:
        if item is None:
            commandList.remove(item)

    createScreen(commandList)
    showScreen()
    print('Done')