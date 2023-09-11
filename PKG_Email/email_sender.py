import smtplib
import os
from email.message import EmailMessage


class Email:
    recieverDict = {"sabir": "fa20-bse-100@cuilahore.edu.pk",
                    "ali": "sp21-bse-019@cuilahore.edu.pk",
                    "azeem": "sp21-bse-025@cuilahore.edu.pk",
                    "nouman": "sp21-bse-035@cuilahore.edu.pk",
                    "azim":"azimamjad412@gmail.com"}

    def __init__(self, reciever, subject, message):
        self.__senderEmail = "azeemamjad412@gmail.com"
        self.__senderPass = os.environ.get("Email_Pass")
        self.__setRecieverEmail(reciever)
        self.__subject = subject
        self.__message = message

    def __setRecieverEmail(self, reciever):
        try:
            self.__recieverEmail = Email.recieverDict[reciever]
        except KeyError:
            self.__recieverEmail = Email.recieverDict["azeem"]

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com',
                              587)
        server.starttls()
        server.login(self.__senderEmail, self.__senderPass)
        email = EmailMessage()
        email['From'] = self.__senderEmail
        email['To'] = self.__recieverEmail
        email['Subject'] = self.__subject
        email.set_content(self.__message)
        server.send_message(email)
        print("send successfully")
