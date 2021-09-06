import re

from django.forms import ModelForm
from validate_docbr import CNPJ, CPF

from portifolio.cadastro.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'fantasia', 'cpf_cnpj', 'bairro', 'cep', 'email', 'complemento',
                  'logradouro', 'numero', 'fone', 'celular', 'uf', 'contato', 'cidade')

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            if instance.id:
                self.fields['cpf_cnpj'].widget.attrs['readonly'] = True
                self.fields['nome'].widget.attrs['autofocus'] = True
            else:
                self.fields['cpf_cnpj'].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        instance = super(ClienteForm, self).save(commit=False)
        cpf_cnpj = re.sub('[^0-9]', '', instance.cpf_cnpj)
        if len(cpf_cnpj) > 11:
            if not CNPJ().validate(cpf_cnpj):
                raise Exception('cnpj inválido')
        elif not CPF().validate(cpf_cnpj):
            raise Exception('cpf inválido')
        if commit:
            instance.cpf_cnpj = cpf_cnpj
            instance.save()
        return instance
