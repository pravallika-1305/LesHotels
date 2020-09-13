from django.urls import path
#from .views import SignUpView
from . import views
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
