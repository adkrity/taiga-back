from django.contrib import admin

from taiga.projects.custom_attributes.models import UserStoryCustomAttribute
from taiga.projects.models import Project, UserStoryStatus
from taiga.users.models import Role
from settings.constants import ADKRITY_PROJECT_ID
from . import models

class ProjectRoleUserStoryStatusMappingAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project":
            kwargs["queryset"] = Project.objects.filter(id=ADKRITY_PROJECT_ID)
        elif db_field.name == "role":
            kwargs["queryset"] = Role.objects.filter(project_id=ADKRITY_PROJECT_ID)
        elif db_field.name == "allowed_statuses":
            print("allowed statusesss")
            kwargs["queryset"] = UserStoryStatus.objects.filter(project_id=ADKRITY_PROJECT_ID)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "allowed_statuses":
            kwargs["queryset"] = UserStoryStatus.objects.filter(project_id=ADKRITY_PROJECT_ID)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class ProjectRoleUserStoryCustomAttributeMapping(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project":
            kwargs["queryset"] = Project.objects.filter(id=ADKRITY_PROJECT_ID)
        elif db_field.name == "role":
            kwargs["queryset"] = Role.objects.filter(project_id=ADKRITY_PROJECT_ID)
        elif db_field.name == "allowed_attributes":
            kwargs["queryset"] = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "allowed_attributes":
            kwargs["queryset"] = UserStoryCustomAttribute.objects.filter(project_id=ADKRITY_PROJECT_ID)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class UserStoryHourlyPendingWorkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.UserStoryHourlyPendingWork._meta.get_fields() if field.name not in (
    'id', 'onboarding_call', 'sent_for_approval', 'client_confirmation_pending', 'client_req_pending', 'missing_req')]


admin.site.register(models.UserStoryHourlyPendingWork, UserStoryHourlyPendingWorkAdmin)
admin.site.register(models.ProjectRoleUserStoryStatusMapping, ProjectRoleUserStoryStatusMappingAdmin)
admin.site.register(models.ProjectRoleUserStoryCustomAttributeMapping, ProjectRoleUserStoryCustomAttributeMapping)