# Generated by Django 4.0 on 2022-02-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0010_alter_event_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='participated_in',
        ),
        migrations.AddField(
            model_name='event',
            name='bands_participated',
            field=models.ManyToManyField(related_name='events_performed', to='concerts.Band'),
        ),
    ]