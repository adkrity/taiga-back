# Generated by Django 3.2.19 on 2025-03-29 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_attributes', '0015_auto_20200615_0811'),
        ('users', '0033_auto_20211110_1526'),
        ('projects', '0067_auto_20201230_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStoryHourlyPendingWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.CreateModel(
            name='ProjectRoleUserStoryStatusMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_statuses', models.ManyToManyField(blank=True, to='projects.UserStoryStatus')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
            options={
                'unique_together': {('project', 'role')},
            },
        ),
        migrations.CreateModel(
            name='ProjectRoleUserStoryCustomAttributeMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_attributes', models.ManyToManyField(blank=True, to='custom_attributes.UserStoryCustomAttribute')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
            options={
                'unique_together': {('project', 'role')},
            },
        ),
    ]
