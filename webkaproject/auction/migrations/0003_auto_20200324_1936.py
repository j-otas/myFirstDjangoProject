# Generated by Django 3.0.4 on 2020-03-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20200322_0425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'verbose_name': 'Ставка', 'verbose_name_plural': 'Ставки'},
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(null=True),
        ),
    ]
