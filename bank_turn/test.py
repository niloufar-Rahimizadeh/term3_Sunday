from datetime import datetime


def get_time():
    dt = datetime.now()
    return dt.strftime("%H:%M:%S")


def get_date():
    dt = datetime.now()
    return dt.strftime("%d %b %Y")


print(get_date())