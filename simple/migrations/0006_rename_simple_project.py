# Generated by Django 4.0 on 2021-12-12 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0005_simple_tag_alter_simple_demo_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Simple',
            new_name='Project',
        ),
    ]