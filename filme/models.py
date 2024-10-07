from django.db import models
import uuid
# Create your models here.

class Filme(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    lancamento = models.DateField()
    link = models.CharField(max_length=500)
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        def __str__(self):
            return self.nome


