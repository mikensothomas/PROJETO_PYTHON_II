from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    funcionarios = models.IntegerField(default=0)
    bt1mais = models.IntegerField(default=0)
    clientes = models.IntegerField(blank=True, null=True)
    fornecedores = models.IntegerField(blank=True, null=True)
    produtos = models.IntegerField(blank=True, null=True)
    empresas_terceiras = models.IntegerField(blank=True, null=True)

    
