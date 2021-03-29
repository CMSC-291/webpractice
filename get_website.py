import requests
from bs4 import BeautifulSoup

site_url = "http://smite.guru"
site_dir = '/builds'
site_html = requests.get(site_url + site_dir).text
soup = BeautifulSoup(site_html, 'html.parser')

print("All the images that are also links")
urls = []
for champion in soup.select('a.champion'):
    urls.append(site_url + champion['href'])

print(urls)
for url in urls:
    champion_text = requests.get(url).text

    soup = BeautifulSoup(champion_text, 'html.parser')
    names = soup.select('.page-header__div > h1')
    if len(names) > 0:
        name = names[0].text
        with open('{}.html'.format(name), 'w') as f:
            f.write(champion_text)
        print("For {}, the following items are most popular".format(name))
        primary_items = []
        for item in soup.select('.primary-item img'):
            primary_items.append(item['alt'])
        print(primary_items)

# print(site_html)