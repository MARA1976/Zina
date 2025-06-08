# logger_config.py
import logging
import sys
from pathlib import Path

# Configuration automatique
log_dir = Path(__file__).parent / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "zina_bugs.log",
    format="[%(asctime)s] %(levelname)-8s - %(filename)s:%(lineno)d - %(message)s",
    level=logging.ERROR,
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Capture les crashes
sys.excepthook = lambda exc_type, exc_val, exc_tb: logging.critical(
    "Crash non géré", exc_info=(exc_type, exc_val, exc_tb)
)


# Raccourcis pratiques
def log_error(context, error):
    logging.error(f"{context} : {str(error)}", exc_info=True)


def log_warning(message):
    logging.warning(message)
