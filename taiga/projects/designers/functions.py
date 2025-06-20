import random
from django.http import JsonResponse

def get_random_obj_list(queryset, size):
    total = queryset.count()
    if total <= size:
        return list(queryset)

    pks = list(queryset.values_list("pk", flat=True))

    sampled_pks = random.sample(pks, size)
    objs = list(queryset.filter(pk__in=sampled_pks))
    random.shuffle(objs)

    return list(objs)


def success_json_response(result_json):
    return JsonResponse(result_json, safe=False)