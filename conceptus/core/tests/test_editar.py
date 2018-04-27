from django.test import TestCase
from django.shortcuts import resolve_url as r

from conceptus.core.forms import StoreModelForm
from conceptus.core.models import Store


class EditarTest(TestCase):
    def setUp(self):
        self.obj = Store.objects.create(nome='Americana',
                                        descricao='loja americana de variedades',
                                        slug='loja-americana',
                                        contato=1235444554,
                                        ramo_atuacao='Variedade')

        self.resp = self.client.get(r('core:editar', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/editar.html')

    def test_context_store(self):
        form_store = self.resp.context['form_store']
        self.assertIsInstance(form_store, StoreModelForm)
