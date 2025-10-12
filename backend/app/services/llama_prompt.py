import ollama

system_prompt = """
You need to summarize the top new articles of bbc website of the given day as markdown
"""
user_prompt_prefix = """
Here are the top articles.
Provide a short summary of it.
"""
MODEL = 'llama3.1'

messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_prompt_prefix}
]

response = ollama.chat(model=MODEL, messages=messages, stream=True)
full_summary = ''
for chunk in response:
    full_summary += chunk['message']['content']
