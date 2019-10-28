#########################
######## Imports ########
#########################

import datetime, time
from email import utils

#########################
### Global Variables ####
#########################

weekday_lookup = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}

gbm_day = weekday_lookup['Wednesday']
hs_day  = weekday_lookup['Monday']
delivery_hour = 10 # AM

#########################
##### Date Formater #####
#########################

def dt_format(date):
    tuple = date.timetuple()
    timestamp = time.mktime(tuple)
    return utils.formatdate(timestamp) # Formats Date in RFC2822 Format

#########################
####### Now Date ########
#########################

def now_datetime():
    return dt_format(datetime.datetime.now() + datetime.timedelta(minutes=2))

#########################
####### GBM Date ########
#########################

def gbm_datetime():
    # Get and format next Wednesday, 10:00 AM
    dt = datetime.datetime.now()

    # If past 10 AM on Wednesday, get and format current time
    if(dt.weekday() == gbm_day and dt.hour > delivery_hour):
        return now_datetime()

    # Set day to Wednesday and time to 10:00 AM
    while(dt.weekday() != gbm_day):
        dt += datetime.timedelta(days=1)

    return dt_format(datetime.datetime(dt.year, dt.month, dt.day, delivery_hour, 0, 0, 0))

#########################
######## HS Date ########
#########################

def hs_datetime():
    # Get and format next Saturday, 10:00 AM
    dt = datetime.datetime.now()

    # If past 10 AM on Wednesday, get and format current time
    if dt.weekday() == hs_day and dt.hour > delivery_hour:
        return now_datetime()

    # Set day to Wednesday and time to 10:00 AM
    while(dt.weekday() != hs_day):
        dt += datetime.timedelta(days=1)

    return dt_format(datetime.datetime(dt.year, dt.month, dt.day, delivery_hour, 0, 0, 0))
