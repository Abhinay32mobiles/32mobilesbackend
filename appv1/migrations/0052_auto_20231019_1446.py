# Generated by Django 3.2.1 on 2023-10-19 09:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0051_auto_20231019_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeldetails',
            name='accessibility_features',
        ),
        migrations.RemoveField(
            model_name='modeldetails',
            name='sar_value',
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('8827c599-011c-4907-a414-fae6ad227dda'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('66b84efb-8674-439c-bec3-5ab591f2aba9'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('8692eb09-3d27-4927-b114-99769d36a4d5'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
