from django.urls import path  # from django framework >>> urls module >>>  importing path function
from .views import *   # from views module  importing all objects.

urlpatterns = [
    path('', home , name='home'),
    path('inner-page/', inner_page , name='inner_page'),
    path('portfolio-details/', portfolio_details , name='portfolio_details'),
]
