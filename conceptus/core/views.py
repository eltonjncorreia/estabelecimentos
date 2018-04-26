from django.shortcuts import render

from conceptus.core.models import Store


def dashboard(request):
    stores = Store.objects.all()
    return render(request, 'core/dashboard.html', {'stores': stores})
