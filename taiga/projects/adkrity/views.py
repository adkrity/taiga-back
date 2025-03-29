from taiga.projects.history.models import HistoryEntry
from taiga.base.utils.date import get_future_date
from taiga.projects.models import Project, Membership
from . import models
from django.http import JsonResponse
from django.db.models import Q, Count, PositiveIntegerField

from taiga.projects.userstories.models import UserStory


# added by prince dated 08/02/2024
def get_moved_tickets_data(project_id, role):

    users = list(Membership.objects.filter(project_id=project_id, role__name__iexact=role).values_list("user_id",flat=True))
    print(users, "usersssssssss")

    moved_tickets = HistoryEntry.objects.filter(project_id=project_id, user__pk__in=users,
                                                created_at__gt=get_future_date(-1),
                                                values_diff_cache__status__isnull=False).values('user__pk').annotate(moved_ticket_count=Count('id'))
    print(moved_tickets, "??????????????", len(moved_tickets))
    return users


# added by prince
def hourly_pending_work(request):
    project = Project.objects.filter(name__iexact='adkrity').last()

    try:
        data = UserStory.objects.filter(~Q(tags__icontains="testing-ad-ignore"),project=project, is_closed=False).values('status__name').annotate(
                count=Count('id')).order_by('status').values('status__name', 'count')

        pending_work = {f.name: 0 for f in models.UserStoryHourlyPendingWork._meta.get_fields() if isinstance(f, PositiveIntegerField)}

        for item in data:
            field = item["status__name"].lower().strip().replace(' ','_')
            pending_work[field] = item['count']

        models.UserStoryHourlyPendingWork.objects.create(**pending_work)
        return JsonResponse({"Success":"Hourly Pending Work Updated Successfully."})
    except Exception as e:
        return JsonResponse({"Error": f"{e}"})
# added by prince end