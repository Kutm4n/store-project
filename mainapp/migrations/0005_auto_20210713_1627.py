# Generated by Django 3.1.7 on 2021-07-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210706_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
