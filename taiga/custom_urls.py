#added by prince dated 24/12/2024

from django.urls import path
from taiga.projects.userstories.api import  delete_user_stories_reference_images
from taiga.projects.adkrity.views import hourly_pending_work, send_report_on_whatsapp

urlpatterns = [
    path('hourly-pending-work/update/', hourly_pending_work, name='hourly_pending_work'),
    path('delete-reference-images/<int:user_story_id>/', delete_user_stories_reference_images, name='delete_reference_images'),
    path('send-wp-report/', send_report_on_whatsapp, name='send_whatsapp_report'),
]
