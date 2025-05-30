from taiga.projects.models import Membership
from django.db.models import Count, Func, F, Value, Q
from django.db.models.functions import Cast
from django.db.models.fields import CharField
from taiga.projects.history.models import HistoryEntry
from settings.constants import GET_MOVED_TICKETS_CONFIG
from taiga.base.utils.date import get_future_date, convert_to_local_time, get_today_date, get_time_range_for_date
from taiga.projects.userstories.models import UserStory


# added by prince dated 08/02/2024
def get_moved_tickets_data(project_id, role):

    users = list(Membership.objects.filter(project_id=project_id, role__name__iexact=role).values_list("user_id",flat=True))
    moved_tickets = (
        HistoryEntry.objects.filter(
            project_id=project_id,
            user__pk__in=users,  # Filter using the users list
            # created_at__gt=convert_to_local_time(get_future_date(-1)),
            created_at__gt=get_time_range_for_date(get_today_date())[0],
            values_diff_cache__status__isnull=False
        )
    )

    statuses = GET_MOVED_TICKETS_CONFIG.get(role).get('to_status')
    final_moved_tickets = {}

    if moved_tickets:
        for status in statuses:
            moved_tickets_results = list(moved_tickets.filter(values_diff_cache__status__1=status).annotate(
                user_name=Func(
                    Cast(F('user__name'), CharField()),
                    Value('"'),
                    Value(''),
                    function='REPLACE',
                    output_field=CharField()
                )
            ).values('user_name').annotate(moved_ticket_count=Count('id')).order_by('user_name'))
            final_moved_tickets[f"{status}"] = moved_tickets_results

    return final_moved_tickets


def get_pending_tickets_data(project_id, role):

    pending_work_status_list = GET_MOVED_TICKETS_CONFIG.get(role).get('pending_work')
    pending_work_data = list(UserStory.objects.filter(~Q(tags__icontains="testing-ad-ignore"), project=project_id, is_closed=False, status__name__in=pending_work_status_list).values(
        'status__name').annotate(count=Count('id')).order_by('status').values('status__name', 'count'))

    final_pending_work = {}
    for status_record in pending_work_data:
        final_pending_work[f"{status_record.get('status__name')}"] = status_record.get("count")

    return final_pending_work
