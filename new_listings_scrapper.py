from datetime import datetime
from send_telegram_notification import *
from bs4 import BeautifulSoup
from requests import get

def new_listings_scrapper(driver):
    try:
        base_url = "https://www.mexc.com"
        url = "https://www.mexc.com/support/sections/15425930840734"
        last_announcement_text = ""

        driver.get(url)

        if driver.page_source:
            last_announcement_date = datetime(2001, 1, 1)
            announcements_soup = BeautifulSoup(driver.page_source, 'html.parser')
            announcements = announcements_soup.find_all('a')
            for announcement in announcements:
                current_announcement_text = announcement.get_text()
                if current_announcement_text.find('Will List') > 0:
                    if announcement.get('href'):
                        announcement_url = ''.join([base_url, announcement.get('href')])
                        if announcement_url:
                            announcement_source = get(announcement_url)
                            if announcement_source.content:
                                announcement_soup = BeautifulSoup(announcement_source.content, 'html.parser')
                                if announcement_soup:
                                    announcement_time =  announcement_soup.time['datetime']
                                    if announcement_time:
                                        current_announcement_date = datetime.fromisoformat(announcement_time[0:-1])
                                        if current_announcement_date > last_announcement_date:
                                            last_announcement_date = current_announcement_date
                                            last_announcement_text = current_announcement_text
            # print(last_announcement_text)
        return last_announcement_text
    except Exception as err:
        scrape_error_message = f"Unable to scrape URL. {err}"
        send_telegram_notification(scrape_error_message)