# Generated by Django 2.2 on 2020-07-14 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sa3edniApp', '0006_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('maxGrade', models.FloatField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='major',
            options={},
        ),
        migrations.AddField(
            model_name='major',
            name='university',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sa3edniApp.University'),
        ),
    ]
