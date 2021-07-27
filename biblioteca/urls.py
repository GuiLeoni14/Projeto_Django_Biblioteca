"""biblioteca URL Configuration

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
from django.contrib import admin
from django.urls import path
from app.views import (
    home,
    form,
    create,
    view,
    edit,
    update,
    delete,
    table,
    list_emprestimo,
    createem,
    homeem,
    viewem,
    editem,
    updateem,
    deleteem,
    tableem,
    editemp,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("create/", create, name="create"),
    path("view/<int:pk>/", view, name="view"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="dalete"),
    path("table/", table, name="table"),
    path("homeem", homeem, name="homeem"),
    path("emprestimo/", list_emprestimo, name="emprestimo"),
    path("createem/", createem, name="createem"),
    path("viewem/<int:pk>/", viewem, name="viewem"),
    path("editem/<int:pk>/", editem, name="editem"),
    path("updateem/<int:pk>/", updateem, name="updateem"),
    path("deleteem/<int:pk>/", deleteem, name="daleteem"),
    path("tableem/", tableem, name="tableem"),
    path("editemp/<int:pk>/", editemp, name="editemp"),
]
