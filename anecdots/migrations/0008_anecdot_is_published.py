# Generated by Django 4.0.5 on 2022-07-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anecdots', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='anecdot',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
