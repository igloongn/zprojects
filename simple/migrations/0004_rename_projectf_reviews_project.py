# Generated by Django 4.0 on 2021-12-12 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0003_rename_project_reviews_projectf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='projectf',
            new_name='project',
        ),
    ]
