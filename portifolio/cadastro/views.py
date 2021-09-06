from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from portifolio.cadastro.forms import ClienteForm
from portifolio.cadastro.models import Cliente
from portifolio.core.core.report import render_to_pdf


def get_data_impressao(request, cliente):
    return {
        'nome': cliente.nome,
        'cpf_cnpj': cliente.cpf_cnpj,
        'cpf_cnpj': cliente.cpf_cnpj,
        'bairro': cliente.bairro,
        'cep': cliente.cep,
        'email': cliente.email,
        'complemento': cliente.complemento,
        'logradouro': cliente.logradouro,
        'numero': cliente.numero,
        'fone': cliente.fone,
        'celular': cliente.celular,
        'uf': cliente.uf,
        'contato': cliente.contato,
        'cidade': cliente.cidade
    }


def ClienteNew(request):
    lista = Cliente.objects.all()
    cliente = lista[0]
    form = ClienteForm(request.POST or None, instance=cliente)

    if request.POST.get('btn_imprimir'):
        pdf = render_to_pdf('cadastro/ficha.html', get_data_impressao(request, cliente))
        return HttpResponse(pdf, content_type='application/pdf')

    if request.method == 'POST':
        if form.is_valid():
            try:
                cliente = form.save()
                return HttpResponseRedirect(reverse('url_padrao'))
            except Exception as e:
                messages.error(request, e)

    context = {
        'form': form
    }
    return render(request, 'cadastro/cliente_edit.html', context)
