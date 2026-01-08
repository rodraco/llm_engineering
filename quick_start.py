import os
from dotenv import load_dotenv

#for Jupyther notebooks, use this:
#from IPython.display import Markdown, display

# for python scripts, use this:
from rich.console import Console
from rich.markdown import Markdown

from openai import OpenAI

load_dotenv(override=True)

# 0 for local model, 1 for deepseek-chat
env_to_load = 0

this_ai_model = None
this_base_url = None
this_api_key = None

local_ai_model = 'openai/gpt-oss-20b'
local_base_url = os.getenv('LMSTUDIO_BASE_URL')
local_api_key = os.getenv('LMSTUDIO_API_KEY')

deepseek_ai_model = 'deepseek-chat'
deepseek_base_url = os.getenv('DEEPSEEK_BASE_URL')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

match env_to_load:
    case 0:
        this_ai_model = local_ai_model
        this_base_url = local_base_url
        this_api_key = local_api_key
    case 1:
        this_ai_model = deepseek_ai_model
        this_base_url = deepseek_base_url
        this_api_key = deepseek_api_key
    case _:
        this_ai_model = local_ai_model
        this_base_url = local_base_url
        this_api_key = local_api_key 

llm = OpenAI(base_url=this_base_url, api_key=this_api_key)

system_prompt = """
    You are a helpfull assistant specialized in python coding, helping a begginer programmer understand code.
    Your answers will be detailed, explaining the technical terms if used.
"""

user_prompt = """
    Please explain what this code does and why:
    yield from {book.get("author") for book in books if book.get("author")}
"""
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

llm_response = llm.chat.completions.create(model=local_ai_model, messages=messages, temperature=0.5)

# For Juphyter notebooks, format the markdown with this:
#display(Markdown(llm_response.choices[0].message.content))

# For python script, format the markdown like this:
console = Console();
console.print(Markdown(llm_response.choices[0].message.content))
# or use it without formating
# print(llm_response.choices[0].message.content)