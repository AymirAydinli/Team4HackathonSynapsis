# Generated by Django 4.1.5 on 2023-01-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_choice_text_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='pass_choise',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pass_choise',
            field=models.BooleanField(null=True),
        ),
    ]
