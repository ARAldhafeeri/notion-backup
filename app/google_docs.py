
from app.config import  GOOGLE_DRIVE_FOLDER_ID, GOOGLE_SCOPE
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account

from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from app.utils import generate_file_name
import os
import json

def google_drive(data):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("/app/app/token.json"):
        creds = Credentials.from_authorized_user_file("/app/app/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = service_account.Credentials.from_service_account_file(
            filename="/app/app/credentials.json", scopes=[GOOGLE_SCOPE]
            )
 

        service = build('drive', 'v3', credentials=creds)
        filename = generate_file_name()
        file_path = f"/app/app/{filename}"
        file_metadata = {
            'filename': filename,
            'parents': [GOOGLE_DRIVE_FOLDER_ID],
        }
        mediaa =  json.dumps(data).encode('utf-8')

        #  write file to disk
        with open(file_path, 'wb') as f:
            f.write(mediaa)
        media = MediaFileUpload(file_path, mimetype='application/json')

        service.files().create(
            supportsTeamDrives=True,
            body=file_metadata,
            media_body=media,
            media_mime_type='application/json',
            fields='id'
        ).execute()

        #  remove file from disk
        os.remove(file_path)
    
