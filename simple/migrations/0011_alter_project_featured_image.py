# Generated by Django 4.0 on 2021-12-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0010_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]