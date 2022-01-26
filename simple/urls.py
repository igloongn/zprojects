from django.urls import path, re_path
from .views import open, paras, register, database,  single, update, delete

app_name = "simple"

urlpatterns = [
    path("", open, name = "open"),
    path("paras/<str:pk>", paras , name = "paras"),
    path("database", database , name = "database"),
    path("single/<str:num>", single , name = "single"),
    path("register/", register , name = "register"),
    path("update/<str:pk>", update , name = "update"),
    path("delete/<str:pk>", delete , name = "delete"),
]

