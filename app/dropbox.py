import dropbox
import json
from app.config import DROPBOX_ACCESS_TOKEN, DROPBOX_FOLDER
from app.utils import generate_file_name
from app.log import logger
def write_raw_json_to_dropbox(data):
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

    # Convert data to JSON format
    json_data = json.dumps(data, indent=2).encode("utf-8")

    file_path = f"/{DROPBOX_FOLDER}/{generate_file_name()}"
    # Upload JSON data to Dropbox
    with dbx.files_upload(json_data, file_path, mode=dropbox.files.WriteMode("overwrite")) as response:
        print("Uploaded:", response.name)
    logger.info("dropbox backup successful")


