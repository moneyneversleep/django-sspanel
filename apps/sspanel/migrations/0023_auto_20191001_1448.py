# Generated by Django 2.2.1 on 2019-10-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0022_auto_20190920_2238"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vmessnode", old_name="alert_id", new_name="alter_id",
        ),
    ]
