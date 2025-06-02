from django.db import models
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(
    regex=r'^\d{3}\. \d{3}\. \d{3}\.-\d{2}\$',
    message="O CPF deve ser preenchido de maneira correta."
)
class Client(models.Model):
    id = models.CharField(unique=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=120)
    data_de_nascimento= models.DateField()
    cpf = models.CharField(max_length=14, unique=True, validators=[cpf_validator])
    email= models.EmailField(unique=True)




    
def __str__(self):
    return self.nome
