import asyncio
from playwright.async_api import async_playwright

URLS = [f"https://datadash.dev/table-seed-{i}" for i in range(15, 25)]

async def main():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for url in URLS:
            await page.goto(url)
            tables = await page.query_selector_all("table")
            for table in tables:
                rows = await table.query_selector_all("tr")
                for row in rows:
                    cells = await row.query_selector_all("td")
                    for cell in cells:
                        text = await cell.inner_text()
                        try:
                            total += float(text.replace(",", ""))
                        except:
                            pass
        await browser.close()
    print("🔢 Total Sum:", total)

asyncio.run(main())
