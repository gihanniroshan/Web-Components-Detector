import requests
from bs4 import BeautifulSoup

url = "https://example.com" # replace with your WordPress site URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
generator_tag = soup.find('meta', attrs={'name': 'generator'})
if generator_tag:
    version_number = generator_tag['content'].split('WordPress ')[1]
    print("WordPress version number:", version_number)
else:
    print("WordPress version not found")
