from django.db import models
from autor import Autor

# Create your models here.

class Livro(models.Model):

    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor)
