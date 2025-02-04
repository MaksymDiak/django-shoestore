from django.db import models
from brand.models import Brand


class Shoe(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="shoe")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ShoeSize(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="sizes")
    size = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.shoe.name} (Size {self.size}): {self.stock} in stock"
