import ollama
from  bs4 import BeautifulSoup
import requests

def bbc_summarizer(url):

    system_prompt = """
    You need to summarize the news article of bbc website of the given day as pretty html. Be sure to do everything using html tags only and nothing else, use html tags for fonting too but keep it formal text so no extra colors or unncessarily varied font sizes or etc, make it like a formal document with proper spacing and font with just html tags. Your reply will be rendered in html in frontend of my website. "Use only standard HTML tags: <h1>-<h6> for headings, <p> for paragraphs, <b> for bold, <i> for italics. Do not include CSS or inline styles. Do not add colors or font sizes. Return well-formatted HTML that can be directly rendered in the frontend."

    """
    user_prompt_prefix = """
    This is the scrapped data from the news article. Now summarize it the best you can.
    """
    MODEL = 'deepseek-v3.1:671b-cloud'

    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    content_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
    text = " ".join(tag.get_text(strip=True) for tag in content_tags)

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt_prefix+text}
    ]

    response = ollama.chat(model=MODEL, messages=messages, stream=False)
    return {'summary': response['message']['content'], 'source_url': url}

if __name__ == '__main__':
    print(bbc_summarizer('https://www.bbc.com/news/live/cx2r2z0gyp7t')['summary'])
