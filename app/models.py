from django.db import models

# Create your models here.
class livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data = models.DateField()
    quantidade = models.IntegerField(max_length=100)
    editora = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class emprestimo(models.Model):
    STATUS = (
        ('emprestado', 'emprestado'),
        ('devolvido', 'devolvido'),
    )
    nome = models.ForeignKey(livro, on_delete=models.CASCADE)
    dataem = models.DateField()
    pessoa = models.CharField(max_length=100)
    quantidadeem = models.IntegerField(max_length=100)
    estado = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    serie = models.CharField(max_length=100)
    criado_emp = models.DateTimeField(auto_now_add=True)
    editado_emp = models.DateTimeField(auto_now=True)