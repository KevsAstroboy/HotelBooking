# Generated by Django 4.1.7 on 2023-03-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pothole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pot_photo', models.FileField(upload_to='panthole')),
                ('pot_latitude', models.FloatField()),
                ('pot_longitude', models.FloatField()),
                ('status', models.TextField(default='VEHICULE')),
            ],
        ),
    ]
