# Generated by Django 3.2.1 on 2023-10-22 11:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0064_auto_20231021_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='statics',
            name='product_priceband_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('cd3923d6-cad6-497a-9081-74a2722bb4a1'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('aa6164e1-57e7-4b60-8e58-f8c52b7f10fa'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='statics',
            name='articles_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='articles_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='artilcehori_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='artilcehori_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='artilcevert_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='artilcevert_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepage_brand_banner_cdn',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepage_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepage_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepagehori_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepagehori_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepagevert_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='homepagevert_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='producthori_button_text',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='producthori_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='producthori_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='products_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='products_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=15),
        ),
        migrations.AlterField(
            model_name='statics',
            name='productvert_cdn_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='statics',
            name='productvert_redirect_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=400), blank=True, null=True, size=5),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('6d8a83de-b7bf-46b6-afb6-dc2752eac753'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]