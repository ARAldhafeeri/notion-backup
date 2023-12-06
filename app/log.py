from asyncio.log import logger
import logging
import sys
logger = logging

logger.root.setLevel(logging.NOTSET)
logger.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("backup.log"),
        logging.StreamHandler(sys.stdout)
    ]
)