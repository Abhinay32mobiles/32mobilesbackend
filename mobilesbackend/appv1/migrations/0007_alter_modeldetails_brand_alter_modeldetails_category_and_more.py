# Generated by Django 4.2.6 on 2023-10-12 09:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appv1', '0006_remove_category_mobile_remove_category_tv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeldetails',
            name='brand',
            field=models.ForeignKey(default=uuid.UUID('d43af7fd-ac2b-4146-93ad-af79d02d46d8'), on_delete=django.db.models.deletion.CASCADE, to='appv1.brand'),
        ),
        migrations.AlterField(
            model_name='modeldetails',
            name='category',
            field=models.ForeignKey(default=uuid.UUID('4204264b-c20e-4d3c-a965-74dac9a3ffef'), on_delete=django.db.models.deletion.CASCADE, to='appv1.category'),
        ),
        migrations.CreateModel(
            name='CategoryBrandRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appv1.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appv1.category')),
            ],
        ),
    ]
