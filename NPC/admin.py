from django.contrib import admin

from .models import *

# Register your models here.

# admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Class)
# admin.site.register(Proficiency)
admin.site.register(ProficiencyType)

@admin.register(Proficiency)
class ProficiencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'profType')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'npcRace', 'npcClass', 'npcLevel')