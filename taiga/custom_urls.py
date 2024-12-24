#added by prince dated 24/12/2024

from django.urls import path
from taiga.projects.userstories.api import hourly_pending_work

urlpatterns = [
    path('hourly-pending-work/update/', hourly_pending_work, name='hourly_pending_work'),
]
