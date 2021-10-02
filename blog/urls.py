from . import views
from django.urls import path

urlpatterns = [

    path('',views.bloglist),
    path('create/',views.blogView),
    path('blogcreate/',views.blogcreate),
    path('blogdetails/<int:id>',views.blogdetails),

]