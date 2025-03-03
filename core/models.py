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
    
