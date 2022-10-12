from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

PRICE_GOAL = 46
URL_RASP = "https://www.kubii.fr/cartes-raspberry-pi/2771-nouveau-raspberry-pi-4-modele-b-2gb-0765756931175.html" \
           "?search_query=Pi4&results=111 "
message_email = f"""
<h1>Hello</h1>

    <p>You can buy a raspeberry now</p>
    <a href={URL_RASP}>LINK</a>

<h2>Great, See ya</h2>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url=URL_RASP)
    print(page.title())
    body = page.inner_html(".product")
    soup = BeautifulSoup(body, "html.parser")
    price_recover = soup.find("span", {'id': 'our_price_display'}).text
    print(f"Rasp price is => {price_recover}")
    price_pi_4 = int(price_recover[0:2])
    if price_pi_4 < PRICE_GOAL:
        print(f"You can buy")
        # TODO send email
    else:
        print(f"Nope to high")
