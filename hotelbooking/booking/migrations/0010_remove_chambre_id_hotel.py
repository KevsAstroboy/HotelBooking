# Generated by Django 4.1.7 on 2023-03-25 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_remove_hotelphoto_id_chambre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chambre',
            name='id_hotel',
        ),
    ]