# Generated by Django 3.2.1 on 2023-10-21 10:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0054_auto_20231021_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sub_title1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_title2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_title3',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_title4',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('18c8a994-ef74-4267-8019-1cce1ac20dc5'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('4b1940c0-7c05-4622-bcbc-1deb7fc826eb'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('40990268-5736-4f09-bcbd-5daf3d66b202'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]