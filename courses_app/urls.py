from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name = ''),
    path('create', views.create),
    # path('destroy', views.destroy),
    path('courses/destroy/<int:id>', views.delete),
    path('destroy/<int:id>', views.destroy),
]