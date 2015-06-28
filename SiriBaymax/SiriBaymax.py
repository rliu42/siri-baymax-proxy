import imaplib
import email
import time
import threading
import re
import urllib.request
import urllib.parse
import json

class SiriBaymax:
    def __init__(self, username, password, baymax_server):
        self.username = username
        self.password = password
        self.request_url = baymax_server
        self.connection = None
        self.fetch = None
        self.stop = True

    def connect(self, start_thread=True):
        self.stop = False

        try:
            self.connection = imaplib.IMAP4_SSL("imap.mail.me.com", "993") #Connect to server
        except:
            raise Exception("Connection to iCloud failed. Check your internet connection")

        try:
            self.connection.login(self.username, self.password) #Login
        except:
            raise Exception("Login to iCloud failed. Check your credentials")

        self.connection.select("Notes")

        typ, data = self.connection.search(None, 'ALL') 

        for num in data[0].split():
            self.connection.store(num, '+FLAGS', '\\Deleted')
        self.connection.expunge()

        if (start_thread == True):
            self.fetch = threading.Thread(target=self.__fetch)
            self.fetch.start()
        return (True)

    def disconnect(self):
        if (self.stop == False):
            self.stop = True
            self.fetch.join()

        if (self.connection != None):
            self.connection.logout()
            self.connection = None
        return (True)

    def __fetch(self):
        time.sleep(1)
        while (self.stop == False):
            try:
                recent = self.connection.recent() #Check for new notes
                if (recent[1][0] != None):
                    time.sleep(1)
                    typ, data = self.connection.search(None, 'ALL')
                    for num in data[0].split():
                        raw_email = self.connection.fetch(num, '(RFC822)')[1][0][1]
                        email_message = email.message_from_bytes(raw_email)
                        if email_message.is_multipart():
                            for payload in email_message.get_payload():
                                text = payload.get_payload()
                        else:
                            text = email_message.get_payload()

                        self.connection.store(num, '+FLAGS', '\\Deleted')
                        self.connection.expunge()
                        text = re.sub(r"\<.*?\>", "", text.replace("\n","").replace("\r",""))
                        urllib.request.urlopen(self.request_url + urllib.parse.quote(text))
                        time.sleep(1)
                self.connection.noop()
                time.sleep(1)
            except: #Reconnect handler if connection is closed
                print("Connection failure")
                try:
                    self.connection.logout()
                    print("Logout succesful")
                except:
                    print("Couldn't logout")
                self.connection = False
                print("Trying to reconnect")
                self.connect(False)
                print("Reconnected")
        return()