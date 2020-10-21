from bs4 import BeautifulSoup
import requests
from pprint import pprint

query = "python"
location = "bengaluru"
url = f"https://www.indeed.co.in/jobs?q={query}&l={location}"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard'})


results = {}
for i, row in enumerate(rows):
    try:
        apply = f"{url}&vjk={row.get('data-jk').strip()}"
        title = row.find('h2').text.strip().split('\n')[0]
        company = row.find('span', attrs={'class': 'company'}).text.strip()
        location = row.find('span', attrs={'class': 'location'}).text.strip()
        summary = row.find('div', attrs={'class': 'summary'}).text.strip()
        results[i] = {'url': apply, 'title': title,
                      'location': location, 'company': company, 'summary': summary}
    except:
        continue
    print(i)
    pprint(results[i])
