from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    FRUITS_VEGETABLES = 'FV'
    MEAT = 'MT'
    DIARY = 'D'
    CATEGORIES = [
        (FRUITS_VEGETABLES, 'fruits and vegetables'),
        (MEAT, 'meat'),
        (DIARY, 'diary'),
    ]

    KILOGRAM = 'kg'
    PIECES = 'pcs'
    PACKAGES = 'pkgs'
    UNITS = [
        (KILOGRAM, 'kg'),
        (PIECES, 'pcs'),
        (PACKAGES, 'pkgs'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=20, choices=UNITS, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    note = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ['complete']
