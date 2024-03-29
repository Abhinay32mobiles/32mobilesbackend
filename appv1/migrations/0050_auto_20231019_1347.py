# Generated by Django 3.2.1 on 2023-10-19 08:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0049_auto_20231019_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('7259cb51-bad6-4365-98b2-bbe3a7dc8c2f'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('8cdb786f-a863-4c05-ac12-680b710394ab'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('14b33cdb-30fb-4bef-bdf5-0135e2600a20'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
