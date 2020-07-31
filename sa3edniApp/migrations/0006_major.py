# Generated by Django 2.2 on 2020-07-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa3edniApp', '0005_auto_20200714_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorName', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'major',
            },
        ),
    ]