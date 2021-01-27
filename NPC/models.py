from django import forms
from django.core import validators
from django.db import models

# Create your models here.



class ProficiencyType(models.Model):
    profType = models.CharField(max_length=100)

    class Meta:
        ordering = ['profType']

    def __str__(self):
        return self.profType

class Proficiency(models.Model):
    profType = models.ForeignKey(ProficiencyType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['profType']

    def __str__(self):
        return self.name + self.profType.__str__()

class Race(models.Model):
    raceName = models.CharField(max_length=50)

    def __str__(self):
        return self.raceName


class Class(models.Model):
    class Meta:
        ordering = ['className']

    className = models.CharField(max_length=50)

    class HitDice(models.IntegerChoices):
        d6 = 6
        d8 = 8
        d10 = 10
        d12 = 12

    hitDice = models.IntegerField(choices=HitDice.choices, null=True)

    proficiencies = models.ManyToManyField(ProficiencyType)



    def __str__(self):
        return self.className





class Character(models.Model):
    name = models.CharField(max_length=100)

    npcRace = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Race', null=True)

    npcClass = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Class', null=True)

    npcLevel = models.IntegerField(
        default=1,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(20),
        ]
    )

    def __str__(self):
        return self.name
