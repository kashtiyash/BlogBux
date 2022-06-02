from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Home"),
    path('contact/', views.contact, name="Contact"),
    path('post-details/<int:pk>/', views.post_details, name="post_details"),
    path('post-edit/<int:pk>/', views.post_edit, name="post_edit"),
    path('post-delete/<int:pk>/', views.post_delete, name="post_delete"),

]
