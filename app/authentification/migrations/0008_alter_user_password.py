# Generated by Django 3.2.3 on 2021-07-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]