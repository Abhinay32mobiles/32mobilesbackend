# Generated by Django 3.2.1 on 2023-10-20 05:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0051_auto_20231019_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('homepage_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('homepage_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('homepage_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('homepagevert_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagevert_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagevert_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagevert_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagehori_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagehori_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagehori_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepagehori_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('homepage_brand_banner_cdn', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('articles_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('articles_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('articles_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('articles_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('artilcevert_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcevert_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcevert_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcevert_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcehori_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcehori_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcehori_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('artilcehori_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('products_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('products_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('products_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('products_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=15)),
                ('productvert_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('productvert_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('productvert_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('productvert_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('producthori_cdn_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('producthori_redirect_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('producthori_banner_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5)),
                ('producthori_button_text', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=5)),
            ],
        ),
    
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
            field=models.ForeignKey(default=uuid.UUID('350f1ad0-4a6c-40ba-935d-b3a28e687a5a'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
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
            field=models.ForeignKey(default=uuid.UUID('a334a545-80ac-40a5-8b75-28bbacc54fb7'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
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
            field=models.ForeignKey(default=uuid.UUID('3ff3b9f2-a114-449a-a499-7931b62b7138'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]