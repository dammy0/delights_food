from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm

# Create your views here.
def home(request):
    return render(request, "restaurant/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "restaurant/ingredient_list.html"

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "restaurant/ingredient_create_form.html"

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "restaurant/ingredient_update_form.html"

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = "/ingredient/list"
    template_name = "restaurant/ingredient_delete_form.html"

class MenuItemList(ListView):
    model = MenuItem
    template_name = "restaurant/menuitem_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "restaurant/menuitem_create_form.html"

class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "restaurant/menuitem_update_form.html"

class MenuItemDelete(DeleteView):
    model = MenuItem
    success_url = "/menuitem/list"
    template_name = "restaurant/menuitem_delete_form.html"

class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "restaurant/reciperequirement_list.html"

class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "restaurant/reciperequirement_create_form.html"

class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "restaurant/reciperequirement_update_form.html"

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    success_url = "/reciperequirement/list"
    template_name = "restaurant/reciperequirement_delete_form.html"
