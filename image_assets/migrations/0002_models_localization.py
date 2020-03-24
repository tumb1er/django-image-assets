# Generated by Django 3.0.4 on 2020-03-24 08:26

from django.db import migrations, models
import django.db.models.deletion
import image_assets.models
from image_assets import defaults


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('image_assets', '0001_initial'),
    ]

    operations = []

    if defaults.ASSET_TYPE_MODEL == 'image_assets.AssetType':
        operations.extend([
            migrations.AlterModelOptions(
                name='assettype',
                options={'verbose_name': 'Asset Type',
                         'verbose_name_plural': 'Asset Types'},
            ),
            migrations.AlterField(
                model_name='assettype',
                name='allowed_for',
                field=models.ManyToManyField(blank=True,
                                             related_name='allowed_asset_types',
                                             related_query_name='allowed_asset_types',
                                             to='contenttypes.ContentType',
                                             verbose_name='Allowed for'),
            ),
            migrations.AlterField(
                model_name='assettype',
                name='slug',
                field=models.SlugField(unique=True, verbose_name='Slug'),
            ),
            migrations.AlterField(
                model_name='assettype',
                name='required_for',
                field=models.ManyToManyField(blank=True,
                                             related_name='required_asset_types',
                                             related_query_name='required_asset_types',
                                             to='contenttypes.ContentType',
                                             verbose_name='Required for'),
            ),
        ])
    if defaults.ASSET_MODEL == 'image_assets.Asset':
        operations.extend([
            migrations.AlterModelOptions(
                name='asset',
                options={'verbose_name': 'Asset', 'verbose_name_plural': 'Assets'},
            ),
            migrations.AlterField(
                model_name='asset',
                name='active',
                field=models.BooleanField(default=True, verbose_name='Active'),
            ),
            migrations.AlterField(
                model_name='asset',
                name='asset_type',
                field=models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='image_assets.AssetType', verbose_name='Asset Type'),
            ),
            migrations.AlterField(
                model_name='asset',
                name='content_type',
                field=models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='contenttypes.ContentType', verbose_name='Content Type'),
            ),
            migrations.AlterField(
                model_name='asset',
                name='image',
                field=models.ImageField(upload_to='', validators=[
                    image_assets.models.AssetType.validate_asset],
                                        verbose_name='Image'),
            ),
            migrations.AlterField(
                model_name='asset',
                name='object_id',
                field=models.IntegerField(verbose_name='Object ID'),
            ),

        ])
    if defaults.DELETED_ASSET_MODEL == 'image_assets.DeletedAsset':
        operations.extend([
            migrations.AlterModelOptions(
                name='deletedasset',
                options={'verbose_name': 'Deleted Asset',
                         'verbose_name_plural': 'Deleted Assets'},
            ),

        ])
