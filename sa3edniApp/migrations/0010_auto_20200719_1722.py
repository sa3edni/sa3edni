# Generated by Django 2.2 on 2020-07-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa3edniApp', '0009_auto_20200719_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='stream',
            field=models.CharField(choices=[('Scientific', 'Scientific'), ('Literature', 'Literature'), ('Any', 'Any')], max_length=25),
        ),
        migrations.AlterField(
            model_name='subject',
            name='stream',
            field=models.CharField(choices=[('Scientific', 'Scientific'), ('Literature', 'Literature'), ('Any', 'Any')], max_length=25),
        ),
    ]