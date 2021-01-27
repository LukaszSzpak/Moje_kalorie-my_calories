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


def get_week(date):
    weekday = date.weekday()
    start_delta = datetime.timedelta(days=weekday)
    start_of_week = date - start_delta
    week_dates = []

    for day in range(7):
        week_dates.append(start_of_week + datetime.timedelta(days=day))

    return week_dates


def get_prev_week(date):
    last_week_date = date - datetime.timedelta(7)
    return get_week(last_week_date)


def get_next_week(date):
    next_week_date = date + datetime.timedelta(7)
    return get_week(next_week_date)


def date_list_to_string_list(date_list):
    result_list = []
    for date in date_list:
        result_list.append(date_to_string(date))

    return result_list
