# Generated by Django 4.2 on 2023-07-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_instantquote_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media')),
                ('video_name', models.CharField(max_length=100)),
            ],
        ),
    ]
