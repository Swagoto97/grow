# Generated by Django 3.1 on 2021-07-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20210730_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sunday',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
