# Generated by Django 2.2.6 on 2019-11-05 06:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mldemo', '0007_auto_20191102_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervised',
            name='project_short_descr',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supervised',
            name='project_demo_link',
            field=models.URLField(max_length=250),
        ),
    ]
