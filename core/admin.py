from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Newsleter)
class NewsleterAdmin(admin.ModelAdmin):
    list_display=['email','create']