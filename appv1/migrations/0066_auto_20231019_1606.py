# Generated by Django 3.2.1 on 2023-10-19 10:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0065_auto_20231019_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='biometric_security',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='bluetooth_version',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('6e7acc5e-52f4-4e16-9276-eb340abf6519'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='buylink1',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='buylink2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='buylink3',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='buylink4',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('d2c6e47a-a175-4023-98eb-29c58c967671'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='dust_resistance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='img1',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='img2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='img3',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='img4',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='network_connectivity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='sim_card_slots',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='water_resistance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='wi_fi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('625da6c5-b12f-454f-ac1c-5e2d5568ac35'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
