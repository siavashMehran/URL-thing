# Generated by Django 3.1.5 on 2021-02-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlReciever', '0010_url_recieved_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_recieved',
            name='qr',
            field=models.ImageField(blank=True, upload_to='', verbose_name='qrs/q'),
        ),
    ]