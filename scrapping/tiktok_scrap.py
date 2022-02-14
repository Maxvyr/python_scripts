import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.tiktok.com/@maxvyr")
        print(await page.title())
        body = await page.evaluate("document.body.querySelector('div#app')")
        # app = await body.evaluate("div.tiktok-ywuvyb-DivBodyContainer")
        
        print(body)
        # result_handle = await page.evaluate_handle("body => body", handle)
        # print(await result_handle.json_value())
        await browser.close()
        
asyncio.run(main())