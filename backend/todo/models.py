from django.db import models

# Create your models here.
class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=255, null=False)
    data_alteracao = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    
class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    contato_id = models.ForeignKey(Contato , on_delete=models.CASCADE, related_name="contato")
    titulo = models.CharField(max_length=64, null=False)
    descricao = models.TextField(max_length=128, null=False)
    ativo = models.BooleanField(default=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo