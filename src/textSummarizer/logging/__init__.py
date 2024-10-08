import os
import logging 
import sys


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_file_path = os.path.join(log_dir, "runninglogs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    
    handlers= [
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)  # logging to console too for debugging purposes
    ]
)

logger = logging.getLogger("textSummarizerLogger")