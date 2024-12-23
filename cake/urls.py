"""
URL configuration for cake project.

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
from Frosted_Dreams import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('order1/',views.order1, name='order1'),
    path('order2/',views.order2, name='order2'),
    path('order3/',views.order3, name='order3'),
    path('order4/',views.order4, name='order4'),
    path('order5/',views.order5, name='order5'),
    path('ordersave/', views.ordersave, name='ordersave'),
    path('order1/ordersave/',views.ordersave, name='ordersave_from_order1'),
    path('order2/ordersave/',views.ordersave, name='ordersave_from_order2'),
    path('order3/ordersave/',views.ordersave, name='ordersave_from_order3'),
    path('order4/ordersave/',views.ordersave, name='ordersave_from_order4'),
    path('order5/ordersave/',views.ordersave, name='ordersave_from_order5'),
    path('ordered/',views.ordered),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_view, name='login'),
     path('/', views.home_view, name='home'),
     path('logout/', views.logout_view, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

