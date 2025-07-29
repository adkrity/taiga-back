import requests
from taiga.projects.models import Project
from taiga.projects.adkrity import models
from django.http import JsonResponse
from django.db.models import Q, Count, PositiveIntegerField

from taiga.projects.userstories.models import UserStory
from settings.constants import SERVER_APP_BASE_URL, ADKRITY_PROJECT_ID, GET_MOVED_TICKETS_CONFIG, CUSTOM_ATTRIBUTE_IDS
from taiga.projects.adkrity.functions import get_moved_tickets_data, get_pending_tickets_data, get_user_stories_ids_for_updation
from taiga.base.utils.request import make_post


# https://task.adkrity.com/api/v1/send-wp-report?role=Design
# send taiga moved tickets reports on wp (requirement by JK).
def send_moved_tickets_report_on_whatsapp(request):

    role = request.GET.get('role', 'Design')
    final_moved_tickets = get_moved_tickets_data(ADKRITY_PROJECT_ID,role)
    pending_tickets_data = get_pending_tickets_data(ADKRITY_PROJECT_ID,role)

    # {'Design Done': [{'user_name': 'Ankit Makwana', 'moved_ticket_count': 2},
    #                  {'user_name': 'prince', 'moved_ticket_count': 1}],
    #  'In Designing': [{'user_name': 'Ankit Makwana', 'moved_ticket_count': 3}]} sample final_moved_tickets
#================================================ sample final_moved_tickets ===================================================#

    # {'Design Req Done': 2}
# ================================================ sample pending_tickets_data ===================================================#

    message_lines = []
    if final_moved_tickets:
        message_lines = ["The below is the list of moved tickets by your team members:"]
        for status, user_entries in final_moved_tickets.items():
            message_lines.append(f"{status}:")
            for entry in user_entries:
                user_name = entry.get('user_name')
                count = entry.get('moved_ticket_count', 0)
                message_lines.append(f"*{user_name}*: {count} ticket{'s' if count != 1 else ''} moved.")

    message_lines.append("Pending Tickets:")
    for status, count in pending_tickets_data.items():
        message_lines.append(f"*{status}*: {count} tickets remaining")

    whatsapp_msg_string = " ".join(message_lines)
    print(whatsapp_msg_string, "WhatsApp report message string.", sep='\n')
    params_list = [
        {
            "type": "text",
            "text": whatsapp_msg_string
        },
    ]

    payload = {
        "template_name": "taiga_moved_tickets",
        "message": whatsapp_msg_string,
        "params_list": params_list,
        "users_wp_number": GET_MOVED_TICKETS_CONFIG.get(role).get('team_lead_wp_number'),
    }
    api_url = f"{SERVER_APP_BASE_URL}marketing/send-wp-msg/"

    try:
        headers = {"Content-Type": "application/json"}
        api_response, success = make_post(api_url, payload, headers=headers)
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": f"{success}", "api_response": api_response})


# added by prince
def hourly_pending_work(request):
    project = Project.objects.filter(name__iexact='adkrity').last()

    try:
        data = UserStory.objects.filter(~Q(tags__icontains="testing-ad-ignore"),project=project, is_closed=False).values('status__name').annotate(
                count=Count('id')).order_by('status').values('status__name', 'count')

        pending_work = {f.name: 0 for f in models.UserStoryHourlyPendingWork._meta.get_fields() if isinstance(f, PositiveIntegerField)}

        for item in data:
            field = item["status__name"].lower().strip().replace(' ','_')
            if field in pending_work:
                pending_work[field] = item['count']
            # else:
            #     print(f"Warning: Status '{item['status__name']}' doesn't match any field in UserStoryHourlyPendingWork")
        print(pending_work, "Pending work")
        models.UserStoryHourlyPendingWork.objects.create(**pending_work)
        return JsonResponse({"Success":"Hourly Pending Work Updated Successfully."})
    except Exception as e:
        return JsonResponse({"Error": f"{e}"})
# added by prince end


def get_taiga_tickets_to_update_lost_data(request):
    user_stories = get_user_stories_ids_for_updation()
    return JsonResponse({'user_stories_ids': user_stories})