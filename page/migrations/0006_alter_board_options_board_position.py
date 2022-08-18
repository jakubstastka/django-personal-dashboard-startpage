# Generated by Django 4.1 on 2022-08-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_board_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ('position',)},
        ),
        migrations.AddField(
            model_name='board',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
