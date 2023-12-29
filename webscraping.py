#this code will scraping the quote and the author from the web.
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting quotes and authors
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Printing the quotes and authors
    for i in range(len(quotes)):
        print(f'Quote: {quotes[i].text}')
        print(f'Author: {authors[i].text}')
        print('---')
else:
    print('Failed to retrieve the page. Status code:', response.status_code)
