
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

        # Get computed styles for nav-links
        nav_links_style = await page.eval_on_selector('.nav-links', """
            el => {
                const style = window.getComputedStyle(el);
                return {
                    display: style.display,
                    flexDirection: style.flexDirection,
                    listStyleType: style.listStyleType,
                    gap: style.gap
                }
            }
        """)

        print(f"nav-links styles: {nav_links_style}")

        # Get computed styles for nav-container
        nav_container_style = await page.eval_on_selector('.nav-container', """
            el => {
                const style = window.getComputedStyle(el);
                return {
                    display: style.display,
                    justifyContent: style.justifyContent
                }
            }
        """)

        print(f"nav-container styles: {nav_container_style}")

        # Take a screenshot specifically of the header area
        await page.locator('.navbar').screenshot(path='/home/jules/verification/debug_nav_bar.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
