import requests
from bs4 import BeautifulSoup

def fetch_google_news_headlines():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = 'https://www.google.com/search?q=news+headlines&rlz=1C1RXQR_enIN1014IN1014&oq=news+headline'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')

    if not headlines:
        print("No headlines found. Check the class or tag used in the find_all method.")
        return

    print("Google News Headlines:\n")
    for i, headline in enumerate(headlines, start=1):
        print(f"{i}. {headline.text.strip()}")

if __name__ == "__main__":
    fetch_google_news_headlines()
