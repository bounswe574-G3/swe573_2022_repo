# Generated by Django 4.0.4 on 2022-05-22 16:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0005_alter_messagemodel_memberspace'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steptitle', models.CharField(max_length=50)),
                ('stepcontent', ckeditor.fields.RichTextField(max_length=250)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('stepcreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step', to=settings.AUTH_USER_MODEL)),
                ('stepspace', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='space.spacemodel')),
            ],
            options={
                'verbose_name': 'Steps',
                'verbose_name_plural': 'Steps',
                'db_table': 'step_table',
            },
        ),
    ]
