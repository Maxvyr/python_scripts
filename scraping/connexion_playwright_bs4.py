from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://demo.opencart.com/admin/")
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')
    page.is_visible('div.tile-body')
    html = page.inner_html('#content')
    # print(html)
    #now scrap with soup
    soup = BeautifulSoup(html, 'html.parser')
    total_orders = soup.find('h2', {'class': 'pull-right'}).text
    print(f'total orders {total_orders}')