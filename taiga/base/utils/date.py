from django.utils import timezone
from datetime import date, timedelta, datetime
from django.utils.timezone import make_aware
from pytz import timezone as pz_timezone
from django.conf import settings

def get_current_time():

    return timezone.now()

def get_current_timestamp():

    return timezone.now().timestamp()

def datetime_from_timestamp(timestamp):

    return datetime.fromtimestamp(int(timestamp))

def convert_to_local_time(date_time):
    settings_time_zone = pz_timezone(settings.TIME_ZONE)
    return date_time.astimezone(settings_time_zone)

def out_of_office_hrs(date_time):
    return convert_to_local_time(date_time).hour < 7 or convert_to_local_time(date_time).hour > 22

def add_support_working_hrs(add_time_in_hrs):

    if add_time_in_hrs > 6 and add_time_in_hrs < 24:
        return convert_to_local_time(get_future_date(1))

    if is_support_hours() and convert_to_local_time(timezone.now()).hour + add_time_in_hrs < 19:
        return convert_to_local_time(get_future_time(add_time_in_hrs*60*60))
    else:
        add_time_in_hrs = add_time_in_hrs - max((19 - convert_to_local_time(timezone.now()).hour), 0)
        final_time = convert_to_local_time(get_future_date(1))
        return final_time.replace(hour=10+add_time_in_hrs)

    return convert_to_local_time(get_future_date(add_time_in_hrs/24))


def is_support_hours():
    if get_current_time().weekday() == 6:
        return False

    return convert_to_local_time(timezone.now()).hour >= 10 and convert_to_local_time(timezone.now()).hour < 19

def get_date_diff(date):
    return (date - get_today_date()).days

def get_hours_diff(check_datetime, small_datetime=get_current_time()):
    time_diff = check_datetime - small_datetime
    remaining_hours = int(time_diff.days*24) + int(time_diff.seconds/3600)
    return remaining_hours

def is_morning():
    return timezone.localtime(timezone.now()).hour < 12

def is_evening():
    return timezone.localtime(timezone.now()).hour > 19

def get_today_date():
    # return convert_to_local_time(timezone.now()).date()
    return timezone.now().date()

def get_today_start_time():

    return convert_to_local_time(timezone.now()).replace(hour=0, minute=0, second=0)

def get_future_date(no_of_days):

    return (get_current_time() + timedelta(days=no_of_days))

def get_future_date_from_date(date, no_of_days):

    return (date + timedelta(days=no_of_days))

def get_future_time(no_of_seconds):

    return (get_current_time() + timedelta(seconds=no_of_seconds))

def get_future_time_from_datetime(date, no_of_seconds):

    return (date + timedelta(seconds=no_of_seconds))


def get_datetime_from_date(date):

    return


# "%Y-%m-%dT%H:%M:%S%z" -- facebook api
# '%Y-%m-%dT%H:%M:%S.%fZ'
# "%Y-%m-%d %H:%M:%S.%fZ"
def datetime_to_string(date_time, format='%d-%m-%Y %H:%M:%S'):
    if isinstance(date_time, str):
        return date_time

    return date_time.strftime(format)

def date_to_string(date, format='%d-%m-%Y'):

    if isinstance(date, str):
        return date

    try:
        return convert_to_local_time(date).strftime(format)
    except Exception as e:
        return date.strftime(format)


# "%Y-%m-%d %H:%M:%S.%fZ"
# '%d-%m-%Y'
# formats
# https://www.programiz.com/python-programming/datetime/strftime/
def date_from_string(date_string, format='%d/%m/%Y'):

    if not (isinstance(date_string, str)):
        return date_string

    datetime_obj = datetime.strptime(date_string, format)

    return make_aware(datetime_obj) if not datetime_obj.tzname() else datetime_obj

def seconds_to_min_string(no_of_seconds):

    # datetime_obj = datetime.timedelta(seconds=no_of_seconds)
    mins = int(no_of_seconds/60)
    secs = no_of_seconds%60
    if mins < 1:
        return str(secs) + " sec"

    return str(mins)+" mins " + str(secs) + " sec"



def get_max_date_from_list(datetime_list):

    return max(d for d in datetime_list if isinstance(d, datetime))

def get_last_month_date_range(for_date=None):

    if not for_date:
        for_date = timezone.now()

    last_day_of_prev_month = for_date.replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = for_date.replace(day=1) - timedelta(days=last_day_of_prev_month.day)

    return convert_to_local_time(start_day_of_prev_month).replace(hour=0, minute=0, second=0), convert_to_local_time(last_day_of_prev_month).replace(hour=23, minute=59, second=59)

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - timedelta(days=next_month.day)

def get_this_month_date_range(for_date=None):

    if not for_date:
        start_day_of_this_month = timezone.now().replace(day=1)
        return convert_to_local_time(start_day_of_this_month).replace(hour=0, minute=0, second=0), convert_to_local_time(timezone.now())

    start_day_of_the_month = for_date.replace(day=1)
    last_day_of_the_month = last_day_of_month(for_date)
    # last_day_of_the_month = for_date.replace(day=1) - timedelta(days=1)
    # start_day_of_the__month = for_date.replace(day=1) - timedelta(days=last_day_of_the_month.day)

    return convert_to_local_time(start_day_of_the_month).replace(hour=0, minute=0, second=0), convert_to_local_time(last_day_of_the_month).replace(hour=23, minute=59, second=59)

def get_time_range_for_date(date):
    datetime_obj = datetime.combine(date, datetime.min.time())
    return convert_to_local_time(datetime_obj).replace(hour=0, minute=0, second=0), convert_to_local_time(datetime_obj).replace(hour=23, minute=59, second=59)


def get_next_month_date_range(for_date=timezone.now()):
    next_month = for_date.replace(day=28) + timedelta(days=4)
    return get_this_month_date_range(next_month)
