# Generated by Django 4.1.5 on 2023-01-27 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_choice_pass_choise_alter_question_pass_choise'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.question'),
        ),
        migrations.DeleteModel(
            name='FollowUpQuestion',
        ),
    ]