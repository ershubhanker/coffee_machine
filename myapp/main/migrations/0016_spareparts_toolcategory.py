# Generated by Django 4.2 on 2023-05-21 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_spareparts'),
    ]

    operations = [
        migrations.AddField(
            model_name='spareparts',
            name='toolCategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
