from django.urls import path
from .views import (mainpage)


app_name = 'main'
urlpatterns = [
        
        path('', mainpage, name='mainpage'),
        # path('stafflogin/', stafflogin, name='stafflogin'),
        # path('studentlogin/', studentlogin, name='studentlogin'),
    ]
