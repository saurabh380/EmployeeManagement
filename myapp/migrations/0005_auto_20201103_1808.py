# Generated by Django 3.0.6 on 2020-11-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201101_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplyee_details',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
