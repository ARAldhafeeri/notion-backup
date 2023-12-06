from app.notion import read_notion_data
from app.log import logger
from app.google_docs import google_drive
from app.dropbox import write_raw_json_to_dropbox

def read_notion():
    """Reads the notion database and returns the data"""
    try: 
        data = read_notion_data()
        logger.info("Notion database read successfully")
        return data
    except Exception as e:
        logger.error("Error reading notion database")
        logger.error(e)
        return None

def backup_google_drive(data):
    """Authenticates google drive and returns the credentials"""
    try:
        google_drive(data)
        logger.info("Google drive backup successfully")
    except Exception as e:
        logger.error("backup error: google drive")
        logger.error(e)
        return None
    
def backup_dropbox(data):
    try:
        write_raw_json_to_dropbox(data)
        logger.info("dropbox backup successful")
    except Exception as e:
        logger.error("dropbox backup failed")
        logger.error(e)
