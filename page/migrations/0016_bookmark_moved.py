# Generated by Django 4.1 on 2022-09-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_bookmarkgroup_moved'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='moved',
            field=models.BooleanField(default=False),
        ),
    ]