from app.config import NOTION_TOKEN

import requests 


NOTION_API_URL = f"https://api.notion.com/v1/search"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2021-05-11", 
    'Content-Type': 'application/json',
}

def read_notion_data():
    data = []
    response = requests.post(NOTION_API_URL, headers=NOTION_HEADERS)
    for block in response.json()['results']:
        child_blocks = requests.get(
            f'https://api.notion.com/v1/blocks/{block["id"]}/children',
            headers=
            NOTION_HEADERS,
        )
        data.append(child_blocks.json())
    return data