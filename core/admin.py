from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Newsleter)
class NewsleterAdmin(admin.ModelAdmin):
    list_display=['email','create']

@admin.register(models.ContactUs)    
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','subject','created']
    
    
@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['phone','email','address']
