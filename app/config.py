from dotenv import dotenv_values

config = dotenv_values(".env")

# backup config
BACKUP_EVERY = int(config.get("BACKUP_EVERY", 86400))

# notion 
NOTION_TOKEN = config.get("NOTION_TOKEN")

# google drive

GOOGLE_DRIVE_FOLDER_ID = config.get("GOOGLE_DRIVE_FOLDER_ID")
GOOGLE_SCOPE = config.get("GOOGLE_SCOPE")

# dropbox

DROPBOX_ACCESS_TOKEN = config.get("DROPBOX_ACCESS_TOKEN")
DROPBOX_FOLDER = config.get("DROPBOX_FOLDER")
