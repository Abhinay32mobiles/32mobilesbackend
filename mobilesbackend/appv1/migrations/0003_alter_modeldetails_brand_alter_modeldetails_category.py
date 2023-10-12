# Generated by Django 4.2.6 on 2023-10-12 06:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0002_article_brands_article_category_article_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('ddce567b-cef6-4d87-9d7f-eb0c7b8c9f10'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('7fe458c9-6831-4d04-97f6-e6f69abe3b3f'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
    ]
