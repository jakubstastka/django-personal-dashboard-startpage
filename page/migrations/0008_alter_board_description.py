# Generated by Django 4.1 on 2022-08-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_bookmark_options_alter_bookmarkgroup_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]