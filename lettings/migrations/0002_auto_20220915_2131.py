# Generated by Django 3.0 on 2022-09-15 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0002_auto_20220915_2117'),
    ]

    operations = [
        migrations.RunSQL(
            'INSERT INTO lettings_address SELECT * FROM oc_lettings_site_address;'
        ),
        migrations.RunSQL(
            'INSERT INTO lettings_letting SELECT * FROM oc_lettings_site_letting;'
        )
    ]
