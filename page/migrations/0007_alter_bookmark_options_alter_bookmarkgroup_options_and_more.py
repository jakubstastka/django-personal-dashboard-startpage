# Generated by Django 4.1 on 2022-08-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_board_options_board_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ('position',)},
        ),
        migrations.AlterModelOptions(
            name='bookmarkgroup',
            options={'ordering': ('position',)},
        ),
        migrations.AddField(
            model_name='bookmark',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookmarkgroup',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]