# Generated by Django 3.2.1 on 2023-10-17 12:05

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0038_auto_20231017_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('93c5bbd6-3ee3-4a9a-98ef-308224711daa'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('74acbc3e-e26a-49e1-9aeb-6cc37459a213'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='color_options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=7), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('9747d929-a096-4846-b1d5-de6cd4df84b2'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]