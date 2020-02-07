from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    # url is based on name parameter instead of literal file name
    path('count/',views.count, name='count'),
]
