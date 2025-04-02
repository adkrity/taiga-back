from taiga.projects.models import Membership
from django.db.models import Count, Func, F, Value
from django.db.models.functions import Cast
from django.db.models.fields import CharField
from taiga.projects.history.models import HistoryEntry
from settings.constants import GET_MOVED_TICKETS_CONFIG
from taiga.base.utils.date import get_future_date

# added by prince dated 08/02/2024
def get_moved_tickets_data(project_id, role):

    users = list(Membership.objects.filter(project_id=project_id, role__name__iexact=role).values_list("user_id",flat=True))
    moved_tickets = (
        HistoryEntry.objects.filter(
            project_id=project_id,
            user__pk__in=users,  # Filter using the users list
            created_at__gt=get_future_date(-1),
            values_diff_cache__status__isnull=False
        )
    )

    statuses = GET_MOVED_TICKETS_CONFIG.get(role).get('to_status')
    final_moved_tickets = {}
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