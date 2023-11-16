# Generated by Django 3.2.1 on 2023-10-22 12:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0055_auto_20231021_1627'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('67b8d9ab-37ca-4453-ae9f-4e9f986c6332'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('1a0f7ca7-11f6-486f-a1c4-f7326eb49825'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('6c5098fc-edfb-44eb-a433-b68bb8dbbdab'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]