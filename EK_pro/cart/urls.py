"""
URL configuration for EK_pro project.

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
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.cart,name='cart'),
    path('add_cart/<int:product_id>/',v.add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',v.remove_cart,name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',v.remove_cart_item,name='remove_cart_item'),

    path('checkout/',v.checkout,name='checkout')
    
]
