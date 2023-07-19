# Generated by Django 4.2.2 on 2023-07-19 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Confession',
            fields=[
                ('slug', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('urls', models.CharField(blank=True, max_length=128, null=True)),
                ('sender', models.CharField(max_length=30)),
                ('target', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('answer', models.BooleanField(null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('answer_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]
