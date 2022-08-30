from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from page.models import AccountSettings


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            try:
                AccountSettings.objects.create(user=user)
            except IntegrityError:
                print("Already exists, skipping")
                pass
