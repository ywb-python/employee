# Generated by Django 3.2.19 on 2023-06-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_userinfo_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]
