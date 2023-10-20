# Generated by Django 3.2.1 on 2023-10-20 06:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0057_auto_20231019_1610'),
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
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('52b0d79a-c882-470b-8858-bfb2f2cfc075'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('6f16c3af-b5cc-4e9c-ba2f-eaac28349b96'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.AlterField(
            model_name='youtubevideodetails',
            name='model_details',
            field=models.ForeignKey(default=uuid.UUID('d92143d9-9b9b-4605-9951-cf40bc56444c'), on_delete=django.db.models.deletion.CASCADE, related_name='ytvideos', to='appv1.modeldetails'),
        ),
    ]
