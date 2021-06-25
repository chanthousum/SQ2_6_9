"""SQ2_6_9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path

from myapp import views, categoryViews,productViews

urlpatterns = [
    path("api/category/index", categoryViews.index, name="api/category/index"),
    path("api/category/create", categoryViews.create, name="api/category/create"),
    path("api/category/store", categoryViews.store, name="api/category/store"),
    path("api/category/destroy/<id>", categoryViews.destroy, name="api/category/destroy"),
    path("api/category/edit/<id>", categoryViews.edit, name="api/category/edit"),
    path("api/category/update/<id>", categoryViews.update, name="api/category/update"),
    #------------------------------Product------------------------------------------------
    path("api/product/index", productViews.index, name="api/product/index"),
    path("api/product/create", productViews.create, name="api/product/create"),
    path("api/product/store", productViews.store, name="api/product/store"),
    path("api/product/destroy/<id>", productViews.destroy, name="api/product/destroy"),
    path("api/product/edit/<id>", productViews.edit, name="api/product/edit"),
    path("api/product/update/<id>", productViews.update, name="api/product/update")

]
