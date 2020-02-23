from django.urls import path
#from .views import HomePageView
from . import views
urlpatterns = [
     path('',views.HomePageView.as_view(),name='home'),
]
