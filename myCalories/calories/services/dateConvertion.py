import datetime


def date_to_string(o):
    if isinstance(o, datetime.date):
        return o.__str__()[:10]


def string_to_date(o):
    return datetime.datetime.strptime(o, '%Y-%m-%d')


def yesterday(date):
    return date - datetime.timedelta(1)


def tommorow(date):
    return date + datetime.timedelta(1)
