# Generated by Django 4.1.6 on 2023-02-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='frequency_question',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pass_choice',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
