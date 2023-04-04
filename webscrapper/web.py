from urllib.request import urlopen
from bs4 import BeautifulSoup

url = r'https://witchculttranslation.com/arc-7/'

def getWebObject(url):
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    return html


def getChapterLinks():
    with open('output.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

        li_tags = soup.find_all('li')
        for li in li_tags:
            li = li.a
            
            with open('links.txt', 'a', encoding='utf-8') as text:

                try: 
                    href = li.get('href')
                    if 'chapter' in href:
                        text.write(href + '\n')

                except: 
                    None

def getText(url):
    obj = getWebObject(url)

    with open('chapter.html', 'w', encoding='utf-8') as f:
        f.write(obj)
    
    with open('chapter.html', 'r', encoding='utf-8') as f:
        
        soup = BeautifulSoup(f, 'html.parser')

        p_tags = soup.find_all('p')

        for p in p_tags:
            try: print(p) ; print()
            except: None
            


with open('links.txt', 'r', encoding='utf-8') as links:

    lines = links.readlines()
    chapUrl = lines[0]

    getText(chapUrl)


