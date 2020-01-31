# Generated by Django 3.0.2 on 2020-01-31 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0022_auto_20200131_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homes.Housing'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='pic',
            field=models.CharField(max_length=50, null=True),
        ),
    ]