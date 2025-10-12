from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def bbc_scrapper():
    url = 'https://www.bbc.com/news'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        html = page.content()
        browser.close()
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for main in soup.select('section.sc-92527ac1-1'):
        links = main.select('a.sc-8a623a54-0')        # all links in this section
        imgs = main.select('img.sc-5340b511-0')       # all images in this section
        h2_tags = main.select('h2.sc-9d830f2a-3')     # all headings in this section

        # iterate over the items together (zip limits to shortest list)
        for link, h2_tag, img_tag in zip(links[:2], h2_tags[:2], imgs[:2]):
            if img_tag:
                img_url = img_tag['src']
            else:
                continue
            if h2_tag:
                title = h2_tag.get_text(strip=True)
            else:
                continue
            href = link.get('href')
            if href and not href.startswith('https'):
                href = 'https://www.bbc.com' + href
            
            stories.append({'title': title, 'url': href, 'img_path': img_url})

    return stories
