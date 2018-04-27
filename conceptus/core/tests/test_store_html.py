from django.test import TestCase
from django.shortcuts import resolve_url as r

from conceptus.core.forms import StoreModelForm
from conceptus.core.models import Store


class StoreHtmlTest(TestCase):
    def setUp(self):
        self.obj = Store.objects.create(nome='Americana',
                                        descricao='loja americana de variedades',
                                        slug='loja-americana',
                                        contato=1235444554,
                                        ramo_atuacao='Variedade')

        self.resp = self.client.get(r('core:create'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/cadastro.html')

    def test_str(self):
        self.assertEqual('Americana', str(self.obj))

    def test_context(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, StoreModelForm)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 5),
                ('type="text"', 4),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_create(self):
        self.assertTrue(Store.objects.exists)