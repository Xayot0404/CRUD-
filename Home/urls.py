from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',CrudView,name="crud"),
    path('show',show,name="show"),
    path('edit/<int:eddid>',editView,name="edit"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)