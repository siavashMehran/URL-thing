# Generated by Django 3.1.1 on 2021-02-20 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlReciever', '0007_auto_20210220_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_recieved',
            name='csrftoken',
        ),
    ]