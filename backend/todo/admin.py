from django.contrib import admin
from .models import Tarefa
from .models import Contato
# Register your models here.

class tarefaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','ativo')
    readonly_fields = ('id','data_alteracao', 'data_cadastro')
    
class contatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','data_cadastro')
    readonly_fields = ('id','data_alteracao', 'data_cadastro')


admin.site.register(Tarefa, tarefaAdmin)
admin.site.register(Contato, contatoAdmin)