# Generated by Django 2.2.3 on 2019-07-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eee', '0005_remove_customuser_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photos',
            field=models.FileField(default=None, upload_to='images/'),
        ),
    ]
