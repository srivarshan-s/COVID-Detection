# Generated by Django 3.2 on 2021-04-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_alter_userimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(upload_to='covid/static/covid/userImage/'),
        ),
    ]
