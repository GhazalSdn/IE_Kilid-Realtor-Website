# Generated by Django 3.0.2 on 2020-01-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0017_auto_20200130_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
    ]
