# Generated by Django 4.1 on 2022-08-14 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_board_options_alter_bookmark_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ('created',)},
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ('created',)},
        ),
        migrations.AlterModelOptions(
            name='bookmarkgroup',
            options={'ordering': ('created',)},
        ),
    ]
