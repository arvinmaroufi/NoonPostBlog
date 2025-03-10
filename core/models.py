from django.db import models

# Create your models here.

class Newsleter(models.Model):
    email=models.EmailField(unique=True, verbose_name="ایمیل")
    create=models.DateTimeField(auto_now_add=True , verbose_name="تاریخ عضویت")

    class Meta:
        verbose_name="عضو خبر نامه"
        verbose_name_plural="اعضای خبر نامه"
    
    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="نام کامل")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ارسال")
    
    class Meta:
        verbose_name="تماس با ما"
        verbose_name_plural="تماس با ما"
        
    def __str__(self):
        return self.full_name
    


class SiteSetting(models.Model):
    about_us = models.TextField(verbose_name="متن درباره ما",blank=True,null=True)
    contact_us = models.TextField(verbose_name="متن تماس با ما",blank=True,null=True)
    copy_right = models.CharField(verbose_name="متن کپی رایت",max_length=100)
    phone = models.CharField(verbose_name="شماره تماس",blank=True,null=True,max_length=15)
    address = models.CharField(verbose_name="آدرس",blank=True,null=True,max_length=100)
    email = models.EmailField(verbose_name="ایمیل",blank=True,null=True,max_length=50)
    facebook_link = models.CharField(verbose_name="لینک فیسبوک",blank=True,null=True,max_length=200,default='https://facebook.com/username')
    instagram_link = models.CharField(verbose_name="لینک اینستاگرام",blank=True,null=True,max_length=200,default='https://instagram.com/username')
    telegram_link = models.CharField(verbose_name="لینک تلگرام",blank=True,null=True,max_length=200,default='https://t.me/username')
    
    class Meta:
        verbose_name="تنظیمات سایت"
        verbose_name_plural="تنظیمات سایت"
        
    
    
