"""
URL configuration for fastfood_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fastfood_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/update/<int:pk>/', views.update_food, name='update_food'),
    path('food/delete/<int:pk>/', views.delete_food, name='delete_food'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


