from django.db import models
from django.core.validators import RegexValidator


class Store(models.Model):
    ATUACAO = (('A', 'Alimentos'),
               ('Auto', 'Automóveis'),
               ('Esp', 'Esport'))

    ramo_atuacao = models.CharField(max_length=4, choices=ATUACAO)
    nome = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Slug')
    descricao = models.CharField('Descrição', max_length=255)
    contato = models.IntegerField('Contato', validators=[RegexValidator(r'^\d+$')])

    class Meta:
        ordering = ['nome']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.nome

