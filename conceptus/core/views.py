from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404

from conceptus.core.forms import StoreModelForm
from conceptus.core.models import Store


def dashboard(request):
    stores = Store.objects.all()
    return render(request, 'core/dashboard.html', {'stores': stores})


def create(request):
    if request.method == 'POST':
        form = StoreModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(r('core:dashboard'))
    else:
        form = StoreModelForm()

    return render(request, 'core/cadastro.html', {'form': form})


def editar(request, slug=None):
    try:
        store = get_object_or_404(Store, slug=slug)
    except Store.DoesNotExist:
        store = None

    if request.method == 'POST':
        form_store = StoreModelForm(request.POST, instance=store)
        if form_store.is_valid():
            form_store.save()

            messages.success(request, 'Atualização realizada')
            return HttpResponseRedirect(r('core:editar', slug=slug))
    else:
        form_store = StoreModelForm(instance=store)

    return render(request, 'core/editar.html', {'form_store': form_store})


