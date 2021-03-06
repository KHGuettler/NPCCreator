# Generated by Django 3.1.5 on 2021-01-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NPC', '0013_auto_20210127_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProficiencieTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='proficiencies',
            name='Armour',
        ),
        migrations.AddField(
            model_name='proficiencies',
            name='armour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proficiencies',
            name='weapons',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ArmourProficiencies',
        ),
        migrations.AddField(
            model_name='proficiencietypes',
            name='Armour',
            field=models.ManyToManyField(related_name='profWeapons', to='NPC.Proficiencies'),
        ),
        migrations.AddField(
            model_name='proficiencietypes',
            name='Weapons',
            field=models.ManyToManyField(to='NPC.Proficiencies'),
        ),
    ]
