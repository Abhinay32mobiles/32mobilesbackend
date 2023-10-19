# Generated by Django 3.2.1 on 2023-10-19 09:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0056_auto_20231019_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldetails',
            name='antutu_score',
            field=models.PositiveIntegerField(blank=True, null=True, default=100000),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='antutu_desc',
            field=models.TextField(blank=True, null=True, default="about the benchmarkings")
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('38bb5bb8-fa4b-4393-8a58-39448aca20a4'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('6b82b1e2-df1a-4a29-95d5-4bb4871c2225'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('64266498-2ffc-41cf-a05f-f0bdac11830b'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]