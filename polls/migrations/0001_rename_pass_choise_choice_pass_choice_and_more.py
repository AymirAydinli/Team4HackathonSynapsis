# Generated by Django 4.1.5 on 2023-01-30 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_question_question_parent_delete_followupquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='pass_choise',
            new_name='pass_choice',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pass_choise',
            new_name='pass_choice',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_children', to='polls.question'),
        ),
    ]
