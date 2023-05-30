# Generated by Django 4.2.1 on 2023-05-30 10:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='shor_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]