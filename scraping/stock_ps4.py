from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://www.amazon.fr/PS4-Pro-B-1-blanc/dp/B0774PWPG4/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AMM1O60YDM6A&keywords=ps4+pro&qid=1645033065&sprefix=ps4+pr%2Caps%2C177&sr=8-1"


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url=URL)
    product_name = page.title()
    html = page.inner_html("div#ppd")
    soup = BeautifulSoup(html, "html.parser")
    try :
        product_available = soup.find("span", {"class": "a-size-medium a-color-price"}).text
        print(f"product {product_name} => {product_available}")
    except AttributeError :
        print(f"{product_name} => STOCK")