# Generated by Django 5.1.6 on 2025-03-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsleter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
            ],
            options={
                'verbose_name': 'عضو خبر نامه',
                'verbose_name_plural': 'اعضای خبر نامه',
            },
        ),
    ]
