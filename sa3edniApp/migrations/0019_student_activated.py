# Generated by Django 2.2.7 on 2020-08-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa3edniApp', '0018_auto_20200803_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
