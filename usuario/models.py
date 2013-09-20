from django.db import models

TIPOPESSOA = (
    ('PF', 'Pessoa Fisica'),
    ('PF', 'Pessoa Juridica'),
)

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    profissao = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    tipopessoa = models.CharField(max_length=2,choices=TIPOPESSOA)
    cpf_cnpj = models.CharField(max_length=40)

