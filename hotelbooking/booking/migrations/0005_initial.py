# Generated by Django 4.1.7 on 2023-03-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0004_delete_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_hotel', models.CharField(max_length=50)),
                ('logo_hotel', models.FileField(upload_to='tools')),
            ],
        ),
    ]
