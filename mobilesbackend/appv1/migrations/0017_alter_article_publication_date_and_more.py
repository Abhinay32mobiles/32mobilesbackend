# Generated by Django 4.2.6 on 2023-10-12 17:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0016_article_image_url_article_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('dd0f8f1b-f6d4-44a4-bc14-a6f763a3a0b7'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('e4b93b3e-53dd-40d6-bdd5-8e1ebf5db27e'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('c1cbdbb0-b550-463c-8a16-8747db2fe7c1'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
