from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://www.tiktok.com/@maxvyr")
    print(page.title())
    html = page.inner_html("div#app")
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
        
