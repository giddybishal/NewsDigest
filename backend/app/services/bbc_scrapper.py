from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def bbc_scrapper():
    url = 'https://www.bbc.com/news'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Scroll down to load lazy images
        page.evaluate("""
            () => {
                return new Promise(resolve => {
                    let totalHeight = 0;
                    const distance = 500;
                    const timer = setInterval(() => {
                        window.scrollBy(0, distance);
                        totalHeight += distance;
                        if(totalHeight >= document.body.scrollHeight){
                            clearInterval(timer);
                            resolve();
                        }
                    }, 300);
                });
            }
        """)
        time.sleep(2)  # give images a moment to load

        html = page.content()
        browser.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    stories = []
    seen_urls = set()

    for article in soup.select('div.fAWaua'):
        link_tag = article.select_one('a.huZCWi')
        img_tag = article.select_one('img.hLdNfA')
        h2_tag = article.select_one('h2.iCfgww')

        if not (link_tag and img_tag and h2_tag):
            continue

        title = h2_tag.get_text(strip=True)

        srcset = img_tag.get('srcset', '')
        if srcset:
            img_url = srcset.split(',')[3].strip().split()[0]
        else:
            img_url = img_tag.get('src') 

        href = link_tag.get('href')

        if href and not href.startswith('https'):
            href = 'https://www.bbc.com' + href

        if href in seen_urls:
            continue

        seen_urls.add(href)

        stories.append({'title': title, 'url': href, 'img_path': img_url})

        if len(stories) >= 20:
            break

    return stories
