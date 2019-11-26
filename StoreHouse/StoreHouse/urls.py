"""StoreHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from store_app import views

urlpatterns = [
    path('quit/', views.quit),
    path('admin/', admin.site.urls),
    path('', views.main),
    path('manage/', views.manage),
    path('login/', views.login),
    path('query/', views.query),
    path('in_cargo/<str:cargo_name>/', views.in_cargo),
    path('out_cargo/<str:cargo_name>/', views.out_cargo),
    path('in_new_cargo/', views.in_new_cargo),
    path('check_in/', views.check_in),
    path('check_out/', views.check_out),
    path('check/进货/', views.check_query_in),
    path('check/出货/', views.check_query_out),
    path('toregiste/', views.registe),
    path('User_registe/', views.add_User),
    path('del_User/', views.delete_User)
]
