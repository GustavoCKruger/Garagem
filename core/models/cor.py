from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"({self.id}) {self.nome}"