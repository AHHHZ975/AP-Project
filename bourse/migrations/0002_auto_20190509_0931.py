# Generated by Django 2.2.1 on 2019-05-09 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='publicDate',
            field=models.DateTimeField(default=2019, verbose_name='Data published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='publicDate',
            field=models.DateTimeField(default=2019, verbose_name='Data published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currentassets',
            name='publicDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 9, 31, 22, 109272, tzinfo=utc), verbose_name='Data published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debtsandassetsowner',
            name='publicDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 9, 31, 31, 628654, tzinfo=utc), verbose_name='Data published'),
            preserve_default=False,
        ),
    ]