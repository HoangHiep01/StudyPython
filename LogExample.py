import logging
logger = logging.getLogger(__name__)

# # Nothing log
# logger.propagate = False
# logger.info("From LogExample.py")


# create handler
streamh = logging.StreamHandler()
fileh = logging.FileHandler("file.log")

# level and format
streamh.setLevel(logging.WARNING)
fileh.setLevel(logging.ERROR)

formater = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
streamh.setFormatter(formater)
fileh.setFormatter(formater)

logger.addHandler(streamh)
logger.addHandler(fileh)

logger.warning("This is a warning")
logger.error("This is a error")