from django.contrib import admin
from django.urls import path,include
from .views import index,QuestonAPI,latest
from rest_framework import routers

router = routers.DefaultRouter()
router.register("questions",QuestonAPI)

urlpatterns = [
    path('', latest, name="latest"),
    path('', include(router.urls)),
    # path('latest',latest,name="latest")

]
