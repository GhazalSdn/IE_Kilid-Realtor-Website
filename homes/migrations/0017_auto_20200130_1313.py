# Generated by Django 3.0.2 on 2020-01-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0016_auto_20200130_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
