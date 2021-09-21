from django.urls import path
from . import views

<<<<<<< Updated upstream

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
=======
urlpatterns = [
	path( '', views.home ),
	path( 'products/', views.products ),
	path( 'customer/', views.customer ),
>>>>>>> Stashed changes
]