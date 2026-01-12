
import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath("docs/index.html")
        await page.goto(f"file://{file_path}")

        # Wait for Mermaid to render (it replaces the div with an svg)
        await page.wait_for_selector(".mermaid svg", timeout=5000)

        # Take a screenshot specifically of the mermaid container
        await page.locator('.project-image').screenshot(path='/home/jules/verification/debug_mermaid.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
