# Generated by Django 4.2.6 on 2023-10-12 10:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0007_alter_modeldetails_brand_alter_modeldetails_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('TV', 'TV')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('9eaf801b-a597-4fce-b656-c6e6391364e6'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('a0de6c59-0877-4cdb-8c6c-f29605b326a7'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
    ]
