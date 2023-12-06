from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete")
]