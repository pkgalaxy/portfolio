
from django.contrib import admin      # from django framework >>> contrib module >>> importing  admin site / class
from django.urls import path, include    # from django framework >>> urls module >>>  path and include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
]
