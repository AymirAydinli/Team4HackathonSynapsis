# Generated by Django 4.1.6 on 2023-02-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_filledquestionair_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='custom_answer',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
