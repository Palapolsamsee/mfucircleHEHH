# Generated by Django 4.2.15 on 2024-11-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_helpcenter_alter_event_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpcenter',
            name='is_checked',
        ),
        migrations.AlterField(
            model_name='helpcenter',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='helpcenter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='helpcenter_images/'),
        ),
    ]