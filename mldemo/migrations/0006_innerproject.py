# Generated by Django 2.2.6 on 2019-11-02 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mldemo', '0005_auto_20191102_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnerProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_image/innerpage/%Y/%m/%d/')),
                ('project_demo_link', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('project_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mldemo.ProjectCategory')),
                ('project_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mldemo.ProjectSubCategory')),
            ],
        ),
    ]
