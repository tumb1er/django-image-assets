# Generated by Django 3.0.5 on 2020-04-06 13:02

from django.db import migrations
from image_assets import defaults


# noinspection PyUnusedLocal
def migrate_formats(apps, schema_editor):
    app_label, model_name = defaults.ASSET_TYPE_MODEL.split('.')
    # noinspection PyPep8Naming
    AssetType = apps.get_model(app_label, model_name)
    formats = AssetType._meta.get_field('formats')

    for at in AssetType.objects.all():
        flag = getattr(formats, at.format)
        at.formats = flag
        at.save()


class Migration(migrations.Migration):

    dependencies = [
        ('image_assets', '0005_assettype_formats'),
    ]

    operations = [
        migrations.RunPython(migrate_formats, migrations.RunPython.noop),
    ]
