# Generated by Django 3.2.19 on 2024-12-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0021_auto_20201202_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStoryHourlyPendingWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('onboarding_call', models.PositiveIntegerField(default=0)),
                ('client_req_pending', models.PositiveIntegerField(default=0)),
                ('missing_req', models.PositiveIntegerField(default=0)),
                ('client_req_done', models.PositiveIntegerField(default=0)),
                ('req_review_pending', models.PositiveIntegerField(default=0)),
                ('design_req_done', models.PositiveIntegerField(default=0)),
                ('in_designing', models.PositiveIntegerField(default=0)),
                ('design_done', models.PositiveIntegerField(default=0)),
                ('sent_for_approval', models.PositiveIntegerField(default=0)),
                ('client_changes', models.PositiveIntegerField(default=0)),
                ('client_confirmation_pending', models.PositiveIntegerField(default=0)),
                ('design_approved', models.PositiveIntegerField(default=0)),
                ('ready_to_publish', models.PositiveIntegerField(default=0)),
                ('ad_support', models.PositiveIntegerField(default=0)),
                ('ad_issues', models.PositiveIntegerField(default=0)),
                ('integration_issues', models.PositiveIntegerField(default=0)),
                ('integration_pending', models.PositiveIntegerField(default=0)),
                ('ad_published', models.PositiveIntegerField(default=0)),
                ('ad_changes', models.PositiveIntegerField(default=0)),
                ('need_optimization', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
