from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fastfood_app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/update/<int:pk>/', views.update_food, name='update_food'),
    path('food/delete/<int:pk>/', views.delete_food, name='delete_food'),

    path('like/<int:food_id>/', views.add_like, name='add_like'),
    path('food/<int:food_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
