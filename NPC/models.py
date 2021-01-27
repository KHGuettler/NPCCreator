from django.db import models

# Create your models here.


class Race(models.Model):
    raceName = models.CharField(max_length=50)

    def __str__(self):
        return self.raceName


class Class(models.Model):
    className = models.CharField(max_length=50)

    class HitDice(models.IntegerChoices):
        d6 = 6
        d8 = 8
        d10 = 10
        d12 = 12

    hitDice = models.IntegerField(choices=HitDice.choices, null=True)

    def __str__(self):
        return self.className


class Character(models.Model):
    name = models.CharField(max_length=100)

    npcClass = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Class', null=True)

    npcRace = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Race', null=True)

    def __str__(self):
        return self.name
