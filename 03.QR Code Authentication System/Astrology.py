import requests
from bs4 import BeautifulSoup

def get_horoscope(sign):
    url = f"https://www.horoscope.com/us/horoscopes/daily/{sign}-daily-horoscope.aspx"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Change the class below if necessary based on the current structure of the site
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            horoscope = horoscope_div.get_text(strip=True)
            return horoscope
        else:
            return f"Horsecope not available for {sign.capitalize()}. Element not found."
    else:
        return f"Horoscope not available for {sign.capitalize()}. Status code: {response.status_code}"

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
