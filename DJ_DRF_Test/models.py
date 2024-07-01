from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Заказчик'),
        ('employee', 'Сотрудник'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=False, null=True, verbose_name="Фотография")


class Task(models.Model):
    created_by = models.ForeignKey(CustomUser, related_name='tasks_created', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, related_name='tasks_assigned', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    report = models.TextField(blank=True)
    STATUS_CHOICES = (
        ('PENDING', 'Ожидает исполнителя'),
        ('IN_PROGRESS', 'В процессе'),
        ('COMPLETED', 'Выполнена'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')


@receiver(pre_save, sender=Task)
def update_task_status(sender, instance, **kwargs):
    if instance.assigned_to:
        instance.status = 'IN_PROGRESS'
    if instance.status == 'COMPLETED':
        instance.report = models.TextField(blank=False)
