from django.urls import path
from website.views import about_view,contact_view,index_view

urlpatterns = [
    path('about',about_view),
    path('contact',contact_view),
    path('index',index_view),
]