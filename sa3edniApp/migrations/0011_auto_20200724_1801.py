# Generated by Django 2.2 on 2020-07-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa3edniApp', '0010_auto_20200719_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='avgPrice',
        ),
        migrations.AddField(
            model_name='major',
            name='avgPrice',
            field=models.FloatField(default=0),
        ),
    ]