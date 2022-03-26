from django.contrib.auth import get_user_model
from django.contrib import admin

from .models import RecipeIngredient, Recipe

# Register your models here.
User = get_user_model()

admin.site.register(RecipeIngredient)


class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    # fields = ['name', 'quanity', 'unit', 'directions']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields = ["user"]


admin.site.register(Recipe, RecipeAdmin)
