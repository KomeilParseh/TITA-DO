# Generated by Django 3.1.4 on 2020-12-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201203_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='TODO',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='question_text',
            new_name='TODO',
        ),
    ]
