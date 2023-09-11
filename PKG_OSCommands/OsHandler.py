import datetime as dt
import threading
import time
from datetime import datetime
from playsound import playsound  # pip install playsound==1.2.2
import psutil
import pyautogui
import os
import random
from bs4 import BeautifulSoup
import requests
import speedtest
import pywhatkit


class OsHandler:
    def __init__(self):
        self.__apps = {"paint": "mspaint", "chrome": "chrome", "excel": "EXCEL", "notepad": "notepad",
                       "word": "WINWORD", "power point": "POWERPNT", "vs code": "code", "opera": "opera",
                       "explorer": "explorer"}

        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}

    def greeting(self):
        hour = int(dt.datetime.now().hour)
        current_time = time.strftime('%I:%M %p')

        if 0 < hour <= 12:
            greet = 'Good Morning...'
        elif 12 < hour <= 15:
            greet = 'Good Afternoon'
        else:
            greet = 'Good Evening'

        return f'{greet}, it\'s {current_time}'

    def weather(self, query):
        city = query.replace('what is the weather in ', ' ')
        url = f'https://www.google.com/search?q=weather+in+{city}'
        res = requests.get(url, headers=self.__headers)

        data = BeautifulSoup(res.text, 'html.parser')
        location = data.select('#wob_loc')[0].getText()
        time_ = data.select('#wob_dts')[0].getText()
        info = data.select('#wob_dc')[0].getText()
        weather = data.select('#wob_tm')[0].getText()

        return f'The current weather in {location} is {weather}..°Celsius...,{info} updated at {time_} '

    @staticmethod
    def getDestinationFolderPath(folderName):
        path = os.path.join(os.getcwd(), folderName)

        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def write_in_notepad(self, query):
        current_time = dt.datetime.now().strftime('%H:%M')
        filename = f'{current_time.replace(":", "-")}-note.txt'

        destinationFolder = 'Notes'
        destinationFolder_path = self.getDestinationFolderPath(destinationFolder)

        with open(filename, 'a') as file:
            file.write(query)

        os.rename(os.path.join(os.getcwd(), filename), f'{destinationFolder}/{filename}')
        file_path = os.path.join(destinationFolder_path, filename)
        os.startfile(file_path)

    def play_audio_file(self, query):  # example query = play music.mp3
        file_found = False
        query = query.replace('play ', '')
        query = query.replace(' ', '')
        root_dir = "C:\\"
        file_to_search = f'{query}'

        for relPath, dirs, files in os.walk(root_dir):
            if file_to_search in files:
                full_path = os.path.join(relPath, file_to_search)
                os.startfile(full_path)
                # print(full_path)
                file_found = True
                return random.choice(['Playing...', 'Starting...'])

        if not file_found:
            pywhatkit.playonyt(query)
            return random.choice(['Playing...', 'Starting...'])

    def set_reminder(self, query):
        query = query.replace('i ', 'you ')
        reminder_file = open('remider.txt', 'w')
        reminder_file.write(query)
        reminder_file.close()
        return f'You have told me to remember that {query}'

    def check_reminder(self):
        reminder_file = open('remider.txt', 'r')
        return f'You have set reminder that {reminder_file.read()}'

    def open_folders(self, query):
        folder_found = False
        query = query.replace('open', '')
        query = query.replace('folder', '')
        query = query.strip()
        root_dir = "D:\\"
        folder_to_search = query

        for relPath, dirs, files in os.walk(root_dir):
            for folder in dirs:
                folder = folder.strip()
                folder = folder.lower()
                if folder_to_search == folder:
                    full_path = os.path.join(relPath, folder_to_search)
                    os.system(f'start {full_path}')
                    print(full_path)
                    folder_found = True
                    return random.choice(['Opening...', 'Launching...'])

        if not folder_found:
            return 'No such folder found in your pc'

    def run_alarm(self):
        path = os.path.join(os.getcwd(), 'utils', 'AlarmClock.mp3')
        playsound(path)

    def set_alarm(self, hour, minute, am_pm):
        am_pm = am_pm.replace('.', '')
        if am_pm == "pm":
            hour = hour + 12

        current_time = datetime.now()

        alarm_date = dt.datetime.now().date()
        alarm_time = datetime(alarm_date.year, alarm_date.month, alarm_date.day, hour, minute, 0)

        difference = (alarm_time - current_time)

        total_sec = difference.total_seconds()

        timer = threading.Timer(total_sec, self.run_alarm)
        timer.start()

        h = str(int(total_sec * (1 / (3600 * total_sec))))
        m = str(int(total_sec * (1 / 60)))
        s = str(round(total_sec, 2))
        return f'Your alarm will ring in {h} hours, {m} minutes and {s} seconds'

    def take_screenshot(self):
        current_time = dt.datetime.now().strftime('%H:%M')
        file_name = f'{current_time.replace(":", "-")}.png'

        destination_dir_path = self.getDestinationFolderPath('ScreenShots')
        file_path = os.path.join(destination_dir_path, file_name)

        image = pyautogui.screenshot()
        image.save(file_path)
        os.startfile(file_path)
        return 'Here is your screenshot'

    def open_app(self, query):
        app_found = False
        all_apps = list(self.__apps.keys())
        for app in all_apps:
            if app in query:
                try:
                    if os.system(f"start {self.__apps[app]}") == 0:  # when !=0, it means any error
                        app_found = True
                        return random.choice(['Launching...', 'Opening...'])
                    else:
                        raise Exception('App not found in your pc')
                except:
                    return 'No such app is installed on your pc'

        if not app_found:
            return 'Sorry..No such app Found'

    def close_app(self, query):
        app_closed = False
        all_apps = list(self.__apps.keys())
        for app in all_apps:
            if app in query:
                try:
                    if os.system(f"taskkill /f /im {self.__apps[app]}.exe") == 0:  # when !=0, it means any error
                        app_closed = True
                        return random.choice(['Closing...', 'Terminating...'])
                    else:
                        raise Exception('App not found on your pc')
                except:
                    return 'No such app is installed on your pc'

        if not app_closed:
            return 'Sorry.. No such app Found'

    def battery_check(self):
        battery = psutil.sensors_battery()
        try:
            percentage = battery.percent
            return f'The system has {percentage} percent battery remaining'
        except AttributeError:
            return 'Battery percentage is not supported by your computer'

    def internet_speed_check(self):
        st = speedtest.Speedtest()
        dl_ = st.download()
        dl = round(dl_ / (10 ** 6), 2)
        ul_ = st.upload()
        ul = round(ul_ / (10 ** 6), 2)
        return f'Your downloading speed is {dl} mbps and Your uploading speed is {ul} mbps'

    def volume_settings(self, query):
        if 'up' in query:
            pyautogui.press('volumeup')
        elif 'down' in query:
            pyautogui.press('volumedown')
        elif 'mute' in query:
            pyautogui.press('volumemute')

    def cpu_details(self):
        cpu_detail = str(psutil.cpu_percent())
        return f'Your CPU is working at {cpu_detail} percentage'
