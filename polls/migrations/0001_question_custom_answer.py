# Generated by Django 4.1.6 on 2023-02-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', 'initial_data_load'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='custom_answer',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
