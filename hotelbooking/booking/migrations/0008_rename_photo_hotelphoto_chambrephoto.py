# Generated by Django 4.1.7 on 2023-03-23 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_reservation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='HotelPhoto',
        ),
        migrations.CreateModel(
            name='ChambrePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='tools')),
                ('id_chambre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.chambre')),
            ],
        ),
    ]
