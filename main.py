from app.config import BACKUP_EVERY
import os
import time
import atexit
from flask import Flask

import sys

from apscheduler.schedulers.background import BackgroundScheduler

from app.log import logger

from apscheduler.schedulers.background import BackgroundScheduler

from app.tasks import (
    read_notion,
    backup_google_drive,
    backup_dropbox
)

from backup_now import run_now

# server
app = Flask(__name__)


#  global scheduler task

def tasks():
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



    




scheduler = BackgroundScheduler(
    job_defaults={'max_instances': 10}
)

scheduler.add_job(func=tasks, trigger="interval", seconds=BACKUP_EVERY)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route("/backup") 
def images():
    run_now()
    return "back up run"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0",  port=5000)

