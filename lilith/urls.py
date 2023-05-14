from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', homeView, name='home'),
    path('create/', create, name='create'),
    path('create-view', createView, name='createView'),
    path('listar/', listarView, name='listar'),
    path('update/<int:id>', updateView, name='update'),
    path('deleteView/<int:id>', deleteView, name='deleteView'),
]
