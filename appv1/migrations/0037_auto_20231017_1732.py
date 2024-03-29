# Generated by Django 3.2.1 on 2023-10-17 12:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0036_auto_20231017_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldetails',
            name='buylink1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='buylink2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='buylink3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='buylink4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('09608c83-6b97-4bf4-b458-34a4de5591b2'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('07287f20-e931-4539-84b6-c49c78d51beb'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='color_options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=7), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('140483ba-b7ed-45d5-b7b6-f2166408b0ce'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
