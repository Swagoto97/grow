# Generated by Django 3.1 on 2021-07-29 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210729_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='wellcome_msg2',
        ),
    ]