# Generated by Django 4.2.6 on 2023-10-12 09:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0005_alter_modeldetails_brand_alter_modeldetails_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tv',
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('a0436add-e9a5-42b9-91b2-2a17357cec06'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('15ece1d9-d6d8-4ad8-a25a-a7eb29e918d2'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
    ]
