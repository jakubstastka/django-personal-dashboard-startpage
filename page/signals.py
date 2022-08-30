from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from page.models import AccountSettings


@receiver(post_save, sender=User)
def create_account_settings(sender, instance, created, **kwargs):
    if created:
        AccountSettings.objects.create(user=instance)
