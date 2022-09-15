from rest_framework import serializers
from .models import Tarefa
from .models import Contato

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ("id",'titulo', 'descricao', 'contato_id' , 'ativo')
    
    def to_representation(self, instance):
        rep = super(TodoSerializer, self).to_representation(instance)
        rep['contato_id'] = instance.contato_id.nome
        return rep

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('id','nome', 'email')