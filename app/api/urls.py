from django.urls import path
from . import views

urlpatterns = [
    path('create_new_product/', views.CreateNewProductView.as_view()),
    path('get_name_product/', views.GetNameProductView.as_view()),
    path('get_product/', views.GetProductView.as_view()),
]
