# from django.conf import settings
from settings.constants import SUPPORT_TICKET_URL
from taiga.base.api.serializers import ModelSerializer,SerializerMethodField
from taiga.projects.attachments.models import FinalAttachment
from taiga.projects.userstories.models import UserStory

class GetAdImageSerializer(ModelSerializer):
    image = SerializerMethodField("get_image")
    full_image = SerializerMethodField("get_full_image")
    ticket_url = SerializerMethodField("get_ticket_url")

    class Meta:
        model = UserStory
        fields = ['id', 'image', 'full_image', 'ticket_url']

    def get_image(self, obj):
        last_image = FinalAttachment.objects.filter(object_id=obj.id).order_by('-created_date').first()
        # return get_ad_image_url(obj)
        return last_image.attached_file.url if last_image else None

    def get_full_image(self, obj):
        # from utils.image import get_cached_image_url

        # if not obj.attached_file:
        #     return None
        last_image = FinalAttachment.objects.filter(object_id=obj.id).order_by('-created_date').first()
        return last_image.attached_file.url if last_image else None

    def get_ticket_url(self, obj):

        if not obj.ref:
            return None

        return SUPPORT_TICKET_URL+"us/"+str(obj.ref)