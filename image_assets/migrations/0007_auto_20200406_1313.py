# Generated by Django 3.0.5 on 2020-04-06 13:13

import bitfield.models
from django.db import migrations, models
import image_assets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('image_assets', '0006_migrate_formats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assettype',
            name='format',
        ),
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(upload_to='', validators=[image_assets.validators.AssetValidator()], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='assettype',
            name='formats',
            field=bitfield.models.BitField((('jpeg', 'JPEG'), ('png', 'PNG')), default=None),
        ),
    ]
