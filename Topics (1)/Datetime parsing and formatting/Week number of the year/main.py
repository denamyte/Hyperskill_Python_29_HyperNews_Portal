from datetime import datetime


def get_week_number(dt: datetime):
    return f'Week number: {dt.strftime("%U")}.'
