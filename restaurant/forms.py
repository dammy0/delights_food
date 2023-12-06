from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'price')

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('item', 'price')

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menuitem', 'ingredient')

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('item_purchased', 'quantity')       