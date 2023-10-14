# Generated by Django 4.2.6 on 2023-10-14 10:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0025_alter_modeldetails_brand_alter_modeldetails_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('fbe3ae22-f9ea-4a05-a50c-cea17ea2bcd1'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('df0293fa-0825-4e1c-8cd7-d16e79398251'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('7c90b6eb-1d75-446f-a204-14d4d2fdc08b'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
