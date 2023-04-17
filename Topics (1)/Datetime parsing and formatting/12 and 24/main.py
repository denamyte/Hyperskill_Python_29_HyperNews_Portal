from datetime import datetime


formats = {24: '%H:%M',
           12: '%I:%M'}


def format_time(dt):
    for k, v in formats.items():
        print(f'{k}h {datetime.strftime(dt, v)}')
