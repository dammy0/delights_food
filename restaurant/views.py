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
