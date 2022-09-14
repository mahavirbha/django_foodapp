from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default="https://cdn-icons-png.flaticon.com/512/1148/1148263.png?w=740&t=st=1663126784~exp=1663127384~hmac=9d455493b1a7fb8495f4312f51649d00e272d39e3bd55b9a774a89a25d12a857")
