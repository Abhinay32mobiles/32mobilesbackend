# Generated by Django 3.2.1 on 2023-10-20 07:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0058_auto_20231020_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagsarticle',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='articles',
            field=models.ManyToManyField(related_name='tags', to='appv1.TagsArticle'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('7e50b9c3-d5a1-4adc-81ae-775ceb324e49'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('a552cf64-2f72-4d6c-8c79-04074e4f303b'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('a40d6568-d8d9-4015-b447-3fb5b089d845'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]