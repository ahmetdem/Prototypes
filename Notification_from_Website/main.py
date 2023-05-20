from urllib.request import urlopen
from bs4 import BeautifulSoup
from emailsender import SEND_EMAIL
import schedule, time

def main():
    url = r'https://aybu.edu.tr/aybu/tr/duyurular'

    def getWebObject(url):
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        return html

    html = getWebObject(url)

    soup = BeautifulSoup(html, 'html.parser')
    div_element = soup.find("div", {"class": "duyuru-list d-flex flex-wrap"})

    # Extract href from all the <a> elements
    a_tag = div_element.find("a")
    href = a_tag.get('href')

    # Read the href from the file
    with open('href.txt', 'r', encoding='utf-8') as f:
        previous_href = f.read()

    if href != previous_href:
        # If the href is different, send an email and update the href.txt
        SEND_EMAIL('ahmetyusufdmr88@gmail.com', content=a_tag)

        with open('href.txt', 'w', encoding='utf-8') as f:
            f.write(href)
            
    else:
        print('No new announcement.')

# Schedule and run main() every 1 minute
schedule.every(10).minutes.do(main)

# Continuously check for pending scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)