from django.db import models
from taiga.projects.adkrity.models import BaseModel, MediaTypeMaster, TagMaster
from settings.constants import DESIGNER_FONT_FOLDER, DESIGNER_MEDIA_FOLDER


class DesignerFontMaster(BaseModel):
    name =  models.CharField(max_length=100, unique=True)
    font_file =  models.FileField(upload_to=DESIGNER_FONT_FOLDER, default=None, blank = True, null = True)

    is_active = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class DesignerMediaCategories(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class DesignerMedia(BaseModel):
    category = models.ForeignKey(DesignerMediaCategories, on_delete=models.PROTECT)
    source = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False, db_index=True)

    media_type = models.ForeignKey(MediaTypeMaster, on_delete=models.PROTECT, db_index=True, null=True, blank=True)
    image = models.ImageField(upload_to=DESIGNER_MEDIA_FOLDER, default=None, blank = True, null = True, verbose_name="Image (Jpg or Png)")
    media = models.FileField(
        upload_to=DESIGNER_MEDIA_FOLDER,
        default=None,
        blank=True,
        null=True,
        verbose_name="Vector (Psd)"
    )

    tags = models.ForeignKey(TagMaster, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.category.name