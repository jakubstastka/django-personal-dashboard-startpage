from django.db import models


class Positioned(models.Model):
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ('position',)


class Timestamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("created",)


class Named(models.Model):
    name = models.TextField(default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
