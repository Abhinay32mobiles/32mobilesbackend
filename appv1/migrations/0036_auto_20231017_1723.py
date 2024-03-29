# Generated by Django 3.2.1 on 2023-10-17 11:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0035_auto_20231017_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldetails',
            name='accessibility_features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='audio_jack',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='battery_life',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='biometric_security',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='bluetooth_version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='color_options',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='dust_resistance',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='gaming_performance',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='gps',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='nfc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='os_updates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='price_range',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='sensors',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='speaker_quality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='special_features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='warranty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='water_resistance',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='wi_fi',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='modeldetails',
            name='wireless_charging',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('e2391ca9-a1c4-49a5-95f0-9188e1a1aae8'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('d0848ae4-849e-49fa-b03b-9668058a9ab2'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('2d02a5c6-cb32-42d2-9118-12d448d6022f'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
