# Generated by Django 3.2.4 on 2021-06-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nashsshubapi', '0002_auto_20210609_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='hostname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]