from django.urls import path
from .views import *



urlpatterns=[
    path('',CrudView,name="crud"),
    path('show',show,name="show"),
    path('edit/<int:id>',edit,name="edit"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    
]