# Generated by Django 3.2.1 on 2023-10-22 12:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0057_auto_20231022_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('78f36866-ea65-4eef-81c3-3630b5ffc27f'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('a7d4198c-2ff4-4a44-b111-30dd8015d88d'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('72a3d694-6ee0-4637-8d51-1c34bffdfb25'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
