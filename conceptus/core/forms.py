from django.forms import ModelForm

from conceptus.core.models import Store


class StoreModelForm(ModelForm):

    class Meta:
        model = Store
        fields = '__all__'