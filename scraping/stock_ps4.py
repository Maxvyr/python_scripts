from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

URL = "https://www.amazon.fr/PS4-Pro-B-1-blanc/dp/B0774PWPG4/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91" \
      "&crid=1AMM1O60YDM6A&keywords=ps4+pro&qid=1645033065&sprefix=ps4+pr%2Caps%2C177&sr=8-1 "

message_email_begin = """
<h1>Hello</h1>
"""

message_email_end = """.

<h2>Great, See ya</h2>

"""
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url=URL)
    product_name = page.title()
    html = page.inner_html("div#ppd")
    soup = BeautifulSoup(html, "html.parser")
    try:
        product_available = soup.find("span", {"class": "a-size-medium a-color-price"}).text
        res = f"product {product_name} => {product_available}"
        print(res)
    except AttributeError:
        res = f"{product_name} => STOCK"
        link = f"Link => {URL}"
        # Call method for send email here
        print("Email Send")
