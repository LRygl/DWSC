import datetime
import time

# Get the current date and time
current_datetime = datetime.datetime.now()


# Format the date and time components
# Get current datetime
def getCurrentDateTime():
    return current_datetime.strftime("%d-%m-%Y-%H-%M-%S")

# Get current date
def getCurrentDate():
    return current_datetime.strftime("%d-%m-%Y")

# Get current time seconds
def getCurrentTime():
    return current_datetime.strftime("%H-%M-%S")

# Get current time
def getTime():
    return time.time()