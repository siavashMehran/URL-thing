# Generated by Django 3.1.1 on 2021-02-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlReciever', '0003_url_resieved_csrftoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_resieved',
            name='ShortAdress',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]