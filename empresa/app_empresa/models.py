from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    funcionarios = models.IntegerField(blank=True, null=True)
    clientes = models.IntegerField(blank=True, null=True)
    fornecedores = models.IntegerField(blank=True, null=True)
    produtos = models.IntegerField(blank=True, null=True)
    empresas_terceiras = models.IntegerField(blank=True, null=True)


def aumentar(self):
        valor = models.IntegerField(default=0)
        self.valor += 1
        self.save()
