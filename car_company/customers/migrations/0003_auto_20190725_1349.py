# Generated by Django 2.2.1 on 2019-07-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20190724_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='city',
        ),
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]
