from new_listings_scrapper import *
from send_telegram_notification import *
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def main():
    sleep_period = 600
    last_announcement_cache = ""
    chrome_service = Service(executable_path='/usr/bin/chromedriver')
    chrome_service.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    print("Starting the script.")
    while(True):
        last_announcement = new_listings_scrapper(driver=chrome_driver)
        if last_announcement != "":
            if last_announcement_cache != last_announcement:
                last_announcement_cache = last_announcement
                send_telegram_notification(last_announcement)
                if last_announcement.find('Will List') == -1:
                    chrome_driver.close()
                    chrome_driver.quit()
                    chrome_service.stop()
                    break
        sleep(sleep_period)

if __name__ == '__main__':
    main()