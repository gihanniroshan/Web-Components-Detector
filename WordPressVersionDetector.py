import requests
from bs4 import BeautifulSoup

url = "https://www.sliit.lk/" # replace with your WordPress site URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

def detect_wordpress(url):
    try:
        if "wp-content" in response.text or "wp-includes" in response.text:
            return True
        else:
            return False
    except:
        return False

if detect_wordpress(url):
    print(f"{url} is likely a WordPress website.")

    #Getting WP version using meta tag method
    #<meta name="generator" content="WordPress 6.2" />
    generator_tag = soup.find('meta', attrs={'name': 'generator'})
    if generator_tag:
        version_number = generator_tag['content'].split('WordPress ')[1]
        print("WordPress version number:", version_number)
    else:
        print("But WordPress version not found.")
else:
    print(f"{url} does not appear to be a WordPress website.")





