# Generated by Django 5.1.1 on 2024-10-22 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choices',
            new_name='choice_text',
        ),
    ]