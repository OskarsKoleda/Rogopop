# Generated by Django 4.0 on 2022-01-08 21:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, default='', max_length=215, unique=True)),
                ('date', models.DateField(blank=True)),
                ('city', models.CharField(max_length=30)),
                ('ticket_price', models.IntegerField(blank=True)),
                ('comment', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to='accounts.profile')),
                ('participants', models.ManyToManyField(related_name='participated_in', to='accounts.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bands', to='accounts.profile')),
                ('event', models.ManyToManyField(blank=True, related_name='events_in', to='concerts.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
