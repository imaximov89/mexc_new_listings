import requests
import os
from dotenv import load_dotenv

def send_telegram_notification(message):
    try:
        print(f"Sending telegram notification. {message}")

        load_dotenv()

        TOKEN = os.getenv("TELEGRAM_TOKEN")
        CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url).json()
    except:
        raise Exception("Unable to send telegram notification.")
