from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.aboutUs, name='aboutUs'),
    path('contact/',views.contact, name='contactUs'),
    path('tracker/',views.tracker, name='tracking'),
    path('products/<int:id>',views.productView, name='product View'),
    path('checkout/',views.checkout, name='checkout'),
    path('search/',views.search, name='search'),
]