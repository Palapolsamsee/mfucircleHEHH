# Generated by Django 4.2.15 on 2024-11-06 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_tweet_content_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='handle',
        ),
    ]