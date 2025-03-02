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
    
