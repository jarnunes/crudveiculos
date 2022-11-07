from django.db import models
from django.core.validators import MinValueValidator


class Veiculo(models.Model):
    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=50, null=False)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False)
    valor = models.FloatField(null=False)
    data_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo

    @staticmethod
    def get_all_fields_name():
        return [field.name for field in Veiculo._meta.get_fields()]
