# Generated by Django 3.2.1 on 2023-10-18 06:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0042_auto_20231018_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('0c33678e-15c1-47fb-ba6b-8200b9616333'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('418bfb91-6bfd-45d2-877a-9a5ae7762edc'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('46ac28f1-153f-4a2e-a7b6-bff3629c7a69'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]