import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url) # for sending GET reguest to the URL

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = soup.find_all('h1', class_='title')

        hlist = [headline.text.strip() for headline in headlines]

        return hlist
    else:
        print("Failed to retrieve the required page.")

def display(headlines):
    print("Headlines: ")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")

url = "https://sportstar.thehindu.com/cricket/ipl/ipl-news/ipl-2024-opening-ceremony-live-updates-performers-ar-rahman-akshay-kumar-chennai-streaming-info/article67980153.ece"
headlines = scrape(url)

if headlines:
    display(headlines)
else:
    print("No headlines found.")
