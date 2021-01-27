# Generated by Django 3.1.5 on 2021-01-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NPC', '0006_class_hitdice'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitDice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='class',
            name='hitDice',
        ),
        migrations.AddField(
            model_name='class',
            name='hitDice',
            field=models.ManyToManyField(null=True, to='NPC.HitDice'),
        ),
    ]
