# Generated by Django 3.2.4 on 2021-07-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0004_alter_transport_supplies'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='license_number',
            field=models.CharField(default='ABJ345', max_length=30),
            preserve_default=False,
        ),
    ]
