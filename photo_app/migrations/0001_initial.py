# Generated by Django 3.2 on 2021-04-08 15:04

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 4, 10, 126108))),
            ],
        ),
    ]
