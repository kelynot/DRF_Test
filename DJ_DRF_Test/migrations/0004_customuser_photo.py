# Generated by Django 5.0.6 on 2024-06-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ_DRF_Test', '0003_alter_task_employee_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]
