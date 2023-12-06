from app.config import BACKUP_EVERY

from app.log import logger

from app.tasks import (
    read_notion,
    backup_google_drive,
    backup_dropbox
)

#  global scheduler task

def run_now():
    logger.info("Starting backup task")
    # notion
    logger.info("Reading notion database")
    data = read_notion()
    if not data:
        logger.error("Error reading notion database, aborting backup")
    logger.info("Starting google backup")
    backup_google_drive(data)
    logger.info("Starting dropbox backup")
    backup_dropbox(data)
    logger.info("scheduled task finished")

