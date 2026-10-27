from .views import home, welcome, listExpeditions, detailExpedition
from django.urls import path

urlpatterns = [
    path('home/', home , name="home"),
    path('w/<str:name>/', welcome, name="welcomeFunction"),
    path('list/',listExpeditions,name="list"),
    path('detail/<int:id>/', detailExpedition, name="detail"),
]