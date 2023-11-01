import requests
import json

#TOKEN:
TOKEN = "TU TOKEN VA AQUI BEIBI"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = URL + f"sendMessage?text={text}&chat_id={chat_id}"
    requests.get(url)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                chat_id = update["message"]["chat"]["id"]
                message_text = update["message"]["text"]
                if message_text:
                    send_message(chat_id, "Recibí tu mensaje: " + message_text)

if __name__ == '__main__':
    main()
