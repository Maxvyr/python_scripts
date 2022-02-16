


import asyncio
from playwright.async_api import async_playwright

PRICE_GOAL = 44
URL_RASP = "https://www.kubii.fr/cartes-raspberry-pi/2771-nouveau-raspberry-pi-4-modele-b-2gb-0765756931175.html?search_query=Pi4&results=111"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url=URL_RASP)
        print(await page.title())
        price_recover = await page.evaluate_handle("document.querySelector('span[itemprop=price]').innerHTML")
        print(f"Rasp price is => " + price_recover);
        price_pi_4 = int(price_recover[0:2])

        if(price_pi_4 < PRICE_GOAL):  
            print(f"You can buy")
        else:
            print(f"Nope to high")
            
        await browser.close()
        
asyncio.run(main())