from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    FRUITS_VEGETABLES = 'FV'
    MEAT = 'MT'
    DIARY = 'D'
    DRY_GOODS = 'DG'
    ALCOHOLS = 'ALC'
    MEDICINE = 'MED'
    PET_GOODS = 'PG'
    BABY_GOODS = 'BG'
    DOMESTIC_DETERGENTS = 'DD'
    READY_COOK_MEALS = 'RCM'
    HYGIENE = 'H'
    COFFEE_TEA = 'CT'
    FROZEN_FOODS = 'FF'
    GARDEN_TINKER = 'GT'
    BREAD = 'B'
    PRESERVES = 'PV'
    SPICES = 'S'
    FISH = 'FS'
    SWEETS = 'SS'
    FATS = 'F'
    DRINKS = 'WD'
    NUTS = 'DFN'
    HERBS = 'FH'
    CANS = 'CF'
    OTHER = 'O'
    CATEGORIES = [
        (FRUITS_VEGETABLES, 'fruits and vegetables'),
        (MEAT, 'meat'),
        (DIARY, 'diary'),
        (DRY_GOODS, 'dry goods'),
        (ALCOHOLS, 'alcohols'),
        (MEDICINE, 'medicine'),
        (PET_GOODS, 'pet goods'),
        (BABY_GOODS, 'baby goods'),
        (DOMESTIC_DETERGENTS, 'domestic detergents'),
        (READY_COOK_MEALS, 'ready-cook meals'),
        (HYGIENE, 'hygiene'),
        (COFFEE_TEA, 'coffee & tea'),
        (FROZEN_FOODS, 'frozen foods'),
        (GARDEN_TINKER, 'garden and tinkering'),
        (BREAD, 'bread'),
        (PRESERVES, 'preserves'),
        (SPICES, 'spices, sauces, additives'),
        (FISH, 'fishes and seafood'),
        (SWEETS, 'sweets and snacks'),
        (FATS, 'fats'),
        (DRINKS, 'water and drinks'),
        (NUTS, 'dried fruit and nuts'),
        (HERBS, 'fresh herbs'),
        (CANS, 'canned food'),
        (OTHER, 'other')
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
