import requests
from bs4 import BeautifulSoup

def get_horoscope(sign):
    url = f"https://www.horoscope.com/us/horoscopes/daily/{sign}-daily-horoscope.aspx"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope = soup.find('div', class_='main-horoscope').get_text(strip=True)
        return horoscope
    else:
        return "Horoscope not available."

def get_all_horoscopes():
    zodiac_signs = [
        "aries", "taurus", "gemini", "cancer", 
        "leo", "virgo", "libra", "scorpio", 
        "sagittarius", "capricorn", "aquarius", "pisces"
    ]
    
    horoscopes = {}
    
    for sign in zodiac_signs:
        horoscopes[sign.capitalize()] = get_horoscope(sign)
        
    return horoscopes

if __name__ == "__main__":
    daily_horoscopes = get_all_horoscopes()
    for sign, horoscope in daily_horoscopes.items():
        print(f"{sign}: {horoscope}\n")
