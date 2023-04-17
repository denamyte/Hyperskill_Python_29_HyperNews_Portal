from datetime import datetime


def get_weekday(dt: datetime):
    return dt.strftime('%A')
