# Generated by Django 4.0.4 on 2022-11-21 12:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0007_alter_stepmodel_attachment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termtitle', models.CharField(max_length=50)),
                ('termdefinition', ckeditor.fields.RichTextField(max_length=500)),
                ('termstep', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('termspace', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='space.spacemodel')),
                ('termwriter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Term',
                'verbose_name_plural': 'Terms',
                'db_table': 'term_table',
            },
        ),
    ]