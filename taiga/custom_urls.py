#added by prince dated 24/12/2024

from django.urls import path
from taiga.projects.userstories.api import  delete_user_stories_reference_images
from taiga.projects.adkrity.views import hourly_pending_work, send_moved_tickets_report_on_whatsapp, get_taiga_tickets_to_update_lost_data

urlpatterns = [
    path('hourly-pending-work/update/', hourly_pending_work, name='hourly_pending_work'),
    path('delete-reference-images/<int:user_story_id>/', delete_user_stories_reference_images, name='delete_reference_images'),
    path('send-moved-tickets-wp-report/', send_moved_tickets_report_on_whatsapp, name='send_whatsapp_report'),
    path('get-update-ticket-ids/', get_taiga_tickets_to_update_lost_data, name='get_taiga_tickets_to_update_lost_data'),
]
