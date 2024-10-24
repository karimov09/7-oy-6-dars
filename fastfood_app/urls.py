from django.urls import path
from fastfood_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/update/<int:pk>/', views.update_food, name='update_food'),
    path('food/delete/<int:pk>/', views.delete_food, name='delete_food'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
