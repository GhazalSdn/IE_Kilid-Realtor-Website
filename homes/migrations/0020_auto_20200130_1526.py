# Generated by Django 3.0.2 on 2020-01-30 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0019_auto_20200130_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='housing',
        ),
        migrations.AddField(
            model_name='housing',
            name='pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homes.Image'),
        ),
    ]
