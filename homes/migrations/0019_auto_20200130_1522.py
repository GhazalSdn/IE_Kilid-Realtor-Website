# Generated by Django 3.0.2 on 2020-01-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0018_housing_bookmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='pic',
        ),
        migrations.AddField(
            model_name='image',
            name='housing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homes.Housing'),
        ),
    ]
