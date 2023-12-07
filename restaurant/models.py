from django.db import models
from decimal import *

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, blank=False)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/ingredient/list"

class MenuItem(models.Model):
    item = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def menu_cost(self):
        total_cost = Decimal(0.00)
        ingredient_list = self.reciperequirement_set.all()
        for i in ingredient_list:
            total_cost += i.ingredient_cost
        return total_cost
    def __str__(self):
        return self.item
    def get_absolute_url(self):
        return "/menuitem/list"

class RecipeRequirement(models.Model):
    menuitem = models.ForeignKey(
        MenuItem, 
        on_delete=models.PROTECT, 
        blank=False
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        blank=False
    )
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    
    @property
    def ingredient_cost(self):
        return self.ingredient.price * self.quantity

    def __str__(self):
        return str(self.menuitem) + " " + str(self.ingredient)
    def get_absolute_url(self):
        return "/reciperequirement/list"

class Purchase(models.Model):
    item_purchased = models.ForeignKey(
        MenuItem, 
        on_delete=models.PROTECT, 
        blank=False
    )
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cost(self):
        return self.quantity * self.item_purchased.menu_cost
    @property
    def revenue(self):
        return self.quantity * self.price
    def profit(self):
        return self.revenue - self.cost
    def __str__(self):
        return str(self.item_purchased) + " " + str(self.created_at)
    def get_absolute_url(self):
        return "/purchase/list"