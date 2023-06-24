from django.urls import path
from . import views



urlpatterns = [
    path('', views.Store, name='store' ),
    path('<slug:category_slug>/', views.Store, name='products_by_category' ),
]


