# ---------------------------------------------------
# -- Advanced_Lessons => Add Logging to your Code --
# ---------------------------------------------------
# - Print out to Console or File
# - Prnt Logs of What Happens
# ---------------------------------------------------
# - Debug
# - Info
# - WARNING
# - ERROR
# - CRITICAL
# ------------------------
# name => Logging Module Give it to the Default Logger
# ---------------------------------------------------
# Basic Config
# - level => level of Severity
# - filename => File Name and Extention
# - mode => Mode of the File a => Append
# - format => Format for the Log Message
# ---------------------------------------------------
# getLogger => Return a Logger with the Specified Name

# It Didn't Work!!!!!!!

import logging

print(dir(logging))

logging.basicConfig(filename='my_app.log',
                    filemode='w',
                    format="%(asctime)s => %(name)s | %(levelname)s | %(message)s",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger('Ahmad')
my_logger.warning('Warning Message from me (New Logger)')
logging.critical('This is Critical Message')

logging.warning('This is Warning Message')