# Generated by Django 3.2.3 on 2021-07-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_name'),
        ('authentification', '0003_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='substitutes_saved',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
