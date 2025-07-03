from django.db import models
from django.utils.translation import gettext_lazy as _
from taiga.projects.models import Project, UserStoryStatus
from taiga.users.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("created date"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("modified date"))

    class Meta:
        abstract = True


class AdKrityTagMaster(BaseModel):

    name = models.CharField(max_length = 100, db_index=True, unique=True)
    category = models.CharField(max_length = 255, null=True, blank=True)
    is_approved = models.BooleanField(default=False, db_index=True)
    meta_data = models.JSONField(default=None, blank = True, null = True)

    added_by = models.ForeignKey(User, on_delete=models.PROTECT, default=None, blank = True, null = True, db_index=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.name)


class MediaTypeMaster(BaseModel):
    type = models.CharField(max_length = 20, db_index=True)
    weight = models.FloatField(default=0)

    def __str__(self):
        return '%s' % (self.type)


# Mapping for allowed statuses per role in a project
class ProjectRoleUserStoryStatusMapping(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey('users.Role', on_delete=models.CASCADE)
    allowed_statuses = models.ManyToManyField(UserStoryStatus, blank=True)

    class Meta:
        unique_together = ('project', 'role')

    def __str__(self):
        return f"{self.project} - {self.role} statuses"


# Mapping for allowed custom attributes per role in a project
class ProjectRoleUserStoryCustomAttributeMapping(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey('users.Role', on_delete=models.CASCADE)
    allowed_attributes = models.ManyToManyField('custom_attributes.UserStoryCustomAttribute', blank=True)

    class Meta:
        unique_together = ('project', 'role')

    def __str__(self):
        return f"{self.project} - {self.role} Custom attributes"


class UserStoryHourlyPendingWork(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    onboarding_call = models.PositiveIntegerField(default=0)
    client_req_pending = models.PositiveIntegerField(default=0)
    missing_req = models.PositiveIntegerField(default=0)
    client_req_done = models.PositiveIntegerField(default=0)
    req_review_pending = models.PositiveIntegerField(default=0)
    design_req_done = models.PositiveIntegerField(default=0)
    in_designing = models.PositiveIntegerField(default=0)
    design_done = models.PositiveIntegerField(default=0)
    sent_for_approval = models.PositiveIntegerField(default=0)
    client_changes = models.PositiveIntegerField(default=0)
    client_confirmation_pending = models.PositiveIntegerField(default=0)
    design_approved = models.PositiveIntegerField(default=0)
    ready_to_publish = models.PositiveIntegerField(default=0)
    ad_support = models.PositiveIntegerField(default=0)
    ad_issues = models.PositiveIntegerField(default=0)
    integration_issues = models.PositiveIntegerField(default=0)
    integration_pending = models.PositiveIntegerField(default=0)
    ad_published = models.PositiveIntegerField(default=0)
    ad_changes = models.PositiveIntegerField(default=0)
    need_optimization = models.PositiveIntegerField(default=0)