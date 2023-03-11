import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="detailed_description",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                default="",
                help_text="Подробное описание выполненной работы",
                verbose_name="Подробное описание",
            ),
            preserve_default=False,
        ),
    ]