from dotenv import load_dotenv
import os
from  bs4 import BeautifulSoup
import requests

def bbc_summarizer(url):

    load_dotenv()
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ['HF_API_TOKEN']}",
    }

    system_prompt = """
    You need to summarize the news article of bbc website of the given day as pretty html. Be sure to do everything using html tags only and nothing else, use html tags for fonting too but keep it formal text so no extra colors or unncessarily varied font sizes or etc, make it like a formal document with proper spacing and font with just html tags. Your reply will be rendered in html in frontend of my website. "Use only standard HTML tags: <h1>-<h6> for headings, <p> for paragraphs, <b> for bold, <i> for italics. Do not include CSS or inline styles. Do not add colors or font sizes. Return well-formatted HTML that can be directly rendered in the frontend. Also, only return relevant news articles snippet nothing irrelevant part of the bbc news. so no other headlines and such, strictly news summary only in well formatted html."

    """
    user_prompt_prefix = """
    This is the scrapped data from the news article. Now summarize it the best you can.
    """
    MODEL = 'deepseek-ai/DeepSeek-V3.1:novita'

    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    content_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
    text = " ".join(tag.get_text(strip=True) for tag in content_tags)

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt_prefix+text}
    ]

    response = requests.post(API_URL, headers=headers, json={
        "messages": messages,
        "model": MODEL
    })

    # Convert to JSON
    response_json = response.json()

    # Debugging help
    if response.status_code != 200:
        raise Exception(f"Hugging Face API error: {response_json}")

    # Extract summary text
    summary = response_json["choices"][0]["message"]["content"]

    return {"summary": summary, "source_url": url}

if __name__ == '__main__':
    print(bbc_summarizer('https://www.bbc.com/news/live/cx2r2z0gyp7t')['summary'])
