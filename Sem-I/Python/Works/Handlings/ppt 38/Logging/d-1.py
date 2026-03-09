
import logging
logging.basicConfig(level=logging.WARNING)
logging.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")



#Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
#logging.debug() - Detailed information, typically of interest only when diagnosing problems.
#logging.info() - Confirmation that things are working as expected. 
#logging.warning() - An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
#logging.error() - Due to a more serious problem, the software has not been able to perform some function.
#logging.critical() - A very serious error, indicating that the program itself may be unable
