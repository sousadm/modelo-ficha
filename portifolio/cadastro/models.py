from django.db import models
from django.utils.text import slugify


class Cliente(models.Model):
    slug = models.SlugField(max_length=100, unique=True, default='.')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    fantasia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fantasia')
    cpf_cnpj = models.CharField(max_length=14, unique=True, verbose_name='CPF/CNPJ')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    email = models.EmailField('E-mail', blank=True, null=True)
    complemento = models.CharField(max_length=35, blank=True, null=True, verbose_name='Complemento')
    logradouro = models.CharField(max_length=150, blank=True, null=True, verbose_name='Logradouro')
    numero = models.IntegerField(verbose_name='Número', blank=True, null=True)
    fone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Fone')
    celular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Celular')
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name='UF')
    contato = models.CharField(max_length=100, blank=True, null=True, verbose_name='Contato')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        db_table = "cliente"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome)
        super(Cliente, self).save(*args, **kwargs)

    @property
    def endereco_completo(self):
        return self.logradouro + ', ' + str(
            self.numero) + " " + self.bairro + ", CEP-" + self.cep + " em " + self.cidade + "/" + self.uf

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
        db_table = 'cliente'
