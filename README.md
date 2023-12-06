# notion-backup
The following solution allow for scheduled backup , it creates two or one replica of notes on dropbox and google drive.

![alt text](https://github.com/ARAldhafeeri/notion-backup/blob/main/architecture.png)

## environment variables

BACKUP_EVERY=86400


NOTION_TOKEN= notion token


- google drive backup

GOOGLE_DRIVE_FOLDER_ID= folder id for google drive
credntials.json file must be in the same directory as the app


- dropbox backup -

DROPBOX_ACCESS_TOKEN= access token for dropbox
DROPBOX_FILE_PATH= folder path in dropbox

## google backup configuration
1. after floowing the following link to get credintials file
https://developers.google.com/drive/api/quickstart/python
2. place credentials.json in app directory, otherwise google drive backup will not work
3. must create a folder in google drive add the folder name to the environment variable `GOOGLE_DRIVE_FOLDER_ID`
4. open google drive account, share the folder with the email in the credintials.json file, of the service account

## dropbox backup configuration
1. go to the following page
https://www.dropbox.com/developers/apps
2. create an app, select scoped access App folder to restrict access to a specific folder
3. add the name of dropbox folder to the environment variable `DROPBOX_FOLDER_ID'

## notion configuration

1. go to https://www.notion.so/my-integrations
2. create a new integration
3. get notion api key and add it to the environment variable `NOTION_API_KEY`
4. add the database, pages you want to backup follow the following guide :
https://notionbackups.com/guides/automated-notion-backup-api

to backup pages :
Pick (or create) a Notion page.
Click on the ... More menu in the top-right corner of the page.
Scroll down to + Add Connections.
Search for your integration and select it.
Confirm the integration can access the page and all of its child pages.
## run the app

1. clone the repo
2. docker-compose --env-file .env build
3. docker-compose --env-file .env up -d

## run the back up mnaully
1. send get reqest to http://localhost:5000/backup