# Generated by Django 4.0 on 2022-01-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0006_event_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, default='concerts/no_poster.jpg', upload_to='images', verbose_name='Image'),
        ),
    ]
