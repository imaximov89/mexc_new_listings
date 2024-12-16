from new_listings_scrapper import *
from send_telegram_notification import *
from time import sleep

def main():
    last_announcement_cache = ""
    print("Starting the script.")
    while(True):
        last_announcement = new_listings_scrapper()
        if last_announcement != "":
            if last_announcement_cache != last_announcement:
                last_announcement_cache  = last_announcement
                send_telegram_notification(last_announcement)
        sleep(30)

if __name__ == '__main__':
    main()