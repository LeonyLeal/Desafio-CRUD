from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'tarefas', views.TodoView, 'tarefa')
router.register(r'contatos', views.ContatoView, 'contato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]