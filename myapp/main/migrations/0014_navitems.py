# Generated by Django 4.2 on 2023-04-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='navItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
            ],
        ),
    ]
