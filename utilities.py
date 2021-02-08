
import datetime
import time

START_TIME = time.time()

def get_uptime(start_time=START_TIME):
    return '{}'.format(datetime.timedelta(seconds=time.time() - start_time))

