from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from conceptus.core.forms import StoreModelForm
from conceptus.core.models import Store


def dashboard(request):
    valor = request.GET.get('valor')
    if valor:
        stores = Store.objects.filter(nome__contains=valor)

    if not valor:
        stores = Store.objects.all()
        paginator = Paginator(stores, 5)

        page = request.GET.get('page')
        stores = paginator.get_page(page)

    return render(request, 'core/dashboard.html', {'stores': stores})


def create(request):
    if request.method == 'POST':
        form = StoreModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastrado com sucesso")
            return HttpResponseRedirect(r('core:create'))
    else:
        form = StoreModelForm()
    return render(request, 'core/cadastro.html', {'form': form})


def editar(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise ValueError('Error')

    if request.method == 'POST':
        form_store = StoreModelForm(request.POST, instance=store)
        if form_store.is_valid():
            form_store.save()

            messages.success(request, 'Atualização realizada')
            return HttpResponseRedirect(r('core:editar', pk=pk))
    else:
        form_store = StoreModelForm(instance=store)

    return render(request, 'core/editar.html', {'form_store': form_store, 'store': store.slug})


def deletar(request, slug):
    Store.objects.filter(slug=slug).delete()
    messages.success(request, 'Deletado com sucesso')
    return HttpResponseRedirect(r('core:dashboard'))
