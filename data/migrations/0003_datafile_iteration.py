# Generated by Django 2.0.13 on 2019-08-29 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_datafile_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='iteration',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
