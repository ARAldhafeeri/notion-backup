from datetime import datetime
import uuid
import re

def generate_file_name():
    """returns in format fro google drive and dropbox"""
    today_date = datetime.today().strftime("%Y-%m-%d")
    unique_id = uuid.uuid4().hex
    sanitized_date = re.sub(r'[^a-zA-Z0-9]', '_', today_date)
    return f"{sanitized_date}_{unique_id}.json"