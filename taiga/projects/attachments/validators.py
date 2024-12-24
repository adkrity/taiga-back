# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

from django.utils.translation import gettext as _

from taiga.base.api import serializers
from taiga.base.api import validators
from taiga.base.exceptions import ValidationError
from taiga.base.fields import ListField

from . import models


class AttachmentValidator(validators.ModelValidator):
    attached_file = serializers.FileField(required=True)

    class Meta:
        model = models.Attachment
        fields = ("id", "project", "owner", "name", "attached_file", "size",
                  "description", "is_deprecated", "created_date",
                  "modified_date", "object_id", "order", "sha1", "from_comment")
        read_only_fields = ("owner", "created_date", "modified_date", "sha1")


# added by prince dated 20/12/2024
class FinalAttachmentValidator(validators.ModelValidator):
    attached_file = serializers.FileField(required=True)

    class Meta:
        model = models.FinalAttachment
        fields = ("id", "project", "owner", "name", "attached_file", "size",
                  "description", "is_deprecated", "created_date",
                  "modified_date", "object_id", "order", "sha1", "from_comment")
        read_only_fields = ("owner", "created_date", "modified_date", "sha1")
# added by prince end


class UpdateAttachmentsOrderBulkValidator(validators.Validator):
    content_type_id = serializers.IntegerField()
    object_id = serializers.IntegerField()
    after_attachment_id = serializers.IntegerField(required=False)
    bulk_attachments = ListField(child=serializers.IntegerField(min_value=1))

    def __init__(self, model, *args, **kwargs):
        self.model = model
        if not self.model:
            raise ValueError("A model must be provided to the validator.")
        super().__init__(*args, **kwargs)

    def validate_after_attachment_id(self, attrs, source):
        if (attrs.get(source, None) is not None
                and attrs.get("content_type_id", None) is not None
                and attrs.get("object_id", None) is not None):
            filters = {
                "content_type__id": attrs["content_type_id"],
                "object_id": attrs["object_id"],
                "id": attrs[source]
            }

            # changed by prince dated 20/12/2024

            # if not models.Attachment.objects.filter(**filters).exists():
            if not self.model.objects.filter(**filters).exists():
                raise ValidationError(_("Invalid attachment id to move after. The attachment must belong "
                                        "to the same item (epic, userstory, task, issue or wiki page)."))

        return attrs

    def validate_bulk_attachments(self, attrs, source):
        if (attrs.get("content_type_id", None) is not None
                and attrs.get("object_id", None) is not None):
            filters = {
                "content_type__id": attrs["content_type_id"],
                "object_id": attrs["object_id"],
                "id__in": attrs[source]
            }

            # changed by prince dated 20/12/2024

            # if models.Attachment.objects.filter(**filters).count() != len(filters["id__in"]):
            if self.model.objects.filter(**filters).count() != len(filters["id__in"]):
                raise ValidationError(_("Invalid attachment ids. All attachments must belong to the same "
                                        "item (epic, userstory, task, issue or wiki page)."))

        return attrs
