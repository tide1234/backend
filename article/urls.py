from django.urls import path
from .views import getAllArticle, getArticle, createArticle

urlpatterns =[
    path("getarticles/", getAllArticle),
    path("getarticle/<int:id>", getArticle),
    path("createarticle/", createArticle)
]