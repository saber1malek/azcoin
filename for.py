import requests
import json
import time


class bot():

    def __init__(self):
        self.token = '1664699228:AAHQvvzDD8hl0TweKRKAbPSB0mmbSOn9xbc'
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

b = bot()


def fw():
  for i in range(1):
    b.send_message('Hi. Now is     '+time.asctime( time.localtime(time.time())),104710146)

while True:
    fw()
    time.sleep(5)
