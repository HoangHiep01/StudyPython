import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
					datefmt="%d/%m/%y %H:%M:%S")

import LogExample


# by default only warning level or above will print on screen, use basicConfig to setup your
# recommended that read documentation
# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical message")

# Combinate logging with try-exception
# RotatigFileHandler control file's size
# TimeRotatingFileHandler
