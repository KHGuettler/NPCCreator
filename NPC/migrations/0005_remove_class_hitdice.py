# Generated by Django 3.1.5 on 2021-01-27 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NPC', '0004_class_hitdice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='hitDice',
        ),
    ]
