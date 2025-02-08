#added by prince dated 24/12/2024

from django.urls import path
from taiga.projects.userstories.api import hourly_pending_work, delete_user_stories_reference_images

urlpatterns = [
    path('hourly-pending-work/update/', hourly_pending_work, name='hourly_pending_work'),
    path('delete-reference-images/<int:user_story_id>/', delete_user_stories_reference_images, name='delete_reference_images'),
]
