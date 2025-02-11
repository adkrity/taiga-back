from django.utils import timezone
from datetime import timedelta

def _get_current_date():
    return timezone.now().date()


def _get_relative_date(no_of_days):
    return (_get_current_date() + timedelta(days=no_of_days))