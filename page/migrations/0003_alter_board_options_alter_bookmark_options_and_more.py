# Generated by Django 4.1 on 2022-08-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_bookmark_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bookmarkgroup',
            options={},
        ),
        migrations.AddField(
            model_name='bookmarkgroup',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
