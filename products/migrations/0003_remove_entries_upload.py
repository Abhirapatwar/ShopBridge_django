# Generated by Django 4.0.4 on 2022-06-02 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_entries_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='upload',
        ),
    ]
