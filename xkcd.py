import requests
from bs4 import BeautifulSoup as bs



def get_image_url(link):
    html_data = requests.get(link).content
    # print(html_data)
    soup = bs(html_data)
    image_div = soup.find("div", {"id":"comic"})
    image_url = image_div.find("img").get("src")
    final_link = "https:"+ image_url
    return final_link

for i in range(1,11):
    joke_num = i
    link = f"https://xkcd.com/{joke_num}/"
    image_url = get_image_url(link)
    print(image_url)

url = "https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg"

def download_image(image_url):
    image_data = requests.get(image_url).content

    file = open ("test.jpg", wb)
