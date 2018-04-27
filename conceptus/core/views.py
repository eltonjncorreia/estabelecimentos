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


def detail(request, slug=None):
    try:
        store = get_object_or_404(Store, slug=slug)
    except Store.DoesNotExists:
        raise ValueError('Erro')

    return render(request, 'core/detail.html', {'store': store})


