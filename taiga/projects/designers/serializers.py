# from django.conf import settings
from settings.constants import TAIGA_TICKET_URL, PLACEHOLDER_IMAGE_LINK
from taiga.base.api.serializers import ModelSerializer,SerializerMethodField
from taiga.projects.attachments.models import FinalAttachment
from taiga.projects.userstories.models import UserStory
from django.db.models import Q

class GetAdImageSerializer(ModelSerializer):
    image = SerializerMethodField("get_image")
    full_image = SerializerMethodField("get_full_image")
    ticket_url = SerializerMethodField("get_ticket_url")

    class Meta:
        model = UserStory
        fields = ['id', 'image', 'full_image', 'ticket_url']

    def get_image(self, obj):
        last_image = FinalAttachment.objects.filter(
            object_id=obj.id
        ).filter(
            Q(attached_file__iendswith=".jpg") |
            Q(attached_file__iendswith=".jpeg") |
            Q(attached_file__iendswith=".png")
        ).order_by('-created_date').first()
        # last_image = FinalAttachment.objects.filter(object_id=obj.id, attached_file__iendswith=".jpg").order_by(
        #     '-created_date').first()
        # return last_image.attached_file.url if last_image else PLACEHOLDER_IMAGE_LINK
        return last_image.attached_file.url if last_image else None

    def get_full_image(self, obj):
        # last_image = FinalAttachment.objects.filter(object_id=obj.id,attached_file__iendswith=".jpg").order_by('-created_date').first()
        # return last_image.attached_file.url if last_image else PLACEHOLDER_IMAGE_LINK
        return self.get_image(obj)

    def get_ticket_url(self, obj):

        if not obj.ref:
            return None

        return TAIGA_TICKET_URL+"project/adkrity/us/"+str(obj.ref)