from django.urls import path
from .api import *

urlpatterns = [
    path('hourly-pending-work/update/', hourly_pending_work, name='hourly_pending_work'),
]
