# Generated by Django 3.2.1 on 2023-10-25 08:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0065_auto_20231022_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_desc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='back_camera_resolution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='currency',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='front_camera_resolution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='meta_desc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='youtubevideodetails',
            name='duration',
            field=models.CharField(default='10min', max_length=10),
        ),
        migrations.AddField(
            model_name='youtubevideodetails',
            name='meta_desc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='youtubevideodetails',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='youtubevideodetails',
            name='upload_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_title1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_title2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_title3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_title4',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('9e377312-a519-4788-bef8-25fe713eb1b6'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='camera_resolution',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('d448eea4-f388-4b32-a29e-600a34b0d3c9'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='operating_system',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('2fb592f9-9b97-43d1-a6d3-60d0fe7bb226'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
