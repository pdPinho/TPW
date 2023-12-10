from django.urls import path
from hello import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("numero/<int:num>", views.numero, name="numero"),
]