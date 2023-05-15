# Generated by Django 4.2.1 on 2023-05-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tapeman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tape',
            name='capacity',
            field=models.FloatField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tape',
            name='data_expiration',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tape',
            name='pool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tapeman.tapepool'),
        ),
    ]