# Generated by Django 4.1 on 2022-09-14 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/1148/1148263.png?w=740&t=st=1663126784~exp=1663127384~hmac=9d455493b1a7fb8495f4312f51649d00e272d39e3bd55b9a774a89a25d12a857', max_length=500),
        ),
    ]